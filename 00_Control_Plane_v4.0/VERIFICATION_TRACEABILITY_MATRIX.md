# Verification & Traceability Matrix — Kernel v4.0

**Document ID:** SNT-VERIFICATION-TRACEABILITY-MATRIX  
**Version:** 1.1  
**Status:** OPEN — BASELINE STAGED; acceptance, enforcement, and independent source-reconciliation evidence remain outstanding  
**Architecture invariant:** Sentinel is the sole governing kernel; Optimus is a subordinate orchestration subsystem.  
**Synthetic specification dry-run reference:** TASK-2026-RP04B-ACCEPTANCE  
**Synthetic dry-run label:** [SYNTHETIC-DRYRUN-ID: RP04B-001]
**Supplied checksum identifier:** SIM-DIGEST-RP04B

## 1. Purpose and evidence rules

This matrix links GitHub Issues #32–#37 to governing specifications and a synthetic RP-04B specification dry run. It is an OPEN — BASELINE STAGED tracking baseline, not a declaration that the issues' acceptance criteria are complete.

The identifier and checksum string below identify a synthetic specification dry run supplied by the Principal Operator. This dry run exercised specification-level reasoning only; it was not executed against a live host/runtime and is not empirical host-enforcement proof. The identifier is not evidence of an independently reproduced test. Accordingly:

- The reported Strike-1 rejection/acceptance scenario is recorded only as a **synthetic specification dry run**. It is not a live runtime test, a production acceptance test, or independently verified empirical evidence.
- The checksum string is preserved exactly as supplied. It has **not** been recomputed or cryptographically validated in this PR.
- The dry-run reference supports traceability to a specification exercise only. It does not prove implementation, host-level enforcement, platform permissions, independent Verifier access, or successful post-mutation read-back.
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
| **#32 — SNT-TO-01: Evidence-backed RP-04B test-cycle disposition** | This matrix records test identity, reported outcome, evidence provenance, and gaps. Manager §6 (deliverable acceptance and verification), §6.1 (receipt binding), and §7 (Level D gate) in 00_Control_Plane_v4.0/sentinel-manager.md. | TASK-2026-RP04B-ACCEPTANCE; supplied checksum identifier SIM-DIGEST-RP04B; synthetic specification dry run only. The reference is a synthetic specification dry run of the Strike-1 rejection/acceptance scenario, not a live host test. | **OPEN — BASELINE STAGED. SPECIFIED; dry-run reference only.** This matrix makes the reported disposition traceable. Raw test inventory, fixtures, event transcript, and independently recomputed checksum remain **GAP / NOT PROVEN** in this PR. |
| **#33 — SNT-TO-02: Task-bound Level D approval provenance** | Mandatory payload-bound schema in Manager §7 and Operator §7: Proposal_ID, Bound_Task_ID, Target_Scope, Payload_Checksum. Confirmation syntax: APPROVE <Proposal_ID> [<Payload_Checksum>]. | The synthetic specification dry run modeled rejection of an unbound/incomplete proposal and acceptance assessment of a corrected proposal; it did not exercise live runtime enforcement. Exact test vectors and event log are not present in the repository evidence inspected for this PR. | **SPECIFIED + TEST-REFERENCED.** The four-field contract and exact confirmation are now explicit. Runtime rejection of missing, stale, replayed, or mismatched values remains **NOT PROVEN** absent inspectable execution evidence. |
| **#34 — SNT-TO-03: Independent deliverable acceptance, rejection, and rework (MG-04)** | Manager §6 requires independent audit of the exact candidate revision, consolidated defect reporting, bounded correction, and fresh audit after material edits. Operator §6 assigns Strike-1 correction to the producer and prevents self-certification. | The synthetic specification dry run modeled a Strike-1 rejection/correction/acceptance sequence. It is not empirical evidence that independent acceptance occurred in a live execution environment. | **SPECIFIED + TEST-REFERENCED.** The rework and role-separation contract is documented. The raw rejection record, corrected candidate, Verifier receipt, and independent audit transcript are not embedded here; full empirical verification remains **NOT PROVEN** by this PR alone. |
| **#35 — SNT-TO-04: Level D authorization enforcement across execution paths (MG-05)** | Manager §§7–8 and Operator §§7–8 define proposal validation, human authorization, bounded execution, and independent read-back. The approval is bound to task, target/scope, and exact payload checksum. | The synthetic dry run can illustrate proposal-shape and approval-gate specification only. It does not test even one live host entry point, delegation route, replay path, or host execution API. | **OPEN — BASELINE STAGED. SPECIFIED; dry-run reference only. [PR #42](https://github.com/adityadhange/project-sentinel/pull/42): REFERENCE_PROTOTYPE (UNPROVEN_IN_PROD).** End-to-end host enforcement across all execution paths, bypass resistance, revocation, replay prevention, and post-mutation read-back are **GAP / NOT PROVEN**. No claim of runtime enforcement is made. |
| **#36 — SNT-TO-05: Authoritative architecture source baseline** | Kernel v4.0 source baseline and authority boundary are stated in the governing control-plane documents, including Manager and Operator specifications. This matrix preserves the Single-Kernel Monism invariant: Sentinel governs; Optimus is subordinate. | The RP-04B synthetic specification dry run is not a source-provenance audit and does not settle architecture discrepancies. | **OPEN — BASELINE STAGED. SPECIFIED / PARTIALLY TRACEABLE.** The current control-plane documents are identified as sources. A complete v3.6-to-v4 source inventory and discrepancy-by-discrepancy provenance audit are not reproduced in this matrix; any unresolved source conflicts remain unresolved rather than silently settled. |
| **#37 — SNT-TO-06: Canonical requirements-to-implementation-to-test map** | This document is the canonical issue-level requirements-to-evidence index for #32–#37. Manager and Operator paths above identify the governing control locations. | The synthetic dry-run reference is connected to relevant requirements as a specification exercise only; it is not empirical test evidence. | **OPEN — BASELINE STAGED.** The index distinguishes specification, test reference, implementation, independent verification, acceptance, and gaps. It does not certify untested mechanisms or convert the test reference into proof of implementation. |

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
| Checksum identifier supplied | SIM-DIGEST-RP04B |
| Test family | RP-04B synthetic specification dry run |
| Modeled behavior | Strike-1 rejection followed by correction/acceptance assessment, at specification level only |
| Provenance in this PR | Principal-Operator-supplied synthetic dry-run identifier and checksum string |
| Raw test payload/transcript available in this PR | No |
| Checksum independently recomputed in this PR | No |
| Independent re-execution in this PR | No |
| Evidence interpretation | Synthetic specification dry run only; not empirical acceptance evidence or live host/runtime proof |

### Acceptance interpretation

The synthetic dry run illustrates the intended governance contract: defective or insufficiently bound work should be rejected, while corrected work may proceed only after applicable acceptance conditions are met. It does not demonstrate that any of these controls were enforced by a live host/runtime. It must not be cited as production acceptance, independent verification, or post-mutation read-back evidence.

To establish empirical acceptance, execute the tests against the actual host/runtime and preserve the exact fixtures/payloads, expected and observed outputs, event/transcripts, verifier identity/independence evidence, reproducible checksum manifests, and post-mutation read-back. Bind all evidence to the same task and artifact revision.

## 6. Change-impact and maintenance rules

1. A change to a requirement updates its source reference, affected implementation locations, test mapping, and status in this matrix.
2. A change to any of the four Level D binding fields requires updating the Manager and Operator contracts, positive/negative test vectors, and all dependent approval-flow documentation.
3. A material change to a proposal payload invalidates the old checksum, receipt applicability, and approval. Re-propose, re-verify, and re-authorize.
4. Test execution status and independent verification status must be recorded separately.
5. A missing artifact, unavailable platform capability, or unexecuted test is recorded as GAP / NOT PROVEN; it must never be promoted based on narrative confidence or agent consensus.
6. The matrix is a traceability index, not a grant of host permissions, execution authority, or approval to perform consequential actions.

## 7. Issue status and linked remaining work

Issues #32–#37 are **OPEN — BASELINE STAGED**. The merged Kernel v4.0 schemas and this traceability matrix provide a documentation baseline only; their acceptance criteria remain open pending source-reconciliation verification, independent verifier read-back, and automated host/runtime gate testing.

- #52 — Source-reconciliation verification and v3.6-to-v4 coverage.
- #53 — Independent verifier read-back enforcement for consequential repository changes.
- #54 — Automated adversarial Level D runtime gate tests across execution paths.

For Issue #35, [PR #42](https://github.com/adityadhange/project-sentinel/pull/42) is **REFERENCE_PROTOTYPE (UNPROVEN_IN_PROD)**. It exercises a reference-layer task-start gate only; it does not establish host/runtime enforcement, identity authentication, atomic approval consumption, or host permission enforcement. Independent host/runtime proof remains mandatory.

Closing an issue, merging a schema, or merging this matrix update is not evidence that runtime enforcement or empirical acceptance has been achieved.


## 8. Provisional mechanism disposition register — Batch 1 (M-0367–M-0373)

**Record:** [SNT-TO-07 Batch 1 Disposition Record](../.github/audits/SNT-TO-07-batch-1-disposition-record.md)  
**Authority status:** Proposed reconciliation record; not an approved architecture amendment.  
**Verification status:** Source documents were read from the repository and compared at the recorded revision. Independent peer review and formal Sentinel Verifier receipt remain outstanding. No mechanism is marked empirically tested or independently verified by this addendum.

| Mechanism | Disposition | v4.0 source relationship | Traceability state / remaining work |
|---|---|---|---|
| M-0367 — Prompt instruction/context separation | **RESTORE — REFINED** | Researcher §7 treats retrieved content as data and rejects embedded instructions. The original mandatory three-part prompt placement is not explicitly present as a universal v4.0 format. | **PARTIAL.** Preserve the instruction/data authority boundary. Do not reinstate the exact legacy prompt anatomy without a separate need and test. Add an explicit universal invariant only through approved control-plane change. |
| M-0368 — 70/20/10 token allocation | **RESTORE — REFINED** | No explicit adaptive token-budget control or fixed allocation was located in the inspected active v4.0 Manager, Researcher, Verifier, or Operator specifications. | **GAP / NOT PROVEN.** Restore explicit task-sensitive budget planning and protect capacity for evidence and verification. Retire 70/20/10 as a mandatory ratio; define and test any implementation before promotion. |
| M-0369 — Reliability badges and numeric scores | **DEPRECATE** | Researcher §3 uses evidence tiers T1/T2/T3; Verifier §10 uses explicit audit outcomes. Neither establishes calibrated 1–100 reliability scores. | **PROPOSED DEPRECATION.** Retire uncalibrated badges/scores. Preserve evidence tiers and scoped outcome states; do not claim statistical calibration. |
| M-0370 — Bounded retry and diagnostic routing | **MAPPED** | Manager §§6 and 10 define a bounded two-strike correction/arbitration loop; Manager §4 defines specialist routing. | **DOCUMENTED MAPPING.** Do not create a competing retry loop. Executable enforcement and tests remain separate evidence requirements. |
| M-0371 — Last-five-turn memory and no external state | **DEPRECATE** | Manager §§3–4 and §4's state-board requirements use task-pack state, recorded transitions, artifact/receipt references and verified progress. | **DOCUMENTED REPLACEMENT.** Retire fixed five-turn memory and the prohibition on external task state. Conversation history alone is not authoritative state. |
| M-0372 — Retrieve and verify before execution | **MAPPED** | Researcher §2 specifies primary-source routing; Manager §4 requires evidence prerequisites and readiness checks before dispatch; Level D remains separately gated. | **DOCUMENTED MAPPING.** Retrieval, evidence sufficiency, approval and execution remain distinct gates. No claim that every action requires web retrieval. |
| M-0373 — Binary PASS/FAIL output | **MAPPED** | Verifier §10 uses PASS/FAIL/PARTIAL/ARBITRATION_REQUIRED for audit output; §9 uses PASS/FAIL/INDETERMINATE for post-mutation read-back. | **DOCUMENTED MAPPING WITH SCOPE DISTINCTION.** Do not collapse the two outcome vocabularies into one enum. Any unified schema requires separate design and tests. |

### 8.1 Promotion and verification boundary

1. This addendum records dispositions and source comparisons; it does not activate new prompt rules, change role permissions, or authorize consequential actions.
2. M-0367 and M-0368 contain refined restoration proposals. Their new or clarified controls require explicit approved specification text, named tests, and evidence before being marked IMPLEMENTED or TESTED.
3. M-0369 deprecation is a proposed architecture disposition. Do not delete historical source material; retain it in the archive.
4. M-0370, M-0371, M-0372, and M-0373 are mapped at the specification level only. Mapping does not establish runtime enforcement.
5. Independent peer review, source/provenance review of the full SNT-TO-07 scope, and a formal Verifier receipt remain outstanding. Issue #52 therefore remains open.
6. No source archive file, role specification, permission model, or runtime implementation was modified by this batch.
