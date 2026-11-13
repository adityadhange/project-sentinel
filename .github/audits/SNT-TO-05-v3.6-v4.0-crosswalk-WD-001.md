# Sentinel v3.6 → v4.0 Architecture and Requirement Crosswalk

- **Artifact ID:** SNT-TO-05-CROSSWALK-WD-001
- **Status:** WORKING DRAFT — NOT INDEPENDENTLY VERIFIED — NOT APPROVED AS ARCHITECTURE
- **Repository:** `adityadhange/project-sentinel`
- **Baseline branch/commit:** `main` / `10a5a666238e9abd7d8ee12e80f9f425cfbafce7`
- **Prepared:** 2026-11-13
- **Parent workstream:** [#36](https://github.com/adityadhange/project-sentinel/issues/36)
- **Independent verification workstream:** [#52](https://github.com/adityadhange/project-sentinel/issues/52)
- **Integration dependency:** [#37](https://github.com/adityadhange/project-sentinel/issues/37)

## 1. Purpose and evidentiary limits

This artifact records a document-level comparison of the archived Kernel v3.6 source family against the active Kernel v4.0 control-plane baseline. It is an audit working paper, not a ratification, migration approval, or proof of runtime enforcement. The v3.6 material is treated as historical source material because the ratified root source-precedence anchor (`GEMINI.md`, ROOT-GEMINI-001) quarantines `02_Archive_Legacy/` as historical/context-only. No archived requirement is silently promoted to current authority.

The comparison distinguishes: **Preserved** (substantively present in active v4.0 material); **Modified** (present with a material change); **Partial** (some concepts present, but coverage incomplete); **Unmapped** (no explicit active equivalent identified); and **Unproven** (specified but execution/enforcement evidence absent). These are document-analysis classifications only. A row is not independently verified until #52 completes the source/provenance/read-back checks required by that issue.

The source baseline used for this pass includes `GEMINI.md`; GOV-001 `SOURCE_OF_TRUTH.md`; GOV-003 `DOCUMENT_CONTROL_AND_CHANGE_MANAGEMENT.md`; the active `00_Control_Plane_v4.0/` README, traceability matrix and role specifications; and the archived v3.6 DPR, role specifications and M-0367–M-0388 bucket-update material. `AI_AUTHORITY_AND_RESPONSIBILITY.md` is marked DRAFT and is not treated as authoritative. No source file was edited, replaced, moved or deleted in preparing this analysis.

## 2. Architecture and governance crosswalk

| v3.6 requirement / concept | Active v4.0 evidence identified | Working disposition / qualification |
|---|---|---|
| Sentinel as sole governing kernel; Optimus subordinate orchestration | `GEMINI.md`; active Manager specification | **Preserved** in principle. Single-Kernel Monism remains the governing arrangement. |
| Five runtime roles plus offline Co-Developer | Active v4.0 README and role specifications | **Preserved**, with role names/contracts streamlined. |
| Manager as Sentinel intake boundary; project-coordinator subordinate | `sentinel-manager.md` | **Preserved** in substance. |
| Prompt-architect capability represented by Co-Developer | `co-developer.md` | **Preserved/modified** in role placement and scope. |
| Level B task-pack work distinguished from Level D consequential action | `GEMINI.md`, Manager and Operator specifications | **Preserved and formalized**. |
| Human approval required for Level D; no agent self-approval | Manager and Operator specifications | **Preserved and strengthened** through explicit authority boundaries. |
| Approval bound to exact task, scope and payload | Four-field binding: `Proposal_ID`, `Bound_Task_ID`, `Target_Scope`, `Payload_Checksum` | **Strengthened** relative to the simpler v3.6 `APPROVE <ProposalID>` form. |
| Independent Verifier authority and separation from execution | Verifier specification and Manager workflow | **Preserved as specification**; independence in an actual host/runtime remains to be demonstrated. |
| Verifier PASS, receipt, artifact revision/checksum and read-back | Verifier and Manager specifications | **Preserved/formalized as controls**; no automatic inference of live execution. |
| Two-strike defect handling and arbitration | Manager and Verifier specifications | **Preserved** at specification level. |
| R3 scope-split / defer handling | Manager and Verifier specifications | **Preserved** in substance; confirm exact lifecycle and abandonment semantics during detailed verification. |
| Cupboard/Box session-continuity model | Task-pack/state-management provisions | **Partial/unresolved**; no complete one-to-one mapping established in this pass. |

## 3. Evidence and verification crosswalk

| v3.6 requirement / concept | Active v4.0 evidence identified | Working disposition / qualification |
|---|---|---|
| T1 verbatim evidence, T2 source pointer, T3 background context | Researcher evidence-handling provisions | **Preserved** in broad structure. Exact promotion/claim-binding semantics require detailed line-level verification. |
| Primary-source research, source provenance and explicit evidence gaps | Researcher specification | **Preserved**. |
| Untrusted-source handling / prompt-injection quarantine | Researcher and Manager epistemic rules | **Preserved** in principle; exact raw-byte evidence/quarantine-channel mechanics need a separate implementation check. |
| Independent quantitative recalculation | Verifier specification; Manager E2 mandate | **Preserved** as a verifier duty. |
| Citation fidelity, logical support and provenance audit | Verifier specification | **Preserved/expanded**. |
| Full-batch defect reporting | Verifier specification | **Preserved**. |
| Receipt bound to artifact revision/checksum | Verifier and Manager specifications | **Preserved/formalized**. |
| Independent post-mutation read-back | Verifier and Manager specifications | **Preserved as a required control; runtime execution remains unproven**. |
| E0/E1/E2 evidence and enforcement distinctions | v4.0 truth-floor and non-claim rules | **Partial**; not all v3.6 distinctions have a demonstrated one-to-one mapping. |

## 4. Invariant and probe coverage — provisional group-level map

The archived v3.6 DPR summarizes invariant groups; it does not provide a complete individual requirement-by-requirement crosswalk in the source material examined for this pass. The mappings below are therefore provisional and must not be used to certify full coverage.

| v3.6 invariant group / probe family | v4.0 comparison | Working disposition |
|---|---|---|
| INV-001, INV-036 — patch integrity and UTF-8 mutation constraints | No complete individual active-v4 equivalent established | **Unmapped pending line-level source verification**. |
| INV-002, 003, 037, 038 — epistemic certainty, conflict and abstention | v4.0 truth-floor, evidence and uncertainty rules | **Core preserved**, exact invariant mapping incomplete. |
| INV-004, 005, 018, 019, 039 — tool execution and read-back safety | Manager/Verifier execution and read-back requirements | **Partial; host enforcement unproven**. |
| INV-006, 007 — streaming delimiter and truncation handling | No explicit active counterpart identified | **Unmapped**. |
| INV-008, 009, 031, 032 — cache, context and receipt handling | Some continuity, quarantine and receipt provisions | **Partial**. |
| INV-020, 021, 035, 041 — DAG, cycle rejection and state management | Manager intake, DAG and task lifecycle provisions | **Partial; complete invariant mapping absent**. |
| INV-042 — dependency-partitioned parallel dispatch | `GEMINI.md` permits parallel independent reads and controlled mutations | **Preserved in principle**; runtime behaviour not certified. |
| INV-043 — secret-safe execution | No complete requirement-level equivalence established | **Unmapped**. |
| INV-044 — brownfield scope lock | Bounded/surgical correction principles in active workflow | **Partial; exact mapping absent**. |
| INV-045 — explain-versus-execute gate | Manager and root instructions distinguish explanation from mutation | **Preserved**. |
| INV-046 — closed-loop repair | Two-strike correction and arbitration | **Preserved as specification**. |
| PRB-V35-01 — single-turn intake/DAG dispatch | Manager intake and DAG lifecycle | **Partial; runtime test absent**. |
| PRB-V35-02 — two-strike loop | Manager and Verifier specifications | **Specified; execution evidence not established here**. |
| PRB-V35-03 — Level B and E2 execution | Manager and Operator specifications | **Specified; host enforcement not established here**. |

**Caution:** the group labels above are carried from the archived DPR's own summaries. #52 must verify the exact original definitions, identifiers and source locations before treating this table as a canonical mapping.

## 5. Mechanism crosswalk: M-0367 through M-0388

A search of the active v4.0 control-plane documents found no explicit references by identifier to any of M-0367–M-0388. Conceptual overlap is not equivalent to formal migration. The following dispositions are provisional descriptions of apparent overlap, not decisions to retire or retain mechanisms.

| Mechanism | Archived v3.6 concept (short label) | Active v4.0 comparison | Working disposition |
|---|---|---|---|
| M-0367 | Prompt instruction/context separation | No explicit equivalent identified | **Unmapped** |
| M-0368 | 70/20/10 token allocation | No equivalent allocation identified | **Unmapped** |
| M-0369 | Reliability badges and numeric scores | Epistemic tags exist, but not this scoring format | **Modified / not carried forward as-is** |
| M-0370 | Bounded retry and diagnostic routing | Two-strike handling and specialist routing overlap | **Partial** |
| M-0371 | Last-five-turn memory and no external state | Task-pack state/continuity differs materially | **Conflicting / not carried forward as-is** |
| M-0372 | Retrieve and verify before execution | Researcher primary-source and evidence-gap rules overlap | **Partial** |
| M-0373 | Binary PASS/FAIL output | v4.0 also uses PARTIAL and INDETERMINATE | **Modified** |
| M-0374 | Three-state interactive loop | No explicit equivalent identified | **Unmapped** |
| M-0375 | Multipart input buffering | No explicit equivalent identified | **Unmapped** |
| M-0376 | Risk classification | Conditional Critical Analyst activation and Manager routing overlap | **Partial** |
| M-0377 | Three-lines-of-defence model | Independent Verifier and role separation exist; no complete equivalent formal model identified | **Partial** |
| M-0378 | Ex-ante/ex-post security controls | Untrusted-source handling exists; full lifecycle not mapped | **Partial** |
| M-0379 | `<leapArtifact>` patch wrapper | No equivalent identified | **Unmapped** |
| M-0380 | Compressed URI references | No equivalent identified; provenance/locators handled differently | **Not carried forward as-is** |
| M-0381 | Incomplete Assistant-prefix prompting | No equivalent identified | **Not carried forward as-is** |
| M-0382 | Fidelity-score apoptosis | Mechanism evaluation states exist; same threshold/automatic archival rule not identified | **Modified** |
| M-0383 | Fixed five-section prompt anatomy | No universal equivalent identified | **Not carried forward as-is** |
| M-0384 | Model-specific syntax routing | No explicit equivalent identified | **Unmapped** |
| M-0385 | Stripping subjective modifiers | Evidence/testability requirements overlap, but no equivalent rule identified | **Partial** |
| M-0386 | `<think>` XML delimiters | No equivalent identified | **Not carried forward as-is** |
| M-0387 | Bias toward action | Action-oriented routing exists subject to approval gates | **Partial; subordinate to authority controls** |
| M-0388 | One terminal command at a time | No explicit universal equivalent identified | **Unmapped** |

The archive's `active` labels do not establish active v4.0 status. Each mechanism requires an explicit disposition by the authorized decision-maker: retained, modified, rejected, superseded, or unproven. No such disposition is made by this working paper.

## 6. Empirical-kernel discrepancy

The archived v3.6 DPR claims 49 canonical Master Engines, 49 ratified operational invariants, a 23-cluster mechanism organization, and broad probe binding. Archived Co-Developer material also refers to a production promotion standard of approximately 150 failure-free trials.

The active v4.0 Co-Developer specification uses an evidence-led evaluation approach: defined baselines, held-out cases, observable success/failure criteria, reproducible evidence, and `[FIRED]`, `[DEFENDED]`, `[UNPROVEN]` dispositions. It does not certify an empirical kernel or adopt a universal statistical promotion threshold. It treats 3–6 mechanisms as a context-dependent design target rather than a universal quota.

No complete active-v4 inventory was found proving that all 49 engines and all 49 invariants were migrated, tested or independently verified. The archived mechanism index and consolidated parent-mechanism index inspected in this pass state that serialization is pending. Accordingly:

**Disposition:** the 49-engine/49-invariant and 150-trial statements remain historical v3.6 claims. They must not be inherited as established v4.0 empirical facts. This finding does not establish that the mechanisms failed; it establishes that current empirical status is not demonstrated by the active v4.0 source baseline examined here.

## 7. Material authority, provenance and inventory discrepancies

1. **No single active v4.0 DPR identified.** The active baseline is distributed across `GEMINI.md`, ratified governance documents, role specifications and the traceability matrix. A Principal Operator decision is required on whether a consolidated successor DPR is needed.
2. **Conflicting v3.6 DPR path labels.** The same source content appears under a path labelled “Ratified” and another path labelled `[SUPERSEDED_CONTENT]`. Git history and approval provenance—not filenames or byte identity alone—must resolve status.
3. **Archive quarantine.** v3.6 source documents are historical/context-only under the active root precedence rule unless an authorized decision expressly provides otherwise.
4. **49-engine/49-invariant empirical status.** No complete active-v4 crosswalk or test evidence settles these claims.
5. **M-0367–M-0388 disposition.** No active v4 identifier-level migration record was found.
6. **23-cluster guidebook/index.** The mechanism indexes inspected are placeholders indicating serialization is pending; their complete source/provenance status needs verification.
7. **Migration manifest count discrepancy.** The manifest says 31 `Root-Level_Files` artifacts; the current tree count previously observed was 30 tracked entries including `.gitkeep`. Counting conventions may differ; this is not proof of a missing file.
8. **Identical blob groups.** The prior tree audit found 82 identical-blob groups, one consisting of 14 `.gitkeep` placeholders and 81 other groups requiring path/provenance review. Byte identity alone does not authorize deletion or consolidation.
9. **Manager status note.** The migration manifest's note that the active Manager retained DRAFT markers is historical; the current active Manager is labelled RATIFIED. Confirm the approval record if the status itself is material to a decision.

## 8. Decisions and owners required

| Decision / verification item | Responsible authority / workstream | Required outcome |
|---|---|---|
| Confirm source provenance, approval history and duplicate-path status for v3.6 DPR | #52 independent verification; Principal Operator for disposition | Evidence-backed status for each path; preserve originals |
| Decide whether a consolidated active v4.0 DPR is required | Principal Operator | Explicit decision; no implied approval |
| Decide whether the 49-engine/49-invariant claims remain relevant, are retired, or require fresh empirical evaluation | Principal Operator; evidence work through #52 and later #37 | Individual dispositions and evidence standard |
| Decide M-0367–M-0388 retention/modification/retirement | Principal Operator, informed by #52 | Explicit disposition for every mechanism |
| Verify all v3.6 invariant definitions and exact v4 coverage | #52 | Requirement-level matrix with source locators and read-back |
| Resolve manifest 31-vs-30 count and 81 non-placeholder identical-blob groups | #52 | Explain count basis and provenance; no deletion based on hash alone |
| Build canonical requirement → implementation → test traceability | #37, after #52 evidence | Only independently supported rows promoted to verified status |

## 9. Recommended sequence

1. Keep #36 open; attach this working artifact only after its exact payload has been approved through the repository's Level D procedure.
2. Have #52 independently inspect each source artifact, provenance/history, and requirement-level row; independently read back relevant content and hashes.
3. Record each row as VERIFIED, PARTIAL, UNMAPPED, CONFLICTED, or NOT VERIFIABLE with exact source locators and evidence.
4. Send only independently verified mappings to #37 for canonical requirement-to-implementation-to-test traceability.
5. Obtain Principal Operator decisions on architecture/source arrangement and mechanism dispositions before any source rewrite or retirement.

## 10. Explicit non-claims

This artifact does **not** claim that: all v3.6 requirements have been mapped; any runtime control is enforced; any RP-04B or other host test has passed; the 49 engines or invariants are empirically validated; the v3.6 DPR is current authority; any duplicate file is safe to delete; or this working paper has independent Verifier approval.

**Final working disposition:** PARTIALLY RECONCILED — source families and material discrepancy classes identified; complete requirement-level coverage, provenance read-back, empirical status and Principal Operator decisions remain outstanding.
