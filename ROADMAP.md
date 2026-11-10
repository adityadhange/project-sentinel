# Project Sentinel — Roadmap and Exclusive Task Register

**Document status:** DRAFT — awaiting Principal Operator review  
**Version:** 1.0  
**Last refreshed:** 2026-11-11  
**Repository:** `adityadhange/project-sentinel`  
**Default branch:** `main`  
**Baseline observed:** `4ffd9172dca5551fb30c7dafde3541d44767167f`  
**Purpose:** One authoritative queue for project work, with one accountable AI owner per active task.

> This roadmap coordinates work; it does not grant repository, workflow, credential, policy, or execution authority. A task assignment is not permission to exceed the task's stated scope. The Principal Operator remains the final authority.

---

## 1. Non-negotiable ownership rule

**One task → one owner → one active workstream.**

When a task is `ACTIVE`, only its named owner may investigate, design, edit, implement, test, or otherwise advance that task.

Every other AI participant must:
- Not start a parallel investigation or implementation of the same task.
- Not edit the task's files or create a competing branch/PR for the same objective.
- Not ask another AI to do part of the task behind the owner's back.
- Not duplicate tests or research already in the task's recorded scope.
- Wait until the task enters `REVIEW`, becomes `BLOCKED`, or the Principal Operator explicitly reassigns it.

**Permitted exception:** A reviewer may independently inspect the completed work after the owner moves the task to `REVIEW`. Review is limited to checking the submitted result against its acceptance criteria. The reviewer must not silently take over implementation. Defects return to the original owner as `REWORK`.

The Principal Operator may override the lock, pause work, or reassign a task at any time.

### 1.1 Claim and lock protocol

A task is not owned merely because an AI was suggested as its owner.

1. The Principal Operator assigns or confirms one AI owner.
2. That AI explicitly accepts by stating `CLAIM: TASK-ID`, its intended scope, and any known blocker.
3. The roadmap is updated to `ACTIVE` with the owner, claim date, and expected deliverable.
4. The lock remains in force until `REVIEW`, `BLOCKED`, `DONE`, `ABANDONED`, or an explicit operator reassignment.
5. On completion or blockage, the owner records the work performed, evidence, remaining work, and a clear handover state.

If an AI cannot continue, it must request a handover. It must not silently leave the task for another AI to discover or continue.

### 1.2 Status definitions

| Status | Meaning | Who may move it |
|---|---|---|
| `BACKLOG` | Known work, not yet prepared for execution | Principal Operator / roadmap maintainer |
| `READY` | Scope and acceptance criteria are clear; awaiting owner claim or start | Principal Operator |
| `ACTIVE` | Exclusively locked to one accepted owner | Principal Operator confirms claim; owner reports progress |
| `BLOCKED` | Owner cannot proceed; blocker and required decision are recorded | Owner reports; Principal Operator confirms disposition |
| `REVIEW` | Owner has completed the task and submitted evidence | Owner |
| `REWORK` | Review found specific defects; original owner resumes | Reviewer recommends; Principal Operator confirms if disputed |
| `DONE` | Acceptance criteria satisfied and evidence recorded | Principal Operator, after review |
| `ABANDONED` | Operator has stopped the task | Principal Operator |

### 1.3 What counts as completion

A task is not `DONE` because an AI says it is finished, a document exists, or a PR was opened or merged.

The owner must provide:
- Deliverable and exact repository paths / PR / commit references, where applicable.
- Acceptance-criteria result, item by item.
- Tests actually run, with results and environment.
- Tests not run, failed, or blocked.
- Evidence that supports each material completion claim.
- Remaining risks, limitations, and follow-up dependencies.

A reviewer checks the evidence. The Principal Operator determines acceptance.

### 1.4 Scope and collaboration boundaries

- An owner may ask the Principal Operator for a decision or missing input.
- An owner may consult documentation and tools within its assigned scope.
- A second AI may not contribute to an `ACTIVE` task unless the Principal Operator explicitly authorizes a named subtask. That subtask must have a distinct ID and non-overlapping scope.
- Independent review is allowed only after `REVIEW`.
- If two tasks have a dependency, the dependent task stays `BACKLOG` or `BLOCKED` until its prerequisite is accepted.
- Do not create a GitHub issue for every small action. This roadmap is the queue; use PRs and existing evidence records for deliverables.

**Enforcement note:** This is a coordination protocol, not a GitHub technical lock. GitHub does not automatically prevent another AI from working in a separate session. Compliance depends on every participant checking this roadmap before acting and the Principal Operator enforcing ownership. No workflow or permission changes are made by this document.

---

## 2. Current repository baseline

Observed immediately before preparing this roadmap:

- `main` head: `4ffd9172dca5551fb30c7dafde3541d44767167f`.
- PR #19 has been merged. It reconciles the Verifier read-back proposal and the MAPCA free-first access addendum, including the Gemini execution workflow's Mode W classification.
- PR #16 remains open and Draft. It adds an Anthropic API-dependent Claude workflow requiring `ANTHROPIC_API_KEY`. This is not required for Claude Free and is inconsistent with the zero-cost default unless explicitly retained as an optional future adapter.
- The current `PROJECT_STATE.md` is stale relative to the November 10 MAPCA / Verifier work and must not be treated as the current work queue.
- Gemini's earlier Plan Only attempts returned HTTP 503 `UNAVAILABLE`. That establishes a service-availability failure for those attempts, not a permanent inability to participate.
- The Verifier read-back proposal is a design proposal, not evidence that read-back tests have been executed or authorized.

These are dated observations. Refresh GitHub before relying on PR or branch state in a later session.

---

## 3. Roadmap and task register

**Important:** The owners below are proposed assignments only. No task becomes `ACTIVE` until the Principal Operator confirms the assignment and the named AI explicitly claims it. No AI is represented as having accepted a task in this initial version.

| ID | Priority | Task | Proposed owner | Status | Depends on |
|---|---|---|---|---|---|
| `SNT-001` | P1 | Reconcile PR #16 with the free-first MAPCA policy; recommend retain-as-optional or close as not pursued. Do not configure a paid API key or incur charges. | ChatGPT | READY | Operator decision on PR disposition |
| `SNT-002` | P1 | Validate the merged Gemini Phase 2 execution gate: inspect exact workflow, build non-production fixtures, test approval freshness, token consumption/replay, allowlist, and Draft-PR-only behavior. Do not use live destructive or out-of-scope operations. | ChatGPT | READY | Test plan and safe fixture scope |
| `SNT-003` | P1 | Turn the Verifier read-back proposal into a fully specified Stage A non-mutating test pack, including target identity, surfaces, expected evidence, and exact pass/fail/indeterminate rules. Do not run active probes. | Manus | READY | Current merged Verifier proposal |
| `SNT-004` | P1 | Conduct Claude Free's first manual MAPCA peer review using a fixed repository snapshot and the common response/provenance format. No API key or paid route. | Claude | READY | Review pack and snapshot SHA |
| `SNT-005` | P2 | Complete an independent Gemini peer review of MAPCA and the merged reconciliation, when the service is available; report 503 or other failure accurately rather than repeatedly retrying. | Gemini | BLOCKED | Gemini service availability |
| `SNT-006` | P2 | Establish the common peer-review reconciliation: compare completed independent reports, preserve dissent, distinguish evidence from inference, and prepare operator decisions. | ChatGPT (proposed) | BACKLOG | SNT-004 and SNT-005 |
| `SNT-007` | P2 | Run the first bounded MAPCA pilot only after peer-review protocol, access modes, and operator gates are accepted. | To be assigned | BACKLOG | SNT-001 through SNT-006 as applicable |
| `SNT-008` | P1 | Conduct Microsoft Copilot’s first manual MAPCA peer review using a fixed repository snapshot and the common response/provenance format. No Copilot Studio, direct GitHub write access, paid API, or repository change. | Microsoft Copilot | READY | Fixed review pack and Principal Operator assignment |

### Task acceptance criteria

**SNT-001 — PR #16 disposition**
- Inspect the actual PR state and diff.
- Compare its API-dependent design with the merged free-first addendum.
- Recommend a clear disposition with costs, prerequisites, and risks.
- Make no PR closure, merge, secret, or workflow change without operator authorization.

**SNT-002 — Gemini execution gate**
- Re-read the exact merged workflow from `main`; do not rely on a prior summary.
- Validate trigger, owner check, one-time approval token, 24-hour freshness, token consumption, strict path allowlist, rejection cases, and Draft PR/no-merge boundary.
- Use static checks and inert fixtures first; report exactly what was and was not exercised.
- Do not test against live production resources or change secrets/settings/permissions.

**SNT-003 — Verifier read-back pack**
- Use the current merged proposal and current repository SHA.
- Fill every test target and evidence field required for a runnable Stage A plan.
- Separate non-mutating inspection from active denial probes.
- Explicitly mark unknown or unavailable evidence as `UNPROVEN`.
- Do not execute active probes or claim permission boundaries have been tested.

**SNT-004 — Claude Free peer review**
- Use a fixed commit SHA and identify every source file reviewed.
- Review independently before reading other AI assessments, where practical.
- Return findings, evidence, disagreements, assumptions, unknowns, confidence, and what would change the assessment.
- Identify the Claude product/access mode accurately; do not imply GitHub independently authenticated the model.

**SNT-005 — Gemini peer review**
- Use the same fixed snapshot and review contract as other peers.
- Preserve independent first-pass findings before cross-challenge.
- Record service errors and unverified claims; do not fabricate a completed review.

**SNT-006 — Reconciliation**
- Compare only completed peer reports.
- Keep each material claim linked to evidence or marked as inference / unverified.
- Preserve minority positions and unresolved disagreements.
- Produce a concise operator decision list, not an AI consensus verdict.

**SNT-007 — Bounded pilot**
- Begin only after the Principal Operator explicitly authorizes the pilot scope.
- Use the free-first access model by default.
- Keep one owner per task and no simultaneous duplicate work.
- Record measurable outcomes, failures, costs (target ₹0 incremental spend), and limitations.

**SNT-008 — Microsoft Copilot Free manual peer review**
- Use Mode M — manual portable review; no Copilot Studio, custom API, paid API, or GitHub connector write capability is required.
- Use a fixed repository snapshot with the repository, branch, full commit SHA, exact files supplied, review question, and known limitations recorded.
- Obtain Microsoft Copilot’s independent first-pass assessment before supplying other peer conclusions, where practical.
- Record findings, evidence links to supplied source paths/sections, disagreements, assumptions, unknowns, limitations, and confidence.
- Label provenance accurately as manually supplied and operator-transcribed; do not claim direct GitHub access, authentication, or posting by Microsoft Copilot.
- Make no repository edits, commits, branches, PRs, settings, permissions, credentials, or paid API calls as part of this task.

---

## 4. Active ownership lock

This table is the live lock register. A task may have only one active owner.

| Task ID | Owner | Status | Claimed at | Scope lock / handover |
|---|---|---|---|---|
| None | — | No task currently claimed | — | All listed tasks await operator assignment and explicit AI claim |

When a task becomes active, replace the `None` row with one row for that task. Do not create multiple active owners for the same task.

---

## 5. Handover record

Every handover must include:

- Task ID and outgoing owner.
- Incoming owner, only after Principal Operator approval.
- Last completed step and exact evidence.
- Files, branches, commits, PRs, test fixtures, and environment involved.
- What remains, what failed, and what must not be repeated.
- Any unresolved operator decision or authorization boundary.
- Confirmation that the outgoing owner has stopped work.

No handover is complete until the incoming owner explicitly accepts the task.

---

## 6. Roadmap maintenance

- This file is the single authoritative task queue and ownership register.
- Update it when a task is claimed, blocked, handed over, submitted for review, accepted, or abandoned.
- Do not rewrite history to make an incomplete task appear complete.
- Record a date and concise change note for each material update.
- Agents must read this file and check the live task lock before starting any project work.
- If the roadmap conflicts with a newer explicit Principal Operator instruction, the operator instruction prevails; update the roadmap to reflect the decision.
- Keep task scopes bounded. Split a task only when necessary, with distinct non-overlapping IDs and dependencies.

### Change log

- **2026-11-11 — v1.0:** Initial roadmap and exclusive task-ownership protocol. Baseline refreshed after PR #19 merge. Proposed assignments are not accepted claims; no task is active.
- **2026-11-11 — v1.1:** Added `SNT-008` for Microsoft Copilot’s zero-cost manual Mode M peer review. The task is `READY`, not active; no owner claim or repository access is implied.
