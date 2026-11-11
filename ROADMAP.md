# Project Sentinel — Roadmap and Exclusive Task Register

**Document status:** ACTIVE — Principal Operator-approved coordination register  
**Version:** 1.5  
**Last refreshed:** 2026-11-11  
**Repository:** `adityadhange/project-sentinel`  
**Default branch:** `main`  
**Baseline observed before this update:** `4ae036bedd342a1527c57de57161c065608104b2`  
**Historical baseline at initial roadmap creation:** `4ffd9172dca5551fb30c7dafde3541d44767167f`  
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

Observed immediately before this roadmap update:

- `main` head: `4ae036bedd342a1527c57de57161c065608104b2`. 
- The initial roadmap baseline `4ffd9172dca5551fb30c7dafde3541d44767167f` is historical; it is not the current repository head.
- PR #19 has been merged. It reconciles the Verifier read-back proposal and the MAPCA free-first access addendum, including the Gemini execution workflow's Mode W classification.
- PR #16 was merged in commit `4ae036bedd342a1527c57de57161c065608104b2`; it adds an Anthropic API-dependent Claude workflow requiring `ANTHROPIC_API_KEY`. This is not required for Claude Free. No secret presence, workflow execution, or paid API use is inferred from the merge.
- The current `PROJECT_STATE.md` is stale relative to the November 10 MAPCA / Verifier work and must not be treated as the current work queue.
- Gemini Plan Only run logs show an initial workspace-trust failure on the first attempt, followed by HTTP 503 `UNAVAILABLE` and HTTP 429 `RESOURCE_EXHAUSTED` on later attempts. The 429 explicitly identifies the free-tier daily quota for `gemini-3.8-flash` (limit 20 requests/day) as exhausted. This is a quota/service-capacity failure, not evidence of a GitHub permission failure.
- Later workflow runs marked `skipped` had no job steps, consistent with the issue-comment filter rejecting comments that did not match the owner-authored `@gemini-cli plan:` trigger. They are not counted as Gemini model failures.
- The Verifier read-back proposal is a design proposal, not evidence that read-back tests have been executed or authorized.

These are dated observations. Refresh GitHub before relying on PR or branch state in a later session.

---

## 3. Roadmap and task register

**Assignment state:** Claude (`SNT-004`) and Microsoft Copilot (`SNT-008`) remain assigned but are on operator hold after both access checks failed. Neither task is active. Gemini recovery is the current P1 workstream; ChatGPT has claimed `SNT-009` under the Principal Operator's instruction.

| ID | Priority | Task | Proposed owner | Status | Depends on |
|---|---|---|---|---|---|
| `SNT-001` | P1 | Reconcile PR #16 with the free-first MAPCA policy; recommend retain-as-optional or close as not pursued. Do not configure a paid API key or incur charges. | ChatGPT | READY | Operator decision on PR disposition |
| `SNT-002` | P1 | Validate the merged Gemini Phase 2 execution gate: inspect exact workflow, build non-production fixtures, test approval freshness, token consumption/replay, allowlist, and Draft-PR-only behavior. Do not use live destructive or out-of-scope operations. | ChatGPT | READY | Test plan and safe fixture scope |
| `SNT-003` | P1 | Turn the Verifier read-back proposal into a fully specified Stage A non-mutating test pack, including target identity, surfaces, expected evidence, and exact pass/fail/indeterminate rules. Do not run active probes. | Manus | READY | Current merged Verifier proposal |
| `SNT-004` | P1 | Claude Free independent challenge and assurance review. | Claude | BLOCKED — OPERATOR HOLD | Operator decision to resume; direct GitHub access unavailable |
| `SNT-005` | P1 | Complete Gemini's independent peer review of MAPCA and the merged reconciliation after the Plan Only integration is restored and a successful live run is observed. | Gemini | BLOCKED | SNT-009; available free-tier quota |
| `SNT-006` | P2 | Establish the common peer-review reconciliation: compare completed independent reports, preserve dissent, distinguish evidence from inference, and prepare operator decisions. | ChatGPT (proposed) | BACKLOG | SNT-004 and SNT-005 |
| `SNT-007` | P2 | Run the first bounded MAPCA pilot only after peer-review protocol, access modes, and operator gates are accepted. | To be assigned | BACKLOG | SNT-001 through SNT-006 as applicable |
| `SNT-008` | P1 | Microsoft Copilot roadmap intelligence and task-coordination recommendations. | Microsoft Copilot | BLOCKED — OPERATOR HOLD | Operator decision to resume; direct GitHub access unavailable |
| `SNT-009` | P1 | Restore reliable, zero-cost Gemini Plan Only operation: pin a free-tier-capable stable model and CLI version, add actionable failure classification, then perform one controlled live test. Do not alter the Phase 2 execution workflow. | ChatGPT | ACTIVE | Current Plan Only run evidence; no paid API or secret changes |



### Confirmed review assignments — operator hold

| Task | Assigned owner | Current status | Fixed review source | Claim requirement |
|---|---|---|---|---|
| `SNT-004` | Claude Free | `BLOCKED — OPERATOR HOLD` | Fixed snapshot `aaf21fd80f706abdbbce686dc854f5af724f02eb` | Resume only on a new operator instruction; no file transfer workaround is planned. |
| `SNT-008` | Microsoft Copilot | `BLOCKED — OPERATOR HOLD` | Same fixed snapshot | Resume only on a new operator instruction; no file transfer workaround is planned. |

Both providers returned `FAILED` for direct private-repository access. Per the Principal Operator's instruction on 2026-11-11, both review tasks are on hold; no download/upload workaround will be pursued. Their assignments and fixed snapshot are preserved for possible resumption.

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

**SNT-004 — Claude Free independent challenge and assurance review**
- Operate in Mode M using the same fixed repository snapshot supplied for SNT-008; no Anthropic API, paid route, Copilot Studio, or direct GitHub write access.
- **Independent first pass:** before Claude is shown Microsoft Copilot's recommendations, review the snapshot, roadmap, governance records, MAPCA documents, and any supplied issue/PR/project-state extracts. Record the exact commit SHA, every source file or extract reviewed, findings, evidence, contradictions, stale references, assumptions, unknowns, confidence, and dissent.
- **Challenge pass:** only after the independent first pass is preserved, provide Claude the SNT-008 recommendations. Ask Claude to assess whether proposed priorities and owners are supported by evidence and challenge scope mismatch, unavailable/blocked providers, duplicated work, missing dependencies, weak acceptance criteria, stale records, and governance/authority conflicts.
- Review whether each proposed task stays within its stated authority and access mode; propose corrections to wording, dependencies, acceptance criteria, and review gates.
- Preserve agreement, disagreement, minority findings, uncertainty, and the evidence or event that would change Claude's view. Recommend whether each proposal is ready for Principal Operator decision; do not issue an approval.
- Treat roadmap, issue, PR, and project-state information not present in the supplied snapshot as unavailable. Do not claim live repository access, direct GitHub authentication, or model-originated posting; label provenance as manually supplied and operator-transcribed.
- Claude does not maintain the roadmap, assign or activate tasks, create ownership locks, override Copilot or the Principal Operator, edit GitHub, create branches, commit, open PRs, or use the Anthropic API.

**SNT-005 — Gemini peer review**
- Use the same fixed snapshot and review contract as other peers.
- Preserve independent first-pass findings before cross-challenge.
- Record service errors and unverified claims; do not fabricate a completed review.

**SNT-009 — Gemini Plan Only recovery (ChatGPT; ACTIVE)**
- Pin the Plan Only workflow to stable `gemini-3.5-flash-lite` (free tier) and the observed Gemini CLI version `0.67.0`; do not introduce paid authentication or change secrets.
- Add a concise issue comment after failed Plan Only runs, classifying HTTP 429 quota exhaustion, HTTP 503 model unavailability, or other failures and linking the run logs.
- Preserve the read-only Plan Only boundary and the existing Phase 2 execution gate; do not modify `.github/workflows/gemini-peer-execute.yml`.
- Perform one controlled live Plan Only test after the Draft PR is merged. A model/quota failure is recorded as BLOCKED, not hidden or retried in a loop.
- Record exact run ID, model/CLI versions, result, and any comment posted. No repository writes by Plan Only are permitted.

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

**SNT-008 — Microsoft Copilot roadmap intelligence and task-coordination recommendations**
- Operate in Mode M — manual portable review; no Copilot Studio, custom API, paid API, or GitHub connector write capability is required.
- Review a fixed repository snapshot and all extracts explicitly supplied for the task. Identify pending work, dependencies, blockers, stale references, duplicated or conflicting tasks, governance contradictions, unfinished work, and suitable AI owners.
- Compare roadmaps, task registers, governance documents, MAPCA records, project-state extracts, and supplied issue/PR records. Do not claim access to GitHub issues, PRs, comments, Actions, or other surfaces unless their contents are included in the supplied pack or independently verified in the actual Copilot environment.
- Draft proposed roadmap entries, task scopes, acceptance criteria, dependency updates, handover notes, decision records, issue/PR descriptions, and exact proposed Markdown content.
- Report recommendations to the Principal Operator with source paths/sections, full snapshot commit SHA, evidence, assumptions, unknowns, limitations, and confidence. Distinguish verified facts, inferences, and recommendations.
- Recommend ChatGPT, Manus, Gemini, Claude, or another participant only when the proposed owner, capability, access mode, and service availability are supported by evidence; mark unavailable providers as blocked or unverified.
- The Principal Operator retains authority to approve, reject, override, delegate, activate, pause, or reassign tasks.
- Microsoft Copilot does not activate tasks, create ownership locks, override the Principal Operator, edit GitHub, create branches, commit, open PRs, change settings, manage credentials, or make paid API calls.
- After operator delegation, ChatGPT, Manus, or Gemini may implement an approved repository update through the normal branch-and-Draft-PR process within the delegated scope.
- Label provenance accurately as manually supplied and operator-transcribed; do not claim direct GitHub access, authentication, or posting by Microsoft Copilot.

**SNT-004 / SNT-008 review sequence and role separation**
1. Prepare one fixed snapshot and record its repository, branch, full commit SHA, included files/extracts, and known omissions.
2. Claude receives the snapshot first and completes its independent first-pass assessment without seeing Copilot's recommendations. Preserve this output before proceeding.
3. Microsoft Copilot receives the same snapshot and produces its SNT-008 roadmap intelligence and owner recommendations.
4. Claude receives the Copilot recommendation and completes the challenge pass. Preserve agreement, disagreement, unsupported assumptions, dissent, and what evidence would change its assessment.
5. The Principal Operator considers both outputs and decides whether to delegate, revise, defer, or reject proposed work.
6. Only the AI explicitly delegated by the Principal Operator may implement the approved change. It must claim the relevant task and respect the exclusive ownership lock.

Role boundary: Microsoft Copilot recommends; Claude independently challenges and assures; the Principal Operator decides and delegates; ChatGPT, Manus, or Gemini implements only the delegated change. These roles confer no automatic repository permissions or execution authority.

---

## 4. Active ownership lock

This table is the live lock register. A task may have only one active owner.

| Task ID | Owner | Status | Claimed at | Scope lock / handover |
|---|---|---|---|---|
| `SNT-009` | ChatGPT | ACTIVE | 2026-11-11 — Principal Operator instruction | Gemini Plan Only recovery only; Phase 2 execution workflow and gate explicitly excluded |

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
- **2026-11-11 — v1.2:** Expanded `SNT-008` to roadmap intelligence and task-coordination recommendations. Microsoft Copilot recommends; the Principal Operator decides and delegates; another AI implements approved repository updates.
- **2026-11-11 — v1.3:** Expanded `SNT-008` to include document comparison, contradiction/stale-reference detection, and drafting support. Expanded `SNT-004` into Claude Free's independent first-pass and subsequent challenge/assurance review. Clarified review sequencing, manual provenance, role boundaries, and the current versus historical repository baseline.
- **2026-11-11 — v1.4:** Confirmed Claude as the assigned owner of `SNT-004` and Microsoft Copilot as the assigned owner of `SNT-008`, both awaiting explicit claims. Added the fixed-snapshot review pack and four source bundles pinned to `aaf21fd80f706abdbbce686dc854f5af724f02eb`. The pack records the missing parent MAPCA v1.0 and external issue/PR limitations. No task is ACTIVE.
- **2026-11-11 — v1.5:** Placed `SNT-004` and `SNT-008` on operator hold after both providers failed direct private-repository access checks. Recorded live Gemini run evidence: after the workspace-trust fix, a Plan Only run first received HTTP 503 and then HTTP 429 with a `gemini-3.8-flash` Free Tier quota limit of 20 requests/day. Google applies quotas per project, so the evidence does not establish that this workflow alone consumed the quota. Added `SNT-009` as the active P1 ChatGPT-owned repair, pinning a free-tier Flash-Lite model and CLI version with explicit failure reporting. PR #16 is now merged; its API-dependent Claude workflow is not the Claude Free route.
