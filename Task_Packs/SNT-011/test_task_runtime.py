import tempfile
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
