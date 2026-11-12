"""Reference approval-provenance and deliverable-acceptance checks.

This module is intentionally non-production. It validates records supplied by a
caller; it does not authenticate identities, persist approvals, reserve tokens,
perform mutations, or enforce host permissions.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Mapping, Sequence


BLOCKING_APPROVAL_REASONS = {
    "APPROVAL_MISSING",
    "APPROVAL_MISMATCH",
    "APPROVAL_EXPIRED",
    "APPROVAL_REVOKED",
    "APPROVAL_SUPERSEDED",
    "APPROVAL_CONSUMED",
    "APPROVAL_NOT_VERIFIED",
    "APPROVAL_UNSUPPORTED",
}


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamps must include a timezone")
    return parsed.astimezone(timezone.utc)


@dataclass(frozen=True)
class ApprovalRecord:
    """A task-bound approval record; identity authentication is out of scope."""

    approval_id: str
    task_id: str
    proposal_id: str
    authority_id: str
    target: str
    scope: Mapping[str, Any]
    action: str
    payload_revision: str
    payload_digest: str
    expected_state: Mapping[str, Any]
    rollback_path: str
    verification_receipt_id: str
    verification_receipt_revision: str
    issued_at: str
    expires_at: str | None = None
    digest_algorithm: str = "sha256"
    decision: str = "APPROVED"
    lifecycle: str = "UNUSED"
    revoked_at: str | None = None
    superseded_by: str | None = None

    def binding_fields(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "proposal_id": self.proposal_id,
            "target": self.target,
            "scope": self.scope,
            "action": self.action,
            "payload_revision": self.payload_revision,
            "payload_digest": self.payload_digest,
            "digest_algorithm": self.digest_algorithm,
            "expected_state": self.expected_state,
            "rollback_path": self.rollback_path,
            "verification_receipt_id": self.verification_receipt_id,
            "verification_receipt_revision": self.verification_receipt_revision,
        }

    def fingerprint(self) -> str:
        return hashlib.sha256(_canonical(self.binding_fields()).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ApprovalRequest:
    task_id: str
    proposal_id: str
    target: str
    scope: Mapping[str, Any]
    action: str
    payload_revision: str
    payload_digest: str
    expected_state: Mapping[str, Any]
    rollback_path: str
    verification_receipt_id: str
    verification_receipt_revision: str
    payload_bytes: bytes
    verification_result: str = "PENDING"
    digest_algorithm: str = "sha256"

    def computed_payload_digest(self) -> str:
        if self.digest_algorithm != "sha256":
            raise ValueError(f"unsupported digest algorithm: {self.digest_algorithm}")
        if not isinstance(self.payload_bytes, bytes):
            raise TypeError("payload_bytes must be bytes")
        return hashlib.sha256(self.payload_bytes).hexdigest()

    def binding_fields(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "proposal_id": self.proposal_id,
            "target": self.target,
            "scope": self.scope,
            "action": self.action,
            "payload_revision": self.payload_revision,
            "payload_digest": self.payload_digest,
            "digest_algorithm": self.digest_algorithm,
            "expected_state": self.expected_state,
            "rollback_path": self.rollback_path,
            "verification_receipt_id": self.verification_receipt_id,
            "verification_receipt_revision": self.verification_receipt_revision,
        }

    def fingerprint(self) -> str:
        return hashlib.sha256(_canonical(self.binding_fields()).encode("utf-8")).hexdigest()


def validate_approval(
    record: ApprovalRecord | None,
    request: ApprovalRequest,
    *,
    now: datetime | None = None,
    authority_id: str = "principal-operator",
) -> tuple[bool, tuple[str, ...]]:
    """Return whether a record authorizes this exact request.

    This is a deterministic reference check. It does not authenticate the
    authority, atomically consume the record, or contact an external system.
    """
    reasons: list[str] = []
    if record is None:
        return False, ("APPROVAL_MISSING",)
    if record.decision != "APPROVED":
        reasons.append("APPROVAL_UNSUPPORTED")
    if record.authority_id != authority_id:
        reasons.append("APPROVAL_UNSUPPORTED")
    if record.lifecycle == "CONSUMED":
        reasons.append("APPROVAL_CONSUMED")
    elif record.lifecycle != "UNUSED":
        reasons.append("APPROVAL_UNSUPPORTED")
    if record.revoked_at is not None:
        reasons.append("APPROVAL_REVOKED")
    if record.superseded_by is not None:
        reasons.append("APPROVAL_SUPERSEDED")
    if record.verification_receipt_revision != request.payload_revision:
        reasons.append("APPROVAL_NOT_VERIFIED")
    if request.verification_result != "PASS":
        reasons.append("APPROVAL_NOT_VERIFIED")
    try:
        actual_digest = request.computed_payload_digest()
    except (TypeError, ValueError):
        actual_digest = None
        reasons.append("APPROVAL_UNSUPPORTED")
    if actual_digest is not None and actual_digest != request.payload_digest:
        reasons.append("APPROVAL_MISMATCH")
    if record.digest_algorithm != "sha256" or request.digest_algorithm != "sha256":
        reasons.append("APPROVAL_UNSUPPORTED")
    if record.binding_fields() != request.binding_fields():
        reasons.append("APPROVAL_MISMATCH")

    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    issued = _parse_time(record.issued_at)
    if issued > current:
        reasons.append("APPROVAL_UNSUPPORTED")
    if record.expires_at is not None and current >= _parse_time(record.expires_at):
        reasons.append("APPROVAL_EXPIRED")

    return not reasons, tuple(dict.fromkeys(reasons))


@dataclass(frozen=True)
class DeliverableContract:
    task_id: str
    deliverable_id: str
    required_fields: tuple[str, ...] = ()
    required_evidence: tuple[str, ...] = ()
    level_d_required: bool = False


@dataclass(frozen=True)
class DeliverableSubmission:
    task_id: str
    deliverable_id: str
    revision: str
    producer_id: str
    coordinator_id: str
    verifier_id: str
    verification_result: str = "PENDING"
    present_fields: frozenset[str] = frozenset()
    evidence_refs: frozenset[str] = frozenset()
    approval: ApprovalRecord | None = None
    approval_request: ApprovalRequest | None = None


@dataclass(frozen=True)
class AcceptanceDecision:
    status: str
    reason_codes: tuple[str, ...] = field(default_factory=tuple)
    approval_reasons: tuple[str, ...] = field(default_factory=tuple)


def evaluate_acceptance(contract: DeliverableContract, submission: DeliverableSubmission, *, now: datetime | None = None) -> AcceptanceDecision:
    """Evaluate a submission without accepting it on behalf of an operator."""
    reasons: list[str] = []
    if submission.task_id != contract.task_id or submission.deliverable_id != contract.deliverable_id:
        reasons.append("SCOPE_EXCEEDED")
    if submission.verifier_id in {submission.producer_id, submission.coordinator_id}:
        reasons.append("ROLE_CONFLICT")
    reasons.extend("STRUCTURAL_MISSING" for item in contract.required_fields if item not in submission.present_fields)
    reasons.extend("EVIDENCE_MISSING" for item in contract.required_evidence if item not in submission.evidence_refs)
    if submission.verification_result != "PASS":
        reasons.append("VERIFICATION_NOT_PASS")

    approval_reasons: tuple[str, ...] = ()
    if contract.level_d_required:
        if submission.approval_request is None:
            approval_reasons = ("APPROVAL_MISSING",)
            reasons.extend(approval_reasons)
        else:
            allowed, approval_reasons = validate_approval(
                submission.approval,
                submission.approval_request,
                now=now,
            )
            if not allowed:
                reasons.extend(approval_reasons)

    if any(reason in BLOCKING_APPROVAL_REASONS for reason in reasons) or "ROLE_CONFLICT" in reasons:
        status = "BLOCKED"
    elif reasons:
        status = "REJECTED"
    else:
        status = "READY_FOR_OPERATOR_DECISION"
    return AcceptanceDecision(status, tuple(dict.fromkeys(reasons)), approval_reasons)
