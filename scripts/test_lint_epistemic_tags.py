#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_epistemic_tags import lint_text

class EpistemicLintTests(unittest.TestCase):
    def test_fact_with_locator_passes(self):
        self.assertEqual(lint_text("[FACT: PRIMARY_VERIFIED] The record was signed. [Q-014]"), [])

    def test_inference_with_locator_passes(self):
        self.assertEqual(lint_text("[INFERENCE: DEDUCTIVE_VALID] Therefore the branch is blocked. [Q2]"), [])

    def test_gap_abstention_needs_no_locator(self):
        self.assertEqual(lint_text("[GAP: UNVERIFIED_ABSTENTION] The date remains unknown."), [])

    def test_refuted_with_locator_passes(self):
        self.assertEqual(lint_text("[REFUTED] The asserted commit exists. [Q3]"), [])

    def test_untagged_assertion_fails_with_line_number(self):
        errors = lint_text("# Heading\n\nThe workflow blocks the merge.\n")
        self.assertTrue(any("<memory>:3: untagged assertion" in e for e in errors))

    def test_manufactured_tag_fails(self):
        errors = lint_text("[FACT: VERIFIED] The record is authentic. [Q1]")
        self.assertTrue(any("invalid/manufactured" in e for e in errors))

    def test_missing_locator_fails(self):
        errors = lint_text("[FACT: PRIMARY_VERIFIED] The record is authentic.")
        self.assertTrue(any("lacks a concrete citation locator" in e for e in errors))

    def test_placeholder_locator_fails(self):
        errors = lint_text("[FACT: PRIMARY_VERIFIED] The record is authentic. [Q#]")
        self.assertTrue(any("lacks a concrete citation locator" in e for e in errors))

    def test_mixed_tags_fail(self):
        errors = lint_text("[FACT: PRIMARY_VERIFIED] Source says X [Q1]. [INFERENCE: DEDUCTIVE_VALID] Therefore Y [Q2].")
        self.assertTrue(any("mixed epistemic tags" in e for e in errors))

    def test_tag_must_prefix_claim(self):
        errors = lint_text("The record is authentic. [FACT: PRIMARY_VERIFIED] [Q1]")
        self.assertTrue(any("must prefix" in e for e in errors))

    def test_fenced_code_is_ignored(self):
        fence = chr(96) * 3
        self.assertEqual(lint_text(fence + "text\nThe workflow blocks the merge.\n" + fence + "\n"), [])

    def test_heading_and_question_are_ignored(self):
        self.assertEqual(lint_text("# The workflow blocks the merge\n\nDoes it pass?\n"), [])

    def test_markdown_link_is_locator(self):
        self.assertEqual(lint_text("[FACT: PRIMARY_VERIFIED] The policy is current. [source](https://example.org/policy)"), [])

    def test_each_list_item_is_checked(self):
        errors = lint_text("- [FACT: PRIMARY_VERIFIED] The first rule applies. [Q1]\n- The second rule applies.\n")
        self.assertTrue(any(":2: untagged assertion" in e for e in errors))

if __name__ == "__main__":
    unittest.main(verbosity=2)
