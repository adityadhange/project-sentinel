# Sentinel v3.6 → v4.0 Architecture and Requirement Crosswalk

- **Artifact ID:** SNT-TO-05-CROSSWALK-WD-002
- **Status:** CORRECTED WORKING REVISION — AWAITING INDEPENDENT VERIFICATION — NOT APPROVED AS ARCHITECTURE
- **Repository:** `adityadhange/project-sentinel`
- **Baseline branch/commit:** `main` / `10a5a666238e9abd7d8ee12e80f9f425cfbafce7`
- **Prepared:** 2026-11-13 (revision WD-002; supersedes WD-001 where statements conflict)
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
| INV-043 — secret-safe execution | Active Researcher §9 and Operator §4 require credential redaction; full environment-variable indirection and URI/digest exemption are not located in those active specifications | **PARTIAL** — credential redaction is specified; remaining controls are not established. Specification presence is not host/runtime enforcement. |
| INV-044 — brownfield scope lock | Bounded/surgical correction principles in active workflow | **Partial; exact mapping absent**. |
| INV-045 — explain-versus-execute gate | Manager and root instructions distinguish explanation from mutation | **Preserved**. |
| INV-046 — closed-loop repair | Two-strike correction and arbitration | **Preserved as specification**. |
| PRB-V35-01 — single-turn intake/DAG dispatch | Manager intake and DAG lifecycle | **Partial; runtime test absent**. |
| PRB-V35-02 — two-strike loop | Manager and Verifier specifications | **Specified; execution evidence not established here**. |
| PRB-V35-03 — Level B and E2 execution | Manager and Operator specifications | **Specified; host enforcement not established here**. |

**Caution:** group labels are carried from archived DPR summaries. The 49-invariant arithmetic (46 INV identifiers plus 3 PRB-V35 probes) is coherent as a count only; it does not establish a complete individually defined, source-located 49-row inventory or execution evidence for each probe. INV-043 is PARTIAL, not UNMAPPED. #52 must verify exact definitions, identifiers and locators before treating this as canonical.

## 5. Mechanism crosswalk: M-0367 through M-0388

A search of the active v4.0 control-plane documents found no explicit references by identifier to any of M-0367–M-0388. The archived v4.0 decision ledger records DEC-044 / P053 as a high-level taxonomy transition from Buckets/Mechanisms to ORG-, CAP-, MTH-, RUL-, TST- and KNW-. This establishes a historical high-level migration decision, not an item-by-item disposition or M-to-CAP/MTH mapping. The table below is a provisional comparison only; every row remains NOT VERIFIABLE as an identifier-level migration disposition.

| Mechanism | Archived v3.6 concept (short label) | Active v4.0 comparison | Identifier-level migration status |
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

The archived v3.6 DPR claims 49 canonical Master Engines, 49 ratified operational invariants, a 23-cluster mechanism organization, and broad probe binding. The archived master index bucket counts are 16, 15, 5, 7 and 16, summing to 59 rather than 49. The same table states 49 Master Engines, but its roster section does not enumerate the 49 IDs and points to broader bucket files. The exact 49-member subset cannot currently be independently reconstructed; do not assume the ten-count difference is overlap. Archived Co-Developer material and DEC-029 in the archived decision ledger refer to an approximately 150 failure-free-trial promotion standard.

The active v4.0 Co-Developer specification uses an evidence-led evaluation approach: defined baselines, held-out cases, observable success/failure criteria, reproducible evidence, and `[FIRED]`, `[DEFENDED]`, `[UNPROVEN]` dispositions. It does not certify an empirical kernel or adopt a universal statistical promotion threshold. The 150-trial statement is VERIFIED only as a historical specification/decision claim (including DEC-029), not as evidence that 150 trials were run or passed, or as a universal v4.0 gate. It treats 3–6 mechanisms as a context-dependent design target rather than a universal quota.

No complete active-v4 inventory was found proving that all 49 engines and all 49 invariants were migrated, tested or independently verified. The 49-engine roster is internally unreconciled (49 asserted versus 59 from bucket arithmetic), so exact membership is NOT VERIFIABLE. The 49-invariant total is a coherent count claim only; individual definitions, complete locators and execution evidence remain unestablished. The archived mechanism index and consolidated parent-mechanism index inspected in this pass state that serialization is pending. Accordingly:

**Disposition:** the 49-engine/49-invariant and 150-trial statements remain historical v3.6 claims. They must not be inherited as established v4.0 empirical facts. This finding does not establish that the mechanisms failed; it establishes that current empirical status is not demonstrated by the active v4.0 source baseline examined here.

## 7. Material authority, provenance and inventory discrepancies

1. **No single active v4.0 DPR identified.** The active baseline is distributed across `GEMINI.md`, ratified governance documents, role specifications and the traceability matrix. A Principal Operator decision is required on whether a consolidated successor DPR is needed.
2. **Conflicting v3.6 DPR path labels.** The same source content appears under a path labelled “Ratified” and another path labelled `[SUPERSEDED_CONTENT]`. Git history and approval provenance—not filenames or byte identity alone—must resolve status.
3. **Archive quarantine.** v3.6 source documents are historical/context-only under the active root precedence rule unless an authorized decision expressly provides otherwise.
4. **49-engine/49-invariant empirical status.** No complete active-v4 crosswalk or test evidence settles these claims.
5. **M-0367–M-0388 disposition.** No active v4 identifier-level migration record was found.
6. **23-cluster guidebook/index.** The mechanism indexes inspected are placeholders indicating serialization is pending; their complete source/provenance status needs verification.
7. **Migration manifest and DOCX conversion discrepancy.** The manifest contains 31 Root-Level_Files rows including .gitkeep; the current folder contains 30 tracked entries including .gitkeep. This is unresolved and requires row-by-row reconciliation, not dismissal as a counting convention. The current main tree contains zero DOCX files. Commit f6c64e304ade0a57b3b855237cc35455fe62a7d5 moved 130 DOCX binaries into 99_Legacy_DOCX_Binaries; commit 4b24eea8f4d1c311ce2b3ef88e3b47d114fe629e subsequently removed all 130 from the current tree. Historical Git blobs remain retrievable. Current-branch presence and conversion fidelity are not established: the conversion workflow ran Pandoc then git rm on source DOCX files, but no per-file conversion-run evidence or fidelity manifest is cited. Same-basename DOCX/Markdown pairs require file-level reconciliation.
8. **Identical blob groups.** The audit reports 82 groups: one 14-path .gitkeep group and 81 non-placeholder groups. The aggregate count is reported as reproducible; the 81 non-placeholder groups still require an individual path/provenance/disposition register. Byte identity alone does not authorize deletion or consolidation.
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


## 11. WD-002 correction register and controlling interpretations

This section controls wherever an earlier sentence or table conflicts with the corrected finding.

| Finding | Corrected disposition | Established | Not established |
|---|---|---|---|
| INV-043 secret-safe execution | PARTIAL | Active Researcher §9 and Operator §4 require credential redaction. | Full environment-variable indirection and URI/digest exemption; runtime/host enforcement. |
| 49 Master Engines | CONFLICTED / NOT VERIFIABLE | Archived index lists bucket counts 16 + 15 + 5 + 7 + 16 = 59 while asserting 49. | Exact 49-member roster; whether overlap explains discrepancy. Do not assume overlap. |
| 49 invariants | PARTIAL / NOT VERIFIED AS AN INVENTORY | Count arithmetic 46 INV identifiers + 3 PRB-V35 probes = 49 is coherent. | Complete individually defined 49-row inventory, source locators and execution evidence. |
| 150-trial threshold | VERIFIED AS HISTORICAL CLAIM ONLY | Archived v3.6 Co-Developer and DEC-029 record an approximately 150 failure-free-trial promotion standard. | That 150 trials were executed/passed, or that this is a universal active v4.0 rule. |
| DEC-044 / P053 taxonomy transition | VERIFIED AS HISTORICAL HIGH-LEVEL DECISION CLAIM | Archived decision/task records report transition to ORG/CAP/MTH/RUL/TST/KNW taxonomy. | Per-item M-0367–M-0388 migration, M-to-CAP/MTH crosswalk, completed empirical validation. |
| Root-Level_Files manifest | CONFLICTED / OPEN | Manifest has 31 rows incl. .gitkeep; current folder has 30 tracked entries incl. .gitkeep. | Which row is unmatched and whether conversion/history accounts for it. |
| DOCX conversion | NOT VERIFIABLE | 130 DOCX blobs moved in f6c64e304ade0a57b3b855237cc35455fe62a7d5 and removed from current tree in 4b24eea8f4d1c311ce2b3ef88e3b47d114fe629e; historical blobs remain retrievable. | Per-file conversion execution, fidelity, completeness and same-basename reconciliation. |
| Duplicate blobs | AGGREGATE VERIFIED; PATH-LEVEL OPEN | 82 groups: one 14-path .gitkeep group and 81 non-placeholder groups. | Individual provenance, canonical path or safe disposition for each of 81 groups. |
| M-0367–M-0388 | ITEM-LEVEL NOT VERIFIABLE | Archived bucket source contains 22 IDs; DEC-044/P053 records only high-level taxonomy transition. | Individual retain/modify/retire/supersede decisions and destination IDs. |
| Evidence tiers / credential handling | PARTIAL SPECIFICATION EVIDENCE | Active Researcher defines T1/T2/T3; Researcher and Operator require credential redaction. | Full equivalence to every archived security invariant and host enforcement. |

### 11.1 Added archived source inventory and authority treatment

The following archived records are added to the comparison inventory. Their archive location makes them historical/context-only under GEMINI.md (ROOT-GEMINI-001); self-described RATIFIED, ACTIVE, CANONICAL or VERIFIED COMPLETE labels do not override that authority boundary:

- 02_Archive_Legacy/ARCH-System_Architecture_DPR (Kernel v4.0).md.md — header claims VERIFIED COMPLETE / Ratified Empirical Baseline; body is a short two-section summary and does not substantiate completeness by itself.
- 02_Archive_Legacy/v4.0_01_Sentinel_System_Architecture_DPR.md — normalized working copy; records incomplete CAP-to-TST mapping and absent complete CAP/MTH/TST/KNW specifications.
- Archived v4.0 DEC-044 decision ledger, P053 task-register row, roadmap and improvement-workbench records — historical evidence of a high-level taxonomy transition.
- 02_Archive_Legacy/MIGRATION-GAP-REGISTER.md, GAP-004 through GAP-007 — records CAP-to-TST traceability, full taxonomy inventory, DPR completeness/source-depth and epistemic/evidence-mechanics gaps.
- The normalized DPR references migration/source-snapshot/skills/ARCH-System_Architecture_DPR (Kernel v4.0).md.md as its governing source; that path is absent from current main. This is a provenance gap, not proof that no historical copy exists.

Precise file-line locators for these archive records, DEC-044 and P053 must be captured by the independent reviewer from the actual source files. This revision records the supplied source-audit findings but does not claim those line-level checks have already been performed.

### 11.2 Requirement-level and mechanism-level status discipline

- The v3.6 invariant-group table is a navigation aid only. Every individual invariant and probe requires its exact archived definition, active-v4 source locator, comparison rationale and evidence state.
- M-0367–M-0388 may be described using archived bucket labels, but no row is a verified migration disposition. DEC-044/P053 cannot be used to infer 22 individual mappings.
- For #37, a row may be promoted to VERIFIED only when requirement identity and source are independently read back and implementation and test evidence are separately located. A source specification is not implementation evidence; implementation text is not execution evidence; a test description is not a test result.
- Where evidence is incomplete, retain PARTIAL, UNMAPPED, CONFLICTED or NOT VERIFIABLE. Do not collapse these states into a binary mapped label.

### 11.3 Independent verification receipt — required, not yet issued

A separate reviewer who did not author WD-002 must record:

1. Reviewer identity and confirmation of non-authorship.
2. Exact WD-002 Git commit, path, Git blob SHA, and independently computed SHA-256 of retrieved file bytes.
3. Exact source commit/ref and independently read-back source paths, blob hashes and line locators.
4. Results for each row in the correction register, including arithmetic recomputation of 59 and the 49-invariant count.
5. Per-file findings for manifest/DOCX reconciliation and per-group findings for all 81 non-placeholder duplicate groups, or an explicit statement that those work items remain open.
6. Requirement-level results for each invariant, probe and M-0367–M-0388 identifier, with no unsupported promotion.
7. A scoped overall disposition: VERIFIED, PARTIAL, CONFLICTED or NOT VERIFIABLE, plus defects and unresolved items.

No independent receipt is contained in this revision. A reviewer must not rely solely on the author's narrative or the GitHub API response; they must independently retrieve and hash the exact bytes. A passing review of this document does not itself establish runtime enforcement or architecture approval.

## 12. Downstream consumption contract for #37

Until the independent receipt in §11.3 is recorded against the exact WD-002 revision:

- #37 must not consume WD-002 as a verified baseline.
- #37 may record only that WD-002 is a corrected working crosswalk awaiting independent verification.
- No WD-001 or WD-002 provisional row may be silently promoted to VERIFIED.
- The corrected findings are candidate dispositions, not permission to change active source, policy, skills, registers or runtime.
- #37's canonical map must keep separate columns/states for requirement source, implementation locator, test/probe locator, execution evidence, independent verification receipt and unresolved authority decision.

**WD-002 working disposition:** CORRECTED, SOURCE-AUDIT-INFORMED, NOT INDEPENDENTLY VERIFIED, NOT APPROVED AS ARCHITECTURE. The integration gate to #37 remains CLOSED pending a separate reviewer's revision-bound receipt.
