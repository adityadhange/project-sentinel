"""Sentinel task intake and lifecycle adapter for the SNT-010 DAG compiler.

This module records task/work-package state. It does not dispatch agents,
grant permissions, or authorize Level D operations.
"""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Callable, Mapping

from approval_acceptance import ApprovalRecord, ApprovalRequest, validate_approval


def _load_compiler() -> Callable[[dict[str, list[str]]], dict[str, Any]]:
    compiler_path = Path(__file__).resolve().parents[1] / "SNT-010" / "sentinel_dag.py"
    spec = importlib.util.spec_from_file_location("sentinel_dag", compiler_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load dependency compiler at {compiler_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.compile_dag


compile_dag = _load_compiler()

WORK_STATES = {"PENDING", "READY", "IN_PROGRESS", "BLOCKED", "COMPLETED", "FAILED", "CANCELLED"}
TERMINAL_STATES = {"COMPLETED", "FAILED", "CANCELLED"}


class WIP1LockError(RuntimeError):
    """Raised when a second mutating work package attempts to acquire WIP-1."""


def prepare_intake(manifest: dict[str, Any]) -> dict[str, Any]:
    """Validate an intake manifest and compile its dependency graph.

    Required envelope:
      task_id: non-empty string
      payload: non-empty string
      work_packages: [{id: non-empty string, depends_on: [work-package IDs]}]
    """
    if not isinstance(manifest, dict):
        raise ValueError("intake manifest must be an object")
    task_id, payload = manifest.get("task_id"), manifest.get("payload")
    packages = manifest.get("work_packages")
    if not isinstance(task_id, str) or not task_id.strip():
        raise ValueError("task_id must be a non-empty string")
    if not isinstance(payload, str) or not payload.strip():
        raise ValueError("payload must be a non-empty string")
    if not isinstance(packages, list) or not packages:
        raise ValueError("work_packages must be a non-empty list")

    normalized: dict[str, dict[str, Any]] = {}
    for item in packages:
        if not isinstance(item, dict):
            raise ValueError("each work package must be an object")
        node_id = item.get("id")
        deps = item.get("depends_on", [])
        if not isinstance(node_id, str) or not node_id.strip():
            raise ValueError("work-package id must be a non-empty string")
        if node_id in normalized:
            raise ValueError(f"duplicate work-package id: {node_id}")
        if not isinstance(deps, list):
            raise ValueError(f"depends_on for {node_id!r} must be a list")
        owner = item.get("owner")
        mutating = item.get("mutating", False)
        level_d_required = item.get("level_d_required", False)
        if owner is not None and (not isinstance(owner, str) or not owner.strip()):
            raise ValueError(f"owner for {node_id!r} must be a non-empty string when supplied")
        if not isinstance(mutating, bool):
            raise ValueError(f"mutating for {node_id!r} must be a boolean")
        if not isinstance(level_d_required, bool):
            raise ValueError(f"level_d_required for {node_id!r} must be a boolean")
        normalized[node_id] = {
            "id": node_id,
            "depends_on": deps,
            "owner": owner,
            "mutating": mutating,
            "level_d_required": level_d_required,
        }

    graph = {node_id: item["depends_on"] for node_id, item in normalized.items()}
    compilation = compile_dag(graph)
    return {
        "task_id": task_id,
        "payload": payload,
        "work_packages": normalized,
        "compilation": compilation,
    }


class TaskStateManager:
    """Persist and transition work-package states from compiled dependencies."""

    def __init__(self, intake: dict[str, Any], state_path: str | Path | None = None):
        self.intake = prepare_intake(intake)
        self.state_path = Path(state_path) if state_path is not None else None
        compilation = self.intake["compilation"]
        blocked = set(compilation["blocked_nodes"])
        self.states: dict[str, dict[str, Any]] = {}
        for node_id, package in self.intake["work_packages"].items():
            if node_id in blocked:
                state = "BLOCKED"
                reason = compilation["blocked_reasons"].get(node_id, {})
            elif not package["depends_on"]:
                state = "READY"
                reason = None
            else:
                state = "PENDING"
                reason = None
            self.states[node_id] = {
                "status": state,
                "owner": package["owner"],
                "mutating": package["mutating"],
                "blocked_reason": reason,
            }
        self._refresh()
        self._save()

    @classmethod
    def load(cls, path: str | Path) -> "TaskStateManager":
        path = Path(path)
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("manifest"), dict):
            raise ValueError("persisted state must contain a valid manifest")
        instance = cls.__new__(cls)
        instance.intake = prepare_intake(data["manifest"])
        instance.state_path = path
        states = data.get("states")
        packages = instance.intake["work_packages"]
        if not isinstance(states, dict) or set(states) != set(packages):
            raise ValueError("persisted states must exactly match the manifest work packages")
        active_mutations = []
        for node_id, package in packages.items():
            item = states[node_id]
            if not isinstance(item, dict):
                raise ValueError(f"persisted state for {node_id!r} must be an object")
            status = item.get("status")
            if status not in WORK_STATES:
                raise ValueError(f"invalid persisted work state for {node_id!r}: {status!r}")
            if item.get("mutating") is not package["mutating"]:
                raise ValueError(f"persisted mutating flag mismatch for {node_id!r}")
            if item.get("owner") != package["owner"]:
                raise ValueError(f"persisted owner mismatch for {node_id!r}")
            if status in {"READY", "IN_PROGRESS", "COMPLETED"}:
                unmet = [dep for dep in package["depends_on"] if states[dep].get("status") != "COMPLETED"]
                if unmet:
                    raise ValueError(
                        f"persisted {status} package {node_id!r} has incomplete prerequisites: {', '.join(sorted(unmet))}"
                    )
            if package["mutating"] and status == "IN_PROGRESS":
                active_mutations.append(node_id)
        if len(active_mutations) > 1:
            raise WIP1LockError(
                "persisted state violates WIP-1: multiple mutating packages IN_PROGRESS: "
                + ", ".join(sorted(active_mutations))
            )
        instance.states = states
        instance._refresh()
        return instance

    def _refresh(self) -> None:
        statuses = [item["status"] for item in self.states.values()]
        if all(status == "COMPLETED" for status in statuses):
            self.task_status = "REVIEW"
        elif any(status == "IN_PROGRESS" for status in statuses):
            self.task_status = "ACTIVE"
        elif any(status == "READY" for status in statuses):
            self.task_status = "ACTIVE"
        elif any(status in {"BLOCKED", "FAILED", "CANCELLED"} for status in statuses):
            self.task_status = "BLOCKED"
        else:
            self.task_status = "WAITING"

    def _save(self) -> None:
        if self.state_path is None:
            return
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "manifest": {
                "task_id": self.intake["task_id"],
                "payload": self.intake["payload"],
                "work_packages": list(self.intake["work_packages"].values()),
            },
            "compilation": self.intake["compilation"],
            "states": self.states,
            "task_status": self.task_status,
        }
        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.state_path.parent,
                prefix=f".{self.state_path.name}.",
                suffix=".tmp",
                delete=False,
            ) as temporary:
                temporary.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
                temporary.flush()
                os.fsync(temporary.fileno())
                temporary_path = Path(temporary.name)
            os.replace(temporary_path, self.state_path)
        finally:
            if temporary_path is not None and temporary_path.exists():
                temporary_path.unlink()

    def snapshot(self) -> dict[str, Any]:
        return {
            "task_id": self.intake["task_id"],
            "task_status": self.task_status,
            "runnable_order": self.intake["compilation"]["runnable_order"],
            "states": {key: dict(value) for key, value in sorted(self.states.items())},
        }

    def start(
        self,
        node_id: str,
        *,
        approval_record: ApprovalRecord | Mapping[str, Any] | None = None,
        approval_request: ApprovalRequest | Mapping[str, Any] | None = None,
    ) -> None:
        """Start a READY package; mutating packages require a matching approval.

        This reference check fails closed on missing/invalid receipts. It does
        not authenticate the operator, atomically consume approval, or enforce
        host permissions; production enforcement remains a host responsibility.
        """
        item = self._get(node_id)
        if item["status"] != "READY":
            raise ValueError(f"{node_id!r} is not READY (current state: {item['status']})")
        if item["mutating"]:
            active_mutations = [
                other_id for other_id, other in self.states.items()
                if other_id != node_id and other["mutating"] and other["status"] == "IN_PROGRESS"
            ]
            if active_mutations:
                raise WIP1LockError(
                    f"WIP-1 lock held by mutating package(s): {', '.join(sorted(active_mutations))}"
                )
        package = self.intake["work_packages"][node_id]
        if item["mutating"] or package["level_d_required"]:
            if approval_record is None or approval_request is None:
                raise ValueError(
                    f"{node_id!r} is mutating and requires an explicit approval record and verification request"
                )
            record = ApprovalRecord(**approval_record) if isinstance(approval_record, Mapping) else approval_record
            request = ApprovalRequest(**approval_request) if isinstance(approval_request, Mapping) else approval_request
            if not isinstance(record, ApprovalRecord) or not isinstance(request, ApprovalRequest):
                raise ValueError("mutating work package approval inputs have invalid types")
            allowed, reasons = validate_approval(record, request)
            if not allowed:
                raise ValueError(
                    f"{node_id!r} approval validation failed closed: {', '.join(reasons)}"
                )
        unmet = [dep for dep in package["depends_on"]
                 if self.states[dep]["status"] != "COMPLETED"]
        if unmet:
            raise ValueError(f"{node_id!r} has incomplete prerequisites: {', '.join(sorted(unmet))}")
        item["status"] = "IN_PROGRESS"
        item["blocked_reason"] = None
        self._refresh()
        self._save()

    def complete(self, node_id: str) -> None:
        item = self._get(node_id)
        if item["status"] != "IN_PROGRESS":
            raise ValueError(f"{node_id!r} must be IN_PROGRESS before completion")
        item["status"] = "COMPLETED"
        item["blocked_reason"] = None
        self._release_ready()
        self._refresh()
        self._save()

    def fail(self, node_id: str, reason: str) -> None:
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError("failure reason must be a non-empty string")
        item = self._get(node_id)
        if item["status"] != "IN_PROGRESS":
            raise ValueError(f"{node_id!r} must be IN_PROGRESS before failure")
        item["status"] = "FAILED"
        item["blocked_reason"] = {"kind": "failed", "reason": reason}
        self._block_dependants(node_id, "failed_prerequisite")
        self._refresh()
        self._save()

    def block(self, node_id: str, reason: str) -> None:
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError("block reason must be a non-empty string")
        item = self._get(node_id)
        if item["status"] in TERMINAL_STATES:
            raise ValueError(f"cannot block terminal work package {node_id!r}")
        item["status"] = "BLOCKED"
        item["blocked_reason"] = {"kind": "manager_block", "reason": reason}
        self._block_dependants(node_id, "blocked_prerequisite")
        self._refresh()
        self._save()

    def _get(self, node_id: str) -> dict[str, Any]:
        if node_id not in self.states:
            raise KeyError(f"unknown work-package id: {node_id}")
        return self.states[node_id]

    def _block_dependants(self, failed_id: str, kind: str) -> None:
        queue = [failed_id]
        seen = {failed_id}
        while queue:
            prerequisite = queue.pop(0)
            for node_id, package in self.intake["work_packages"].items():
                if prerequisite not in package["depends_on"] or node_id in seen:
                    continue
                seen.add(node_id)
                state = self.states[node_id]["status"]
                if state not in TERMINAL_STATES:
                    self.states[node_id]["status"] = "BLOCKED"
                    self.states[node_id]["blocked_reason"] = {
                        "kind": kind, "prerequisite": prerequisite
                    }
                queue.append(node_id)

    def _release_ready(self) -> None:
        changed = True
        while changed:
            changed = False
            for node_id, package in self.intake["work_packages"].items():
                if self.states[node_id]["status"] != "PENDING":
                    continue
                if all(self.states[dep]["status"] == "COMPLETED" for dep in package["depends_on"]):
                    self.states[node_id]["status"] = "READY"
                    self.states[node_id]["blocked_reason"] = None
                    changed = True
