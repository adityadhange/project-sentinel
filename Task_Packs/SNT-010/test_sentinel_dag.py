import unittest

from sentinel_dag import compile_dag


class CompileDagTests(unittest.TestCase):
    def test_valid_graph_returns_stable_topological_order(self):
        result = compile_dag({
            "publish": ["draft"],
            "draft": ["research"],
            "research": [],
            "independent": [],
        })
        self.assertTrue(result["valid"])
        self.assertEqual(result["runnable_order"], ["independent", "research", "draft", "publish"])
        self.assertEqual(result["blocked_nodes"], [])

    def test_cycle_blocks_downstream_but_preserves_independent_branch(self):
        result = compile_dag({
            "A": ["B"],
            "B": ["A"],
            "C": ["B"],
            "D": [],
            "E": ["D"],
        })
        self.assertFalse(result["valid"])
        self.assertEqual(result["cycle_components"], [["A", "B"]])
        self.assertEqual(result["blocked_nodes"], ["A", "B", "C"])
        self.assertEqual(result["runnable_order"], ["D", "E"])

    def test_self_dependency_is_a_cycle(self):
        result = compile_dag({"A": ["A"], "B": []})
        self.assertEqual(result["cycle_components"], [["A"]])
        self.assertEqual(result["blocked_nodes"], ["A"])
        self.assertEqual(result["runnable_order"], ["B"])

    def test_unknown_prerequisite_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown prerequisite"):
            compile_dag({"draft": ["missing"]})

    def test_duplicate_prerequisite_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "contain duplicates"):
            compile_dag({"draft": ["research", "research"], "research": []})

    def test_empty_graph_is_valid(self):
        result = compile_dag({})
        self.assertTrue(result["valid"])
        self.assertEqual(result["runnable_order"], [])


