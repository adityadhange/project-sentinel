import hashlib
import unittest
from datetime import datetime, timezone

from approval_acceptance import (
    ApprovalRecord,
    ApprovalRequest,
    DeliverableContract,
    DeliverableSubmission,
    evaluate_acceptance,
    validate_approval,
)


NOW = datetime(2026, 11, 12, 1, 0, tzinfo=timezone.utc)


def approval(**overrides):
    values = {
        "approval_id": "APR-001",
        "task_id": "TASK-001",
        "proposal_id": "PROP-001",
        "authority_id": "principal-operator",
        "target": "target.md",
        "scope": {"path": "target.md", "namespace": "test"},
        "action": "overwrite",
        "payload_revision": "rev-1",
        "payload_digest": hashlib.sha256(b"payload-v1").hexdigest(),
        "digest_algorithm": "sha256",
        "expected_state": {"revision": "rev-1"},
        "rollback_path": "restore-rev-0",
        "verification_receipt_id": "REC-001",
        "verification_receipt_revision": "rev-1",
        "issued_at": "2026-11-12T00:00:00Z",
        "expires_at": "2026-11-12T02:00:00Z",
    }
    values.update(overrides)
    return ApprovalRecord(**values)


def request(**overrides):
    record = approval()
    values = record.binding_fields()
    values["payload_bytes"] = b"payload-v1"
    values["verification_result"] = "PASS"
    values.update(overrides)
    return ApprovalRequest(**values)


class ApprovalTests(unittest.TestCase):
    def test_approval_request_defaults_to_pending_and_rejects_omitted_result(self):
        values = approval().binding_fields()
        values["payload_bytes"] = b"payload-v1"
        candidate = ApprovalRequest(**values)
        self.assertEqual(candidate.verification_result, "PENDING")
        allowed, reasons = validate_approval(approval(), candidate, now=NOW)
        self.assertFalse(allowed)
        self.assertIn("APPROVAL_NOT_VERIFIED", reasons)

    def test_approval_request_requires_payload_bytes(self):
        with self.assertRaises(TypeError):
            ApprovalRequest(**approval().binding_fields())

    def test_exact_task_bound_approval_is_allowed(self):
        allowed, reasons = validate_approval(approval(), request(), now=NOW)
        self.assertTrue(allowed)
        self.assertEqual(reasons, ())

    def test_changed_scope_is_rejected(self):
        allowed, reasons = validate_approval(
            approval(), request(scope={"path": "other.md", "namespace": "test"}), now=NOW
        )
        self.assertFalse(allowed)
        self.assertIn("APPROVAL_MISMATCH", reasons)

    def test_expired_approval_is_rejected(self):
        allowed, reasons = validate_approval(approval(), request(), now=datetime(2026, 11, 12, 3, tzinfo=timezone.utc))
        self.assertFalse(allowed)
        self.assertIn("APPROVAL_EXPIRED", reasons)

    def test_consumed_approval_cannot_be_replayed(self):
        allowed, reasons = validate_approval(approval(lifecycle="CONSUMED"), request(), now=NOW)
        self.assertFalse(allowed)
        self.assertIn("APPROVAL_CONSUMED", reasons)

    def test_non_pass_receipt_cannot_authorize(self):
        for result in ("FAIL", "PARTIAL", "PENDING"):
            with self.subTest(result=result):
                allowed, reasons = validate_approval(approval(), request(verification_result=result), now=NOW)
                self.assertFalse(allowed)
                self.assertIn("APPROVAL_NOT_VERIFIED", reasons)

    def test_payload_digest_is_independently_derived_from_bytes(self):
        candidate = request(payload_digest="0" * 64)
        self.assertEqual(candidate.computed_payload_digest(), hashlib.sha256(b"payload-v1").hexdigest())
        allowed, reasons = validate_approval(approval(), candidate, now=NOW)
        self.assertFalse(allowed)
        self.assertIn("APPROVAL_MISMATCH", reasons)

    def test_unsupported_digest_algorithm_fails_closed(self):
        allowed, reasons = validate_approval(
            approval(), request(digest_algorithm="md5"), now=NOW
        )
        self.assertFalse(allowed)
        self.assertIn("APPROVAL_UNSUPPORTED", reasons)


class AcceptanceTests(unittest.TestCase):
    def test_submission_defaults_to_pending_and_is_rejected_without_explicit_pass(self):
        candidate = DeliverableSubmission(
            task_id="TASK-001", deliverable_id="DEL-001", revision="rev-1",
            producer_id="operator", coordinator_id="manager", verifier_id="verifier"
        )
        self.assertEqual(candidate.verification_result, "PENDING")
        result = evaluate_acceptance(self.contract(), candidate)
        self.assertEqual(result.status, "REJECTED")
        self.assertIn("VERIFICATION_NOT_PASS", result.reason_codes)

    def contract(self, level_d_required=False):
        return DeliverableContract(
            task_id="TASK-001",
            deliverable_id="DEL-001",
            required_fields=("summary", "evidence"),
            required_evidence=("E-001",),
            level_d_required=level_d_required,
        )

    def submission(self, **overrides):
        values = {
            "task_id": "TASK-001",
            "deliverable_id": "DEL-001",
            "revision": "rev-1",
            "producer_id": "operator",
            "coordinator_id": "manager",
            "verifier_id": "verifier",
            "present_fields": frozenset({"summary", "evidence"}),
            "evidence_refs": frozenset({"E-001"}),
            "verification_result": "PASS",
        }
        values.update(overrides)
        return DeliverableSubmission(**values)

    def test_complete_non_level_d_submission_is_ready_for_operator_decision(self):
        result = evaluate_acceptance(self.contract(), self.submission())
        self.assertEqual(result.status, "READY_FOR_OPERATOR_DECISION")
        self.assertEqual(result.reason_codes, ())

    def test_missing_evidence_is_rejected(self):
        result = evaluate_acceptance(self.contract(), self.submission(evidence_refs=frozenset()))
        self.assertEqual(result.status, "REJECTED")
        self.assertIn("EVIDENCE_MISSING", result.reason_codes)

    def test_verifier_cannot_be_producer_or_coordinator(self):
        result = evaluate_acceptance(self.contract(), self.submission(verifier_id="operator"))
        self.assertEqual(result.status, "BLOCKED")
        self.assertIn("ROLE_CONFLICT", result.reason_codes)

    def test_level_d_acceptance_requires_matching_approval(self):
        result = evaluate_acceptance(
            self.contract(level_d_required=True),
            self.submission(approval=approval(), approval_request=request()),
            now=NOW,
        )
        self.assertEqual(result.status, "READY_FOR_OPERATOR_DECISION")

    def test_level_d_acceptance_blocks_missing_approval(self):
        result = evaluate_acceptance(self.contract(level_d_required=True), self.submission(), now=NOW)
        self.assertEqual(result.status, "BLOCKED")
        self.assertIn("APPROVAL_MISSING", result.reason_codes)


if __name__ == "__main__":
    unittest.main()
