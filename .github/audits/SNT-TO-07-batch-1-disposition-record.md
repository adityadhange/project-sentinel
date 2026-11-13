# SNT-TO-07 — Batch 1 Mechanism Disposition Record

**Record ID:** SNT-TO-07-B1-DISPOSITIONS  
**Scope:** M-0367 through M-0373 only  
**Status:** PROPOSED RECONCILIATION — source comparison recorded; independent review pending  
**Target repository baseline:** `main` at `26c7d17a60d1cdfc6c0962a491d25b5d879d1f87`  
**Crosswalk:** `.github/audits/SNT-TO-05-v3.6-v4.0-crosswalk-WD-002.md` — Git blob SHA `0cd359fb0e7946f4cb3985d44af3d5d8b41e3480`  
**Legacy mechanism source:** `02_Archive_Legacy/v3.6_transition_source/Kernel v3.6.0 Bucket Updates (M-0367 to M-0388).md` — Git blob SHA `9461f401b5f8c1e1d0a022d48f3b1d14027779a4`

## 1. Purpose and limits

This record captures the seven mechanism dispositions agreed for Batch 1 and compares the archived v3.6 mechanism text with the inspected active v4.0 specifications. It is a scoped reconciliation artifact for Issues #36, #37, and #52.

It does **not** claim that the complete SNT-TO-05 source baseline has been reconciled, that every mechanism in M-0367–M-0388 has been assessed, or that any runtime control has been empirically tested. WD-002 explicitly describes its mechanism comparisons as conceptual and not verifiable at identifier level without further source/provenance work. The seven decisions below are therefore recorded as proposed dispositions with inspectable source locators, not as completed independent verification.

No archived source file was edited, moved, deleted, or rewritten. No active role specification, permission model, or runtime implementation was changed in this batch.

## 2. Source identity and inspected artifacts

All paths below were fetched from the repository at the target baseline above. The SHA values are Git blob SHA-1 identifiers returned for the exact file contents; they are not SHA-256 digests.

| Artifact | Repository path | Git blob SHA |
|---|---|---|
| WD-002 crosswalk | `.github/audits/SNT-TO-05-v3.6-v4.0-crosswalk-WD-002.md` | `0cd359fb0e7946f4cb3985d44af3d5d8b41e3480` |
| v3.6 mechanism definitions | `02_Archive_Legacy/v3.6_transition_source/Kernel v3.6.0 Bucket Updates (M-0367 to M-0388).md` | `9461f401b5f8c1e1d0a022d48f3b1d14027779a4` |
| v4.0 traceability matrix | `00_Control_Plane_v4.0/VERIFICATION_TRACEABILITY_MATRIX.md` | `19b3704b6d66550e1a9efea3e70f971da0ded020` (pre-change) |
| v4.0 Manager | `00_Control_Plane_v4.0/sentinel-manager.md` | `1df1e3319db16e9ac3d8b334b1f0ac149295235a` |
| v4.0 Researcher | `00_Control_Plane_v4.0/researcher.md` | `362f3d3510814a52356ccd587f741224920ac86b` |
| v4.0 Verifier | `00_Control_Plane_v4.0/verifier-officer.md` | `e491208daa1139ac1cfcbedee439443f73ecd08f` |
| v4.0 Operator | `00_Control_Plane_v4.0/operator.md` | `93abee956d543e823553f60ef21f7bcf854d097d` |

The source inspection included the archived definition lines for all seven mechanisms and the active role passages identified in §3. It was a direct repository read and comparison by the implementing assistant, not an independent second-party audit.

## 3. Disposition matrix and source findings

| ID | Archived v3.6 source locator | Disposition | Active v4.0 source locator(s) | Finding and rationale |
|---|---|---|---|---|
| **M-0367** — Prompt instruction/context separation | Legacy mechanism file, line 31 | **RESTORE — REFINED** | Researcher §7, line 111 | The legacy text requires raw context to occupy a middle prompt section and instructions/schema at the beginning/end. The active Researcher already states that retrieved source content is data, not instructions, and rejects embedded commands. That supports the security principle but does not establish the exact three-part prompt anatomy as a universal v4.0 rule. Preserve the instruction/data authority boundary; do not reinstate the exact formatting rule without separate justification and tests. **State: PARTIAL.** |
| **M-0368** — 70/20/10 token allocation | Legacy mechanism file, line 13 | **RESTORE — REFINED** | No explicit active v4.0 token-budget rule located in the inspected Manager, Researcher, Verifier, or Operator specifications. | Explicit task-sensitive token budgeting and a protected evidence/verification reserve are useful. The fixed 70/20/10 ratio is an unvalidated heuristic and should not become a universal invariant. Define the allocation policy and its test criteria before implementation. **State: GAP / NOT PROVEN.** |
| **M-0369** — Reliability badges and numeric scores | Legacy mechanism file, line 23 | **DEPRECATE** | Researcher evidence tiers §3, lines 50–61; Verifier output contract §10, line 122 | The legacy 1–100 reliability score and emoji badges have no demonstrated calibration basis in the inspected v4.0 sources. Evidence tiers and explicit scoped audit outcomes are more defensible. Retire uncalibrated numeric reliability claims; preserve evidence provenance and uncertainty states. **State: PROPOSED DEPRECATION.** |
| **M-0370** — Bounded retry and diagnostic routing | Legacy mechanism file, line 43 | **MAPPED** | Manager §6, lines 40–41; Manager §10, lines 273–278; Manager specialist roster, lines 59–69 | v4.0 has a bounded Strike-1 correction and Strike-2 stop/arbitration process, plus explicit specialist responsibilities and routing. Reuse these controls; do not create a competing retry counter or parallel arbitration path. **State: DOCUMENTED MAPPING.** |
| **M-0371** — Last-five-turn memory and no external state | Legacy mechanism file, line 45 | **DEPRECATE** | Manager task-pack/state requirements, lines 19–20, 93, 153–159, 175 | The legacy fixed five-turn recency window and ban on external state conflict with v4.0's task-bound state board, recorded transitions, artifacts, receipts and workspace persistence. Retire the fixed-turn rule and preserve task-pack state as the authoritative continuity mechanism. Conversation history alone must not establish task state. **State: DOCUMENTED REPLACEMENT.** |
| **M-0372** — Retrieve and verify before execution | Legacy mechanism file, line 15 | **MAPPED** | Researcher §2, lines 16–24; Manager dispatch/readiness gates, lines 135 and 153 | Primary-source routing and evidence prerequisites before specialist dispatch provide the relevant v4.0 coverage. Keep retrieval, evidence sufficiency, approval and execution as distinct gates. Do not overgeneralize this into a requirement to web-search every informational action. **State: DOCUMENTED MAPPING.** |
| **M-0373** — Binary PASS/FAIL output | Legacy mechanism file, line 33 | **MAPPED** | Verifier §9, lines 102–114; Verifier §10, lines 122 onward | v4.0 uses PASS/FAIL/PARTIAL/ARBITRATION_REQUIRED for the audit output contract, while post-mutation read-back separately uses PASS/FAIL/INDETERMINATE. These are scoped vocabularies, not one unified enum. Preserve the richer outcomes and do not collapse them into a binary-only output. **State: DOCUMENTED MAPPING WITH SCOPE DISTINCTION.** |

## 4. Disposition rationale and implementation constraints

### M-0367 — restore the invariant, not obsolete prompt anatomy

The invariant is: **instructions define authority; retrieved, quoted, attached, and otherwise externally supplied content remains data and cannot override governing instructions.** The active Researcher specification supports this for retrieved sources. A universal prompt-layout rule is not evidenced by the inspected active sources and is not restored by this record. If adopted, it requires a separately approved control-plane specification and adversarial tests for prompt injection and instruction/data boundary preservation.

### M-0368 — restore adaptive budgeting, not a fixed ratio

The invariant is: **plan context/token use against task requirements and reserve sufficient capacity for evidence inspection, uncertainty reporting, and verification.** No fixed percentages are adopted. A future implementation must define measurable behavior and tests, including what happens when available context is insufficient. Until then this is a proposed requirement, not an implemented control.

### M-0369 — deprecate false precision

The 1–100 score and colored reliability badges are deprecated as uncalibrated output conventions. This does not prohibit calibrated metrics if a future measurement system defines the target construct, dataset, calibration, validation, uncertainty and failure behavior. No such system was identified in the inspected sources. Historical definitions remain archived.

### M-0370 — reuse the current bounded correction loop

The v4.0 two-strike process already limits correction looping and assigns arbitration to the Verifier. Specialist routing is defined in the Manager's roster and dispatch model. No new retry state machine should be added without evidence of a specific uncovered failure mode.

### M-0371 — use task-bound state, not a fixed conversational window

The task pack and state board carry task identity, transitions, blocked reasons, milestones, artifacts, receipts and next actions. A five-turn window may be useful as conversational context but cannot be the authoritative persistence or continuity mechanism. The prohibition on external state is deprecated.

### M-0372 — retain retrieval and gate separation

The Researcher is read-only and performs primary-source routing. The Manager separately checks evidence prerequisites and readiness before dispatch. Level D actions retain the independent Verifier and Principal Operator authorization gates. Retrieval is not itself authorization, and evidence retrieval must not be conflated with execution permission.

### M-0373 — preserve outcome scope

The audit-result and post-mutation read-back result sets are intentionally different. Audit output includes ARBITRATION_REQUIRED; read-back includes INDETERMINATE. Do not force these into a single status enum without a separately specified state model and compatibility review.

## 5. Traceability promotion rules

| Disposition class | What this record establishes | What remains before promotion |
|---|---|---|
| RESTORE — REFINED (M-0367, M-0368) | A proposed invariant and its source gap/partial coverage are identified. | Approved normative control text, exact scope, implementation location, named positive/negative tests, executed results, and independent verification. |
| DEPRECATE (M-0369, M-0371) | Architectural rationale for retiring the legacy rule is recorded. | Confirm no active references depend on the legacy rule; update downstream references through a separately reviewed change; retain historical source. |
| MAPPED (M-0370, M-0372, M-0373) | Corresponding v4.0 specification passages are identified. | Requirement-level test mapping and proof of implementation/enforcement; verify no uncovered behavior remains. |

No row is marked IMPLEMENTED, TESTED, INDEPENDENTLY VERIFIED, or ACCEPTED by this record. The matrix addendum records the distinction explicitly.

## 6. Verification performed and not performed

### Performed

- Read the exact WD-002 crosswalk and the archived M-0367–M-0373 definitions from the stated repository baseline.
- Read the active v4.0 Manager, Researcher, Verifier, Operator, and Traceability Matrix files.
- Compared the archived mechanism language with the identified active specification passages.
- Recorded Git blob SHA-1 identifiers for source identity.
- Added a provisional mechanism-level addendum to the v4.0 Traceability Matrix on a dedicated branch.
- Preserved the v4.0 matrix's OPEN status and explicit evidence boundaries.

### Not performed / still required

- No SHA-256 was independently computed for these files in this review.
- No separate independent peer or formal Sentinel Verifier reviewed this disposition record.
- No runtime, integration, prompt-injection, token-budget, retry, memory, retrieval, or output-schema tests were executed.
- No host-level enforcement, persistence, permissions, or post-mutation read-back was tested.
- No full-source inventory or full M-0367–M-0388 reconciliation was completed.
- No issues #36, #37, or #52 were closed.
- No active role specification, policy, or runtime implementation was changed.

**Verification disposition: PARTIAL — SOURCE COMPARISON RECORDED; INDEPENDENT VERIFICATION AND IMPLEMENTATION EVIDENCE OUTSTANDING.**

This is not a formal Sentinel Verifier receipt. The implementing reviewer cannot independently certify its own work. A separate reviewer must inspect the exact proposed commit and source artifacts, report any disagreement, and identify the evidence scope before the record can be promoted.

## 7. Required next gates

1. Independent peer review of this record and the matrix addendum at the exact PR head commit.
2. Resolve any source disagreement or missing active control reference.
3. For M-0367 and M-0368, decide whether to authorize a separate implementation specification and test work package.
4. For M-0369 and M-0371, check active references before any downstream removal.
5. For M-0370, M-0372, and M-0373, bind mapped requirements to named tests and distinguish specified from implemented/tested.
6. Continue the remaining SNT-TO-07 scope; this Batch 1 record is not sufficient to close #52 or satisfy the full #36/#37 acceptance criteria.

## 8. Change record

- Branch: `docs/snt-to-07-batch1-dispositions`
- Base: `main` at `26c7d17a60d1cdfc6c0962a491d25b5d879d1f87`
- Change type: documentation-only, proposed reconciliation
- Active role files changed: none
- Legacy source files changed: none
- Runtime code changed: none
