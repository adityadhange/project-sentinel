# DOCUMENT CONTROL AND CHANGE MANAGEMENT

**Document ID:** GOV-003  
**Version:** 1.0  
**Status:** RATIFIED — KERNEL v4.0 BASELINE by Principal Operator Aditya Vijay Dhange  
**Document Class:** Ratified Control Procedure

## 1. Purpose

This document establishes the controlled method for identifying, classifying, reviewing, changing, approving, and preserving Project Sentinel documents.

It prevents accidental authority changes, silent overwrites, undocumented decisions, and confusion between repository activity and governance approval. This procedure is active as part of the ratified Kernel v4.0 governance baseline.

## 2. Governing Rules

1. The human operator is the final authority for approving governance, architecture, policy, and release decisions.
2. A document does not become authoritative merely because it exists in GitHub, has a newer version, was created by an AI system, or was committed to the default branch.
3. Repository history records file changes. It does not, by itself, prove that the operator approved the substance of a change.
4. No AI participant may represent a proposal, review, commit, or recommendation as operator approval unless an explicit approval record supports that claim.
5. Conflicts between documents must be identified and referred for determination. They must not be silently reconciled by an AI participant.
6. Until a controlling rule is approved, the relevant matter remains unresolved; this document does not create authority to decide it.

## 3. Document Identity

Each controlled document should carry a metadata block near its beginning containing, where applicable:

- **Document ID:** A stable unique identifier, such as GOV-001.
- **Title:** The document's descriptive title.
- **Version:** The document revision identifier.
- **Status:** Its current approval or lifecycle state.
- **Document Class:** Its governance, architecture, protocol, role, skill, test, register, or other classification.
- **Owner / Responsible Role:** The role responsible for maintaining the document, if assigned and approved.

Document IDs identify documents, not filenames. A filename or folder may change without changing the document ID, but such a change must be recorded. Document IDs must not be reused for unrelated documents.

A document must not claim an owner or approving authority that has not been assigned.

## 4. Document Statuses

The following status labels govern controlled repository documents:

| Status | Meaning |
|---|---|
| RATIFIED | Formally adopted by an explicit Principal Operator ratification disposition; binding within the recorded scope |
| DRAFT — AWAITING OPERATOR APPROVAL | Proposed content not yet approved |
| UNDER REVIEW | Submitted for examination; not approved |
| APPROVED | Explicitly approved by the operator, with a traceable approval record |
| SUPERSEDED | Replaced by a later approved document or version |
| RETIRED | No longer intended for active use, with retirement explicitly approved |
| REJECTED | Considered and not approved |
| ON HOLD | Further work or decision is paused |

Status must reflect an actual recorded decision. AI-generated labels, inferred intent, repository commits, and elapsed time cannot change a document's status.

Where a status is disputed or cannot be established from available records, report it as **STATUS UNCONFIRMED** rather than guessing.

## 5. Versioning

1. Every substantive revision must increment the document's version.
2. A version number is an identifier for a revision; it is not evidence of approval.
3. Minor editorial corrections may be recorded in the change history without implying a policy change, but must not alter meaning, obligations, permissions, evidence requirements, or authority.
4. Any change that affects meaning, scope, responsibilities, controls, permissions, verification, or approval requirements is substantive.
5. The change record must identify the previous and proposed versions and summarize the material differences.
6. Never overwrite historical approval evidence or falsify an earlier version's status.

The versioning scheme may be standardised further after the repository's document inventory and existing conventions have been reviewed.

## 6. Change Proposal Requirements

A proposed substantive change should include:

- Change ID or other traceable reference.
- Affected document IDs, paths, and sections.
- Current wording or rule, where relevant.
- Proposed wording or rule.
- Reason for the change.
- Supporting evidence and source references.
- Known dependencies and documents that may be affected.
- Risks, unresolved questions, and expected consequences.
- Review findings and objections.
- Operator decision and date, once supplied.

A proposal that lacks material information must identify the gaps. Missing evidence must not be replaced with confident wording.

## 7. Review and Approval Workflow

The following workflow applies to substantive controlled-document changes:

1. **Identify:** Record the issue, inconsistency, or requested improvement.
2. **Scope:** Identify affected documents, dependencies, and possible authority conflicts.
3. **Draft:** Prepare the proposed change without silently modifying approved material.
4. **Consistency review:** Use repository-aware tools, including Copilot where available, to identify cross-file contradictions, broken references, duplicate rules, and terminology or version inconsistencies.
5. **Critical review:** Examine the proposal's reasoning, evidence, assumptions, and unintended consequences. Reviewers must distinguish findings from hypotheses and recommendations.
6. **Verification:** Check factual claims, required evidence, applicable tests, and whether the proposed change actually resolves the identified issue. A tool's assertion that a check passed is not, by itself, proof that it did.
7. **Operator decision:** Present the complete proposal, material findings, unresolved conflicts, and limitations to the operator for explicit approval, rejection, or return for revision.
8. **Incorporation:** Only after the required approval may the change be incorporated into an approved document or release.
9. **Read-back:** Retrieve the saved document and compare it with the approved content. Record any mismatch as a failed or incomplete change.
10. **Closure:** Update the relevant change record and affected document metadata only after the result has been checked.

A reviewer's participation does not transfer the operator's approval authority to that reviewer.

## 8. AI and Tool Boundaries

AI systems and repository tools may assist with discovery, drafting, comparison, analysis, and verification within their assigned permissions.

They must not:

- Approve their own proposals or work.
- Infer operator approval from silence, a commit, or a general instruction to continue.
- Silently change approved governance or architecture.
- Delete or rewrite historical evidence to make the current state appear consistent.
- Claim that a repository-wide audit is complete when only selected files were examined.
- Treat Copilot, ChatGPT, another AI system, or a verifier's report as independent proof merely because it is confidently expressed.
- Conceal tool limitations, inaccessible files, failed checks, or unresolved conflicts.

AI-generated findings and suggested corrections remain proposals until reviewed and approved under the applicable process.

## 9. Repository History and Preservation

1. Repository commits and file history should be retained as an audit aid.
2. A commit message should describe the change accurately and should not claim approval unless approval is evidenced.
3. Approved content should not be silently replaced with materially different content.
4. Superseded or retired documents should be preserved or archived with a clear reference to their replacement or retirement decision.
5. Deletion, relocation, renaming, or archival of controlled documents must be treated as a traceable change and must not be used to conceal prior decisions or evidence.
6. During migration, preserve original source material until its disposition has been explicitly determined.

GitHub history is useful evidence of repository activity, but it is not a substitute for a decision record or independent verification.

## 10. Approval Record

An approval record should identify:

- The approving human authority.
- The exact document ID and version or change proposal approved.
- The decision: approved, rejected, or returned for revision.
- The date of the decision.
- Any conditions, exclusions, or limitations.
- The location of the decision record or other traceable evidence.

If any of these details are unavailable, state what is missing. Do not manufacture an approval record retrospectively.

## 11. Relationship to Other Governance Documents

This document is intended to operate consistently with:

- **GOV-001 — SOURCE OF TRUTH:** RATIFIED — KERNEL v4.0 BASELINE; establishes source authority and confirms `GEMINI.md` as the root source-precedence anchor.
- **GOV-002 — AI AUTHORITY AND RESPONSIBILITY FRAMEWORK:** remains DRAFT unless and until separately ratified by the Principal Operator.
- **GOV-003 — DOCUMENT CONTROL AND CHANGE MANAGEMENT:** RATIFIED — KERNEL v4.0 BASELINE by this decision.

GOV-003 operates within the source-precedence hierarchy in `GEMINI.md` and does not override GOV-001 or independently ratify GOV-002. Resolve any conflict using that hierarchy; halt and refer unresolved conflicts to the Principal Operator.

## 12. Ratification and approval record

This document establishes the ratified document-control procedure for the Kernel v4.0 baseline. It does not ratify GOV-002 or any other document not explicitly named in this approval record, declare every repository document approved, claim that host-platform permissions or enforcement exist merely because a document states a rule, authorize autonomous changes outside applicable approval gates, or replace evidence-based verification and explicit operator decisions.

- **Decision:** RATIFIED — KERNEL v4.0 BASELINE.
- **Approving authority:** Principal Operator Aditya Vijay Dhange.
- **Baseline ratification disposition:** The Principal Operator expressly ratified GOV-003 as part of the Kernel v4.0 baseline; this recorded disposition is the source of its RATIFIED status and binding scope.
- **Decision date:** 2026-11-12.
- **Scope:** GOV-003, Version 1.0, including the controlled document lifecycle, review, approval, read-back, and preservation procedure.
- **Traceability:** Explicit Principal Operator instruction issued for the repository remediation on branch `fix/governance-and-ci-reconciliation`; this branch and its resulting pull request preserve the implementation record.
- **Conditions:** GOV-002 remains separately unratified. Host enforcement and actual tool permissions must be evidenced independently.

---

**END OF DOCUMENT GOV-003**
