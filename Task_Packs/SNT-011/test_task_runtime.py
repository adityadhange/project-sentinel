import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from task_runtime import TaskStateManager, WIP1LockError, prepare_intake
from approval_acceptance import ApprovalRecord, ApprovalRequest


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


class IntakeStateTests(unittest.TestCase):
    def test_mutating_start_fails_closed_without_approval(self):
        data = {
            "task_id": "SNT-MUTATE", "payload": "mutation",
            "work_packages": [{"id": "mutate", "depends_on": [], "mutating": True}],
        }
        state = TaskStateManager(data)
        with self.assertRaisesRegex(ValueError, "requires an explicit approval"):
            state.start("mutate")
        self.assertEqual(state.states["mutate"]["status"], "READY")

    def test_mutating_start_requires_matching_pass_receipt(self):
        data = {
            "task_id": "TASK-001", "payload": "mutation",
            "work_packages": [{"id": "mutate", "depends_on": [], "mutating": True}],
        }
        state = TaskStateManager(data)
        fields = {
            "task_id": "TASK-001", "proposal_id": "PROP-001", "target": "work-package:mutate",
            "scope": {"work_package": "mutate"}, "action": "overwrite", "payload_revision": "rev-1",
            "payload_digest": hashlib.sha256(b"runtime-payload").hexdigest(),
            "digest_algorithm": "sha256", "expected_state": {"revision": "rev-1"},
            "rollback_path": "restore-rev-0", "verification_receipt_id": "REC-001",
            "verification_receipt_revision": "rev-1",
        }
        record = ApprovalRecord(
            approval_id="APR-001", authority_id="principal-operator",
            issued_at="2020-01-01T00:00:00Z", **fields,
        )
        request = ApprovalRequest(**fields, payload_bytes=b"runtime-payload", verification_result="PASS")
        state.start("mutate", approval_record=record, approval_request=request)
        self.assertEqual(state.states["mutate"]["status"], "IN_PROGRESS")

    def test_mutating_start_rejects_approval_not_bound_to_active_task_and_package(self):
        base = {
            "task_id": "TASK-BOUND",
            "proposal_id": "PROP-BOUND",
            "target": "work-package:mutate",
            "scope": {"work_package": "mutate"},
            "action": "overwrite",
            "payload_revision": "rev-1",
            "payload_digest": hashlib.sha256(b"bound-payload").hexdigest(),
            "digest_algorithm": "sha256",
            "expected_state": {"revision": "rev-1"},
            "rollback_path": "restore-rev-0",
            "verification_receipt_id": "REC-BOUND",
            "verification_receipt_revision": "rev-1",
        }
        invalid_bindings = (
            ("task_id", "OTHER-TASK", "active intake task"),
            ("target", "work-package:other", "active work package"),
            ("scope", {"work_package": "other"}, "active work package"),
        )
        for field, value, message in invalid_bindings:
            with self.subTest(field=field):
                state = TaskStateManager({
                    "task_id": "TASK-BOUND",
                    "payload": "mutation",
                    "work_packages": [{"id": "mutate", "depends_on": [], "mutating": True}],
                })
                fields = dict(base)
                fields[field] = value
                record = ApprovalRecord(
                    approval_id="APR-BOUND",
                    authority_id="principal-operator",
                    issued_at="2020-01-01T00:00:00Z",
                    **fields,
                )
                request = ApprovalRequest(
                    **fields,
                    payload_bytes=b"bound-payload",
                    verification_result="PASS",
                )
                with self.assertRaisesRegex(ValueError, message):
                    state.start("mutate", approval_record=record, approval_request=request)
                self.assertEqual(state.states["mutate"]["status"], "READY")

    def test_wip1_rejects_second_concurrent_mutating_package(self):
        data = {
            "task_id": "TASK-WIP1", "payload": "two mutations",
            "work_packages": [
                {"id": "mutate-a", "depends_on": [], "mutating": True},
                {"id": "mutate-b", "depends_on": [], "mutating": True},
            ],
        }
        state = TaskStateManager(data)
        fields = {
            "task_id": "TASK-WIP1", "proposal_id": "PROP-WIP1", "target": "work-package:mutate-a",
            "scope": {"work_package": "mutate-a"}, "action": "overwrite",
            "payload_revision": "rev-1",
            "payload_digest": hashlib.sha256(b"runtime-payload").hexdigest(),
            "digest_algorithm": "sha256", "expected_state": {"revision": "rev-1"},
            "rollback_path": "restore", "verification_receipt_id": "REC-WIP1",
            "verification_receipt_revision": "rev-1",
        }
        record = ApprovalRecord(
            approval_id="APR-WIP1", authority_id="principal-operator",
            issued_at="2020-01-01T00:00:00Z", **fields,
        )
        request = ApprovalRequest(**fields, payload_bytes=b"runtime-payload", verification_result="PASS")
        state.start("mutate-a", approval_record=record, approval_request=request)
        with self.assertRaises(WIP1LockError):
            state.start("mutate-b", approval_record=record, approval_request=request)
        self.assertEqual(state.states["mutate-b"]["status"], "READY")

    def test_level_d_package_requires_approval_even_when_mutating_flag_is_false(self):
        data = {
            "task_id": "TASK-LEVEL-D", "payload": "level d",
            "work_packages": [
                {"id": "level-d", "depends_on": [], "mutating": False, "level_d_required": True},
            ],
        }
        state = TaskStateManager(data)
        with self.assertRaisesRegex(ValueError, "requires an explicit approval"):
            state.start("level-d")
        self.assertEqual(state.states["level-d"]["status"], "READY")

    def test_load_rejects_invalid_persisted_work_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            TaskStateManager(manifest(), path)
            data = json.loads(path.read_text(encoding="utf-8"))
            data["states"]["research"]["status"] = "RUNNING"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid persisted work state"):
                TaskStateManager.load(path)

    def test_load_rejects_persisted_ready_state_with_incomplete_prerequisite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            TaskStateManager(manifest(), path)
            data = json.loads(path.read_text(encoding="utf-8"))
            data["states"]["analysis"]["status"] = "READY"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "incomplete prerequisites"):
                TaskStateManager.load(path)

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


if __name__ == "__main__":
    unittest.main()
