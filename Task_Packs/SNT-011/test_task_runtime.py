import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from approval_acceptance import ApprovalRecord, ApprovalRequest
from task_runtime import TaskStateManager, prepare_intake


def manifest():
    return {
        "task_id": "SNT-TEST",
        "payload": "intake/state integration",
        "work_packages": [
            {"id": "research", "depends_on": [], "owner": "researcher"},
            {"id": "analysis", "depends_on": ["research"], "owner": "critical-analyst"},
            {"id": "draft", "depends_on": ["analysis"], "owner": "operator"},
            {"id": "independent", "depends_on": [], "owner": "operator"},
        ],
    }


def mutating_manifest():
    data = manifest()
    data["work_packages"][0]["mutating"] = True
    return data


def approval_for_research(**overrides):
    values = {
        "approval_id": "APR-RESEARCH",
        "task_id": "SNT-TEST",
        "proposal_id": "PROP-RESEARCH",
        "authority_id": "principal-operator",
        "target": "work-package:research",
        "scope": {"task_id": "SNT-TEST", "work_package": "research"},
        "action": "start",
        "payload_revision": "rev-1",
        "payload_digest": "digest-1",
        "expected_state": {"status": "IN_PROGRESS"},
        "rollback_path": "reset-research",
        "verification_receipt_id": "REC-RESEARCH",
        "verification_receipt_revision": "rev-1",
        "issued_at": "2026-11-12T00:00:00Z",
        "expires_at": "2026-11-12T02:00:00Z",
    }
    values.update(overrides)
    record = ApprovalRecord(**values)
    request_values = record.binding_fields()
    request_values["verification_result"] = "PASS"
    return record, ApprovalRequest(**request_values)


class IntakeStateTests(unittest.TestCase):
    def test_intake_compiles_and_initializes_ready_vs_pending(self):
        state = TaskStateManager(manifest())
        self.assertEqual(state.states["research"]["status"], "READY")
        self.assertEqual(state.states["analysis"]["status"], "PENDING")
        self.assertEqual(state.states["draft"]["status"], "PENDING")
        self.assertEqual(state.states["independent"]["status"], "READY")

    def test_completion_releases_only_next_dependency_layer(self):
        state = TaskStateManager(manifest())
        state.start("research")
        state.complete("research")
        self.assertEqual(state.states["analysis"]["status"], "READY")
        self.assertEqual(state.states["draft"]["status"], "PENDING")

    def test_failure_blocks_transitive_dependants_not_independent_work(self):
        state = TaskStateManager(manifest())
        state.start("research")
        state.fail("research", "source unavailable")
        self.assertEqual(state.states["analysis"]["status"], "BLOCKED")
        self.assertEqual(state.states["draft"]["status"], "BLOCKED")
        self.assertEqual(state.states["independent"]["status"], "READY")

    def test_cycle_and_downstream_are_blocked_at_intake(self):
        data = manifest()
        data["work_packages"] = [
            {"id": "A", "depends_on": ["B"]},
            {"id": "B", "depends_on": ["A"]},
            {"id": "C", "depends_on": ["B"]},
            {"id": "D", "depends_on": []},
        ]
        state = TaskStateManager(data)
        self.assertEqual(state.states["A"]["status"], "BLOCKED")
        self.assertEqual(state.states["B"]["status"], "BLOCKED")
        self.assertEqual(state.states["C"]["status"], "BLOCKED")
        self.assertEqual(state.states["D"]["status"], "READY")

    def test_start_rejects_pending_work(self):
        state = TaskStateManager(manifest())
        with self.assertRaisesRegex(ValueError, "not READY"):
            state.start("analysis")

    def test_state_persists_and_reloads(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = TaskStateManager(manifest(), path)
            state.start("research")
            state.complete("research")
            restored = TaskStateManager.load(path)
            self.assertEqual(restored.states["research"]["status"], "COMPLETED")
            self.assertEqual(restored.states["analysis"]["status"], "READY")

    def test_mutating_start_requires_task_bound_approval(self):
        state = TaskStateManager(mutating_manifest())
        with self.assertRaisesRegex(PermissionError, "LEVEL_D_DENIED: APPROVAL_MISSING"):
            state.start("research")

    def test_mutating_start_allows_exact_valid_approval(self):
        state = TaskStateManager(mutating_manifest())
        record, request = approval_for_research()
        state.start(
            "research",
            approval=record,
            approval_request=request,
            now=datetime(2026, 11, 12, 1, tzinfo=timezone.utc),
        )
        self.assertEqual(state.states["research"]["status"], "IN_PROGRESS")

    def test_mutating_start_rejects_scope_expansion(self):
        state = TaskStateManager(mutating_manifest())
        record, request = approval_for_research(
            scope={"task_id": "SNT-TEST", "work_package": "analysis"}
        )
        with self.assertRaisesRegex(PermissionError, "LEVEL_D_DENIED: APPROVAL_MISMATCH"):
            state.start(
                "research",
                approval=record,
                approval_request=request,
                now=datetime(2026, 11, 12, 1, tzinfo=timezone.utc),
            )


if __name__ == "__main__":
    unittest.main()
