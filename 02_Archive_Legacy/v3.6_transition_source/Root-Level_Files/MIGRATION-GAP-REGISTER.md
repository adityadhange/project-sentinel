# Kernel v4.0 Migration — Reconciliation Gap Register

- Branch: `migration/kernel-v4-reconciliation`
- Baseline: Kernel v4.0 sources dated 07 November 2026
- Purpose: record unresolved source conflicts and validation gaps without inventing policy.
- Snapshot rule: `migration/source-snapshot/` is immutable and was not edited by this migration.

## 1. Completed reconciliation actions

| Item | Action | Result |
|---|---|---|
| System DPR | Replaced the 77-byte placeholder at `01_Sentinel_System_Architecture_DPR.md` with a normalized v4.0 working copy based on the ratified DPR and corroborating v4.0 sources | Completed; source remains in snapshot |
| Sentinel Manager | Reconstructed active role file against v4.0 DPR, registry, directives, and governance contract | Completed as working specification |
| Verifier Officer | Reconstructed independent verification role against v4.0 registry and shared contract | Completed as working specification |
| Researcher | Reconstructed read-only evidence role using v4.0 registry and context-ingestion guide | Completed as working specification |
| Critical Analyst | Reconstructed read-only adversarial role using v4.0 registry and cognitive-logic guide | Completed as working specification |
| Operator | Reconstructed sandboxed assembly role using v4.0 registry, permissions matrix, and shared contract | Completed as working specification |
| Persona registry | Existing active v4.0 registry retained; it already matches the ratified 5+1 roster | Retained |

These are reconciled working copies. They are not a claim that the full kernel or its capabilities have passed empirical tests.

## 2. Source authority and version classification

### Canonical v4.0 source documents

The following files are treated as v4.0 sources because the taxonomy prefix or internal ratification header identifies them as such:

- `ARCH-System_Architecture_DPR (Kernel v4.0).md.md`
- `SKL-Master_Persona_Registry-v4.0.md`
- `SKL-Master_Persona_Registry (Kernel v4.0).md.md`
- `ORG-DIRECTIVES (Kernel v4.0).md.md`
- `ORG-COGNITIVE_LOGIC (Kernel v4.0).md.md`
- `ORG-CONTEXT_INGESTION (Kernel v4.0).md.md`
- `ORG-GUARDRAILS (Kernel v4.0).md.md`
- `ORG-OUTPUT_CONSTRAINTS (Kernel v4.0).md.md`
- `RUL-Capability_Permissions_Matrix (Kernel v4.0).md.md`
- `RUL-Shared_Governance_Contract (Kernel v4.0).md.md`
- `REG-Decisions_Approval_Ledger (Kernel v4.0).md.md`
- `REG-Master_Task_Register (Kernel v4.0).md.md`
- `ARCH-Master_Roadmap (Kernel v4.0).md.md`
- `ARCH-Active_Session_Handover (Kernel v4.0).md.md`
- `ARCH-Improvement_Payload_Workbench (Kernel v4.0).md.md`
- `ARCH-Session_History_Archive (Kernel v4.0).md.md`

User clarification is authoritative for classification: all `ORG-`, `CAP-`, `MTH-`, `RUL-`, `TST-`, and `KNW-` prefixed files are v4.0 source documents. Formatting escapes, filenames, and metadata defects do not downgrade a taxonomy source.

### Historical source material

Several files named as v4.0 role documents internally declare v3.5.0 or v3.6.0. These were used only as historical operational detail where consistent with v4.0 authority. Their filenames do not make their contents v4.0-ratified.

The larger `(1)` copies of some v4.0-named rules/registers also internally declare v3.6.0; retain them as historical evidence, not canonical v4.0 policy.

## 3. Unresolved architectural and governance conflicts

| ID | Conflict / gap | Evidence | Conservative treatment | Required resolution |
|---|---|---|---|---|
| GAP-001 | Manager permissions / classification mismatch | Persona registry: Level A/B/D-Gate. Capability matrix: Level A/B/C/E/F/M triage and E0/E1. | Do not grant additional permissions from the matrix's class list; keep manager at intake, DAG coordination, and gatekeeping. | Define one normative permission model and map action levels to E0/E1/E2 and task classes. |
| GAP-002 | Co-developer identifier mismatch | Registry uses `co-developer`; capability matrix uses `SKL-co-developer`. | Treat `co-developer` as the canonical roster label; offline/advisory only. | Confirm canonical skill ID and update matrix / references consistently. |
| GAP-003 | Authority trace is underspecified | DPR: manager → execution swarm → verifier → Level D gate → mutation. Shared contract says Level D requires proposal, verification PASS receipt, and explicit approval. | Apply the stricter shared-contract gate. | Specify whether verifier PASS is mandatory for every Level D action or only defined action classes; document exceptions, if any. |
| GAP-004 | Capability/test completeness | DPR states each active CAP is test-grounded and bound to a named TST, but the inspected source set does not include complete CAP specifications, TST definitions, execution logs, or acceptance criteria. | Do not mark capabilities empirically validated from declarations alone. | Produce complete CAP-to-TST traceability matrix and independently reproducible test evidence. |
| GAP-005 | Six-category taxonomy completeness | Current inspected canonical set contains ORG guidebook docs and rule/register summaries; full CAP, MTH, TST, and KNW specification bodies were not available in the inspected source set. | Retain every discovered taxonomy file as v4.0; do not fabricate missing documents. | Inventory all taxonomy-prefixed files and recover missing canonical specs from the authoritative archive. |
| GAP-006 | DPR completeness claim vs source depth | DPR header calls itself verified complete, but available body contains only a short executive baseline and a minimal engines/rules section. | This working copy expands only what is corroborated by registry, rules, and guidebook sources; gaps remain explicit. | Obtain full ratified DPR or an independently verified completeness record. |
| GAP-007 | Epistemic tags and evidence ledger | Legacy role documents define four epistemic labels and detailed T1/T2/T3 handling; compact v4.0 ORG docs confirm tiered evidence but not all detailed mechanics. | Preserve the labels and tiers as conservative working conventions, not yet fully validated v4.0 test contracts. | Ratify the exact labels, promotion rules, hash rules, and TST coverage in canonical MTH/RUL/TST specs. |
| GAP-008 | Taxonomy document formatting | Several compact ORG/RUL/REG sources contain backslash-escaped Markdown punctuation. | Normalize only in working copies; never alter source snapshot. | Validate normalized copies against source bytes and publish a formatting-normalization convention. |
| GAP-009 | Legacy duplicate files | Root-level persona duplicates and older co-developer / mechanism placeholders coexist with active subdirectory files. | Do not delete, move, or silently overwrite duplicates in this pass. | Decide canonical path and archive/redirect treatment in a separate approved change. |
| GAP-010 | Registry status vs test status | Registry marks all five runtime personas and offline co-developer ACTIVE, while DPR says CAPs must be test-grounded. | Preserve roster status as declared; do not equate ACTIVE with TESTED PASS. | Separate deployment status from empirical test status in the registry and test ledger. |

## 4. Validation status

| Validation item | Current status |
|---|---|
| Source snapshot immutability | Preserved by migration operations; verify by tree/hash comparison before merge |
| DPR normalization | Reconstructed; semantic review still required |
| Five active role specifications | Reconstructed working copies; semantic review still required |
| 5+1 roster | Source-aligned |
| CAP-to-TST traceability | Not established |
| Test execution / reproducibility | Not established |
| Permission conflict resolution | Open |
| Full taxonomy inventory | Open |
| Root duplicate disposition | Open |
| Merge to `main` | Not authorized by this branch-level approval |

## 5. Explicit non-claims

This migration does not claim:
- that all v4.0 capabilities are implemented or tested;
- that the source's "VERIFIED COMPLETE" labels have been independently reproduced;
- that all permission conflicts have been resolved;
- that every v4.0 taxonomy specification has been recovered;
- that source-snapshot content has been changed;
- that the branch is ready to merge to `main`.

## 6. Next deterministic work

1. Enumerate every taxonomy-prefixed file in the repository and snapshot.
2. Recover and normalize complete `CAP-`, `MTH-`, `TST-`, and `KNW-` specifications where present.
3. Build a CAP → MTH / RUL → TST traceability matrix.
4. Resolve GAP-001 through GAP-003 with explicit policy evidence, not inference.
5. Run independent validation of each active role against the finalized permission matrix and tests.
6. Compare the snapshot tree and hashes before requesting review / merge.
