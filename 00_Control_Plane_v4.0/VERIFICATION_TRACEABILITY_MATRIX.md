# Verification & Traceability Matrix — Kernel v4.0

**Document ID:** SNT-VERIFICATION-TRACEABILITY-MATRIX  
**Version:** 1.0  
**Status:** Reviewable traceability baseline — evidence scope and limitations explicit  
**Architecture invariant:** Sentinel is the sole governing kernel; Optimus is a subordinate orchestration subsystem.  
**Primary empirical test reference:** TASK-2026-RP04B-ACCEPTANCE  
**Supplied checksum identifier:** SHA256-4D9A11C8E03B7F21

## 1. Purpose and evidence rules

This matrix links the requirements tracked by GitHub Issues #32–#37 to the governing specifications, the RP-04B Strike-1 rejection/acceptance test reference, and the strength of evidence actually available for inspection.

The test identifier and checksum above were supplied by the Principal Operator as the reference for the empirical RP-04B acceptance test. The repository search performed for this change did not locate the raw test transcript, fixture/payload bytes, execution log, or an independently generated checksum manifest. Accordingly:

- The reported Strike-1 rejection/acceptance outcome is recorded as an **operator-supplied empirical test reference**, not as a raw artifact independently re-executed during this PR.
- The checksum string is preserved exactly as supplied. It has **not** been recomputed or cryptographically validated in this PR.
- The test reference supports traceability to the reported test cycle; it does not, by itself, prove host-level enforcement, platform permissions, independent Verifier access, or successful post-mutation read-back.
- A documented control, a test-referenced control, an implemented control, and a host-enforced/independently verified control are different evidence states. This matrix never promotes one state into another.

## 2. Canonical traceability states

| State | Meaning |
|---|---|
| SPECIFIED | Requirement or control is stated in a governing document. |
| TEST-REFERENCED | A named test and outcome are referenced, but raw evidence is not independently available in this repository change. |
| IMPLEMENTED | Concrete executable implementation is present at the cited repository location. |
| TESTED | A reproducible test artifact and result demonstrate execution. |
| INDEPENDENTLY VERIFIED | An independent verifier inspected/reproduced the result and its evidence. |
| ACCEPTED | The authorized acceptance authority recorded acceptance for the exact revision/scope. |
| GAP / NOT PROVEN | Evidence is absent or insufficient; no affirmative implementation or enforcement claim is made. |

A row may carry more than one state where the evidence differs by layer. SPECIFIED is not synonymous with IMPLEMENTED, and TEST-REFERENCED is not synonymous with INDEPENDENTLY VERIFIED.

## 3. Requirements-to-evidence matrix

| GitHub issue / requirement | Governing control and repository location | RP-04B evidence relationship | Traceability disposition and remaining boundary |
|---|---|---|---|
| **#32 — SNT-TO-01: Evidence-backed RP-04B test-cycle disposition** | This matrix records test identity, reported outcome, evidence provenance, and gaps. Manager §6 (deliverable acceptance and verification), §6.1 (receipt binding), and §7 (Level D gate) in 00_Control_Plane_v4.0/sentinel-manager.md. | TASK-2026-RP04B-ACCEPTANCE; supplied checksum identifier SHA256-4D9A11C8E03B7F21. The referenced test is described by the operator as the Strike-1 rejection/acceptance test. | **SPECIFIED + TEST-REFERENCED.** This matrix makes the reported disposition traceable. Raw test inventory, fixtures, event transcript, and independently recomputed checksum remain **GAP / NOT PROVEN** in this PR. |
| **#33 — SNT-TO-02: Task-bound Level D approval provenance** | Mandatory payload-bound schema in Manager §7 and Operator §7: Proposal_ID, Bound_Task_ID, Target_Scope, Payload_Checksum. Confirmation syntax: APPROVE <Proposal_ID> [<Payload_Checksum>]. | Strike-1 rejection/acceptance is the referenced empirical probe for rejecting an unbound/incomplete proposal and accepting a corrected proposal. Exact test vectors and event log are not present in the repository evidence inspected for this PR. | **SPECIFIED + TEST-REFERENCED.** The four-field contract and exact confirmation are now explicit. Runtime rejection of missing, stale, replayed, or mismatched values remains **NOT PROVEN** absent inspectable execution evidence. |
| **#34 — SNT-TO-03: Independent deliverable acceptance, rejection, and rework (MG-04)** | Manager §6 requires independent audit of the exact candidate revision, consolidated defect reporting, bounded correction, and fresh audit after material edits. Operator §6 assigns Strike-1 correction to the producer and prevents self-certification. | The named RP-04B test reference is the reported Strike-1 rejection/acceptance evidence point: rejection precedes correction/acceptance; a producer's assertion alone is not an independent PASS receipt. | **SPECIFIED + TEST-REFERENCED.** The rework and role-separation contract is documented. The raw rejection record, corrected candidate, Verifier receipt, and independent audit transcript are not embedded here; full empirical verification remains **NOT PROVEN** by this PR alone. |
| **#35 — SNT-TO-04: Level D authorization enforcement across execution paths (MG-05)** | Manager §§7–8 and Operator §§7–8 define proposal validation, human authorization, bounded execution, and independent read-back. The approval is bound to task, target/scope, and exact payload checksum. | The RP-04B test reference can support proposal-shape and approval-gate behavior only to the extent exercised by that test. It is not evidence that every live entry point, delegation route, replay path, or host execution API enforces the gate. | **SPECIFIED + TEST-REFERENCED (limited).** End-to-end host enforcement across all execution paths, bypass resistance, revocation, replay prevention, and post-mutation read-back are **GAP / NOT PROVEN**. No claim of runtime enforcement is made. |
| **#36 — SNT-TO-05: Authoritative architecture source baseline** | Kernel v4.0 source baseline and authority boundary are stated in the governing control-plane documents, including Manager and Operator specifications. This matrix preserves the Single-Kernel Monism invariant: Sentinel governs; Optimus is subordinate. | RP-04B is a downstream behavioral test reference; it does not establish source provenance or settle architecture discrepancies by itself. | **SPECIFIED / TRACEABLE AT CITED FILES.** The current control-plane documents are identified as sources. A complete v3.6-to-v4 source inventory and discrepancy-by-discrepancy provenance audit are not reproduced in this matrix; any unresolved source conflicts remain unresolved rather than silently settled. |
| **#37 — SNT-TO-06: Canonical requirements-to-implementation-to-test map** | This document is the canonical issue-level requirements-to-evidence index for #32–#37. Manager and Operator paths above identify the governing control locations. | The test reference is connected to the specific requirements it is reported to exercise, with the raw-evidence limitation stated. | **SPECIFIED.** The index distinguishes specification, test reference, implementation, independent verification, acceptance, and gaps. It does not certify untested mechanisms or convert the test reference into proof of implementation. |

## 4. Mandatory Payload-Bound Level D Schema

Every [LEVEL_D_PROPOSAL] is invalid unless all four binding fields are present, non-empty, and mutually consistent:

| Field | Mandatory meaning | Fail-closed condition |
|---|---|---|
| Proposal_ID | Unique immutable identifier for this proposal instance. | Missing, duplicate, malformed, or superseded proposal identity. |
| Bound_Task_ID | Exact task identifier whose authorized work gives rise to this proposal. | Missing task ID or mismatch with the active task/work package. |
| Target_Scope | Exact target resource and namespace, operation, and bounded scope of permitted change. | Ambiguous target, unbounded scope, or scope mismatch. |
| Payload_Checksum | Algorithm and checksum of the exact payload/diff to be executed. | Missing checksum, malformed checksum, mismatch, or any payload change after verification/approval. |

Canonical proposal envelope:

~~~text
[LEVEL_D_PROPOSAL]
Proposal_ID: {unique immutable proposal identifier}
Bound_Task_ID: {exact TASK_ID}
Target_Scope: {exact target resource, namespace, operation and bounded scope}
Payload_Checksum: {algorithm and checksum of exact payload}
Action: {precise operation}
Payload: {complete payload or exact diff; immutable artifact/revision}
Consequences: {material consequences and dependencies}
Verifier_Receipt: {current independent PASS receipt bound to this exact payload/revision}
Recovery: {rollback/recovery procedure and limitations}
Approval_Confirmation_Required: APPROVE <Proposal_ID> [<Payload_Checksum>]
~~~

The Principal Operator's authorization must be a verbatim confirmation using the values in the current proposal:

~~~text
APPROVE <Proposal_ID> [<Payload_Checksum>]
~~~

No approval is valid if any binding field is missing or if the task, target, scope, payload, checksum, or proposal identity differs from the verified proposal. A material change requires a new proposal, a fresh applicable Verifier PASS receipt, and fresh approval. A checksum match establishes payload identity only; it does not establish that the payload is safe, correctly scoped, or authorized.

## 5. Evidence record for RP-04B Strike-1 rejection/acceptance

| Attribute | Recorded value |
|---|---|
| Test/task identifier | TASK-2026-RP04B-ACCEPTANCE |
| Checksum identifier supplied | SHA256-4D9A11C8E03B7F21 |
| Test family | RP-04B governance acceptance |
| Referenced behavior | Strike-1 rejection followed by correction/acceptance assessment |
| Provenance in this PR | Principal-Operator-supplied identifier and checksum string |
| Raw test payload/transcript available in this PR | No |
| Checksum independently recomputed in this PR | No |
| Independent re-execution in this PR | No |
| Evidence interpretation | A traceable test reference, not independently inspected raw proof |

### Acceptance interpretation

The test reference is relevant to the governance contract: defective or insufficiently bound work must be rejected at the first verification strike, while corrected work may proceed only after the applicable acceptance conditions are met. The test reference must not be used to claim that every Level D route is enforced in a live host environment, that a Verifier has independent access on every platform, or that a post-mutation read-back has occurred.

To upgrade this record from TEST-REFERENCED to TESTED and INDEPENDENTLY VERIFIED, preserve and attach the original test fixture/payload, exact expected and observed outputs, event/transcript record, verifier identity/independence evidence, and a reproducible checksum manifest. The evidence must remain bound to the same task and artifact revision.

## 6. Change-impact and maintenance rules

1. A change to a requirement updates its source reference, affected implementation locations, test mapping, and status in this matrix.
2. A change to any of the four Level D binding fields requires updating the Manager and Operator contracts, positive/negative test vectors, and all dependent approval-flow documentation.
3. A material change to a proposal payload invalidates the old checksum, receipt applicability, and approval. Re-propose, re-verify, and re-authorize.
4. Test execution status and independent verification status must be recorded separately.
5. A missing artifact, unavailable platform capability, or unexecuted test is recorded as GAP / NOT PROVEN; it must never be promoted based on narrative confidence or agent consensus.
6. The matrix is a traceability index, not a grant of host permissions, execution authority, or approval to perform consequential actions.

## 7. Issue closure boundary

This PR supplies the requested traceability artifact and aligns the Manager and Operator Level D proposal/approval templates. The PR description links Issues #32–#37 for automatic closure on merge as requested. Their closure must not be interpreted as proof that the unverified host-enforcement and raw-test-evidence gaps listed above have been empirically resolved. The limitations remain explicit in the repository record.
