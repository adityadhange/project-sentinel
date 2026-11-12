# Shared AI Agent Instructions — Project Sentinel

**Status:** RATIFIED  
**Scope:** Ratified repository-wide working guidance for AI agents.

`GEMINI.md` is the repository root authority anchor and defines the active control-plane boundaries and precedence. Living governance policies are located in `01_Governance_Rules/`. These instructions are a proposed continuity aid; they do not amend those sources or grant permissions or authorize execution, policy changes, file deletion, or other consequential actions.

## 1. Establish the repository facts before acting

At the beginning of each session:

1. Confirm the repository is `adityadhange/project-sentinel`.
2. Identify the branch being inspected and its current full commit SHA.
3. Check the current default-branch head and relevant open pull requests in GitHub.
4. Read this file and, if present, `PROJECT_STATE.md` and `HANDOFF_LOG.md`.
5. Compare recorded branch/commit references with live GitHub state. Mark stale, incomplete, or conflicting information; do not silently treat an old snapshot as current.
6. Read [`GEMINI.md`](GEMINI.md) first as the Level 0 root authority anchor, then read the active specifications in [`00_Control_Plane_v4.0/`](00_Control_Plane_v4.0/) before consulting applicable binding policies in [`01_Governance_Rules/`](01_Governance_Rules/).
7. Read the specific source documents needed for the assigned task. Historical archive records are not automatically current instructions or approved policy.

If a referenced state or handoff file does not yet exist, report that fact. Do not invent its contents.

## 2. Preserve operator authority

- The human operator retains final decision-making authority.
- AI analysis, recommendations, drafts, commits, reviews, and merged pull requests must not be represented as operator approval unless an explicit operator decision is recorded.
- A document marked `DRAFT`, `NON-AUTHORITATIVE`, `CANDIDATE`, `UNDER REVIEW`, or similar must not be described as approved or binding policy.
- Do not infer authorization from silence, elapsed time, a commit, a merge, or another agent's recommendation.
- If required authorization is absent or ambiguous, stop at the decision boundary and ask the operator.

## 3. Distinguish claims from evidence

When reporting work, keep these categories separate:

- **Assertion:** what an agent says it did or believes.
- **Repository evidence:** a traceable file path, commit SHA, PR, diff, command result, or other observed record.
- **Verification:** a specific check actually performed, with its scope and result.
- **Operator decision:** an explicit decision made by the human operator, with traceable context where available.
- **Unknown / unverified:** anything not established by the available evidence.

A commit proves that a repository change exists; it does not by itself prove correctness. A merged PR proves that a change was merged; it does not by itself prove independent verification. Never claim a check was performed if it was not.

## 4. Work safely and transparently

- Inspect before changing. Keep changes within the task's authorized scope.
- Do not delete, overwrite, rename, or relocate historical material unless specifically authorized and protected by a reviewable change.
- Prefer small, focused branches and Draft PRs for proposed repository changes.
- Do not merge PRs on the operator's behalf. The operator controls merging.
- Do not change repository settings, permissions, branch protection, secrets, or workflows unless explicitly authorized.
- Report all files changed, including generated or incidental files.
- Preserve unfinished, failed, interrupted, and not-run work in the handoff.
- When two sources conflict, surface the conflict and its evidence; do not silently synthesize a resolution.

## 5. Branch and concurrency discipline

- Treat an unmerged branch as branch-local work, not as the state of `main`.
- Record the starting and ending full commit SHAs for work sessions when available.
- Before updating shared state or handoff records, refresh the target branch and inspect its latest contents.
- If another agent has changed the same files or the base branch has moved, reconcile the changes rather than overwriting them.
- Identify open PRs by number, head branch/SHA, base branch, and observed status.
- Mark snapshots stale when their recorded commit no longer describes the branch state they claim to represent.

## 6. Session closeout

At the end of a substantive session, provide a handoff that records:

- Agent and session date/time (timezone if known).
- Repository, branch, starting SHA, and ending SHA.
- Task and phase.
- Files inspected and files changed.
- Actions actually performed.
- Verification performed, its scope, and evidence.
- Unverified items and limitations.
- Explicit operator decisions received and pending approvals.
- Open PRs, blockers, unfinished work, and failed/not-run actions.
- One exact next recommended action, including any authorization prerequisite.

If `HANDOFF_LOG.md` exists and updating it is authorized, append a factual entry rather than rewriting prior entries. If it does not exist or an update is not authorized, provide the handoff in the session response and state that the repository log was not updated.

## 7. Shared continuity files

When present:

- `PROJECT_STATE.md` is a timestamped snapshot, not a live feed or an independent source of authority.
- `HANDOFF_LOG.md` is a chronological record of session handoffs, not a decision ledger.
- Tool-specific instruction files should point here rather than duplicate or contradict shared guidance.

These files synchronize only information actually recorded in the repository. They do not synchronize private ChatGPT, Claude, Copilot, or other AI conversation histories, and they cannot guarantee that an agent has read or followed them.

## 8. Current approval boundary

This instruction set is RATIFIED working guidance. It remains subordinate to the Level 0 root anchor and does not amend governance policy or grant permissions beyond the recorded operator decision and host capabilities.
