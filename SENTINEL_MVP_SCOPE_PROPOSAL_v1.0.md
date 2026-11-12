# Project Sentinel — Product-Focused MVP Scope Proposal

**Status: PROPOSED, NOT APPROVED, no implementation authorized**  
**Document:** SENTINEL-MVP-SCOPE-PROPOSAL-v1.0  
**Prepared against `main` HEAD:** `11bb2f8711731dac31ca2996b18ae5c05f0cbc56`  
**Related work item:** [Issue #28](https://github.com/adityadhange/project-sentinel/issues/28)  
**Proposal posture:** Review material only. This document records a drafting direction, not an operator acceptance decision.

> **Authority boundary:** The Principal Operator selected Option A solely as the direction for drafting this proposal. That selection is not approval of this MVP scope, not approval of Python or a CLI, not authorization to implement, and not permission to change runtime permissions, workflows, credentials, governance policies, or production systems. No implementation work is authorized by this document or its pull request.

---

## 1. Purpose and product definition

Project Sentinel's proposed first product release is a small, deterministic, inspectable **governance kernel for managing a task safely from intake through evidence-backed closeout**.

The MVP is not a general-purpose AI chat application, a model-provider wrapper, or an autonomous agent platform. Its primary product value is the reliable management of task identity, dependencies, lifecycle state, authorization boundaries, verification evidence, and handoff. It should remain useful when no AI provider is configured or available.

The MVP should demonstrate a complete, reproducible task-management path while making its own limits visible. It must not imply that a documented policy is enforced by a host, that a reference implementation is a production runtime, or that a producer's report is independent verification.

### 1.1 Product outcome

A Principal Operator should be able to:

1. submit a bounded task request;
2. receive a classified, uniquely identified task record;
3. see a validated dependency graph and package-level state;
4. understand which work is eligible, blocked, failed, or indeterminate;
5. see governance and approval requirements before any consequential operation;
6. inspect candidate outputs and their evidence/verification status; and
7. close out or hand off the task with a revision-bound, auditable record.

The MVP demonstrates task control and evidence discipline. It does not need to execute consequential external actions to demonstrate those controls.

### 1.2 Governing architecture

The proposal preserves the current architecture invariant:

- **Sentinel** is the sole governance kernel and operating substrate.
- **Optimus** is a subordinate orchestration/execution subsystem, not a peer governance authority.
- The **Principal Operator** remains the human authority for decisions reserved to the operator.
- A producing component must not self-certify independent verification.
- A reference module or local application check must not be represented as host-level permission enforcement.

The documented flow is a design constraint, not a claim that every stage is already wired into a runnable application:

`User Request → Sentinel Intake Gate → Optimus Orchestration (where needed) → Sentinel Verification Gate → Sentinel Level D Gate → Authorized Execution`

For this MVP, consequential execution is excluded. The Level D gate may validate and record a proposal/approval state, but it must not execute the consequential action.

---

## 2. Target user, environment, and assumptions

### 2.1 Target user

**Primary target user:** the Principal Operator managing Sentinel tasks and reviewing their status, evidence, approvals, and closeout.

The MVP is not initially scoped for multi-tenant use, public self-service, team administration, or arbitrary external users. Additional user classes require an explicit product decision.

### 2.2 Proposed operating environment

The intended initial environment is a single-operator, locally inspectable development or evaluation environment with:

- a clean repository checkout;
- access to the task workspace and its persisted records;
- a deterministic execution environment;
- a way to inspect inputs, outputs, state transitions, and verification records; and
- no mandatory AI-provider credentials or network service dependency for core task/state operations.

**The concrete runtime, language, packaging format, and user interface are unresolved.** A Python implementation and a command-line interface are candidates for evaluation because existing SNT-010/SNT-011 reference artifacts are Python-based and SNT-010 already exposes a JSON stdin/stdout CLI. Those facts do not decide the production stack. The existing `package.json` is not evidence that Node.js is the required application runtime.

### 2.3 Assumptions to validate

- One Principal Operator is the only human authority represented in the first release.
- A task can be represented by a stable task ID, bounded payload, work packages, dependencies, and explicit state.
- The first release can use local, inspectable persistence if its durability, atomicity, recovery, and path-confinement properties are tested.
- A core workflow can operate without an AI provider. Specialist/model execution may be represented as an assigned work package or an external handoff, not as a mandatory provider integration.
- Verification can be recorded as a distinct step with explicit evidence references and outcomes: PASS, FAIL, or INDETERMINATE.
- Any host-level security, permission, identity, or independent-access guarantee must be proven in the selected environment; a local code check alone cannot establish it.

---

## 3. Scope boundary

### 3.1 In-scope behaviors proposed for the MVP

1. **Task intake and classification:** validate a bounded request envelope and classify it before creating or advancing work.
2. **Task identity and isolation:** assign a unique task ID and keep task data within a task-specific workspace or equivalent isolated namespace.
3. **Dependency compilation:** validate work-package identifiers and edges, reject cycles, identify blocked dependants, and preserve independent acyclic branches.
4. **Lifecycle state:** represent PENDING, READY, IN_PROGRESS, BLOCKED, COMPLETED, FAILED, and CANCELLED at package level, plus task-level REVIEW and closeout states.
5. **Readiness semantics:** READY means dependencies are complete; it does not itself mean authorized or dispatched.
6. **Safe blocked/ambiguous handling:** report missing, contradictory, corrupt, or inaccessible state as UNKNOWN/INDETERMINATE; do not invent progress or silently repair dependency input.
7. **Governance boundary:** identify when an action requires Level D review; validate proposal completeness and task/scope/payload binding as data; do not perform consequential execution.
8. **Evidence and verification records:** associate candidate artifacts with revision identity, evidence references, verifier outcome, defects, and receipt identity.
9. **Closeout and handoff:** produce an inspectable summary of completed work, unresolved work, evidence, risks, and next action.
10. **Deterministic operation:** core intake, dependency, state, and closeout functions must not require a model call.
11. **Auditability:** expose machine-readable state and a human-readable view/report of the same underlying record.
12. **Reproducible validation:** provide documented setup/run/test instructions once the stack is selected, plus tests for normal, negative, and indeterminate outcomes.

### 3.2 Explicit non-goals

The following are outside this MVP proposal:

- Mandatory integrations with Gemini, OpenAI, Anthropic, Perplexity, or other AI providers.
- A model marketplace, model router, multi-provider failover, or provider-specific orchestration as a release dependency.
- A general-purpose chat interface or consumer-facing AI application.
- Autonomous execution of external actions, financial transactions, legal filings, public communications, repository merges, deployments, or other consequential operations.
- Production Level D mutation execution. The MVP may validate and record a proposal/approval state only; it does not execute the action.
- Changes to host permissions, credentials, secrets, workflow permissions, governance policy, or canonical role specifications.
- A claim that local application checks enforce all execution paths or prevent bypass through host tools, APIs, retries, delegation, or alternate entry points.
- Multi-user, multi-tenant, distributed, cloud-hosted, or high-availability deployment.
- A web dashboard, mobile application, browser extension, or polished graphical interface.
- Autonomous agent dispatch or a production Optimus runtime. Assignment/handoff records may be represented, but real dispatch is not a required MVP capability.
- Production concurrency locks or cross-process WIP-1 enforcement unless separately designed and empirically proven.
- Automatic policy interpretation or resolution of unresolved governance questions.
- Data migration, historical archive restructuring, or broad repository cleanup.
- Expanding or replacing `package.json` before the runtime and packaging decisions are made.

---

## 4. Minimum end-to-end workflow

The following is the proposed minimum workflow. Each stage must expose its input, output, state transition, and failure/indeterminate behavior.

### Stage 1 — Intake

- Accept a structured task request containing at least a task payload and, where applicable, work-package definitions.
- Validate required fields, identifiers, duplicate IDs, malformed references, and unsupported request classes.
- Classify the request before orchestration.
- Reject malformed input without creating a misleading active task.
- Record the exact accepted intake payload or a stable revision/checksum identity.

**Output:** validated intake record or explicit rejection/indeterminate result.

### Stage 2 — Task identity and workspace

- Assign or validate a unique `TASK_ID`.
- Establish an isolated task workspace/namespace.
- Record the payload, creation revision, owner/role assignments if known, and initial state.
- Keep task-local artifacts out of global governance/control-plane files.

**Output:** task record and initial state snapshot.

### Stage 3 — Dependency compilation

- Compile the declared work-package graph.
- Reject unknown prerequisite IDs, duplicate IDs, self-loops, malformed edges, and cycles.
- Mark cyclic nodes and downstream dependants BLOCKED.
- Preserve independent acyclic branches as potentially eligible.
- Never silently delete an edge or rewrite a graph to make it pass.

**Output:** validated DAG classification, blocked reasons, and dependency order.

### Stage 4 — Eligibility and governance preflight

- Mark a package READY only when every declared prerequisite is actually COMPLETED.
- Apply scope, role/capability, WIP-1, and governance preflight checks as explicit checks or recorded limitations.
- Keep dependency eligibility distinct from authorization and dispatch.
- For a consequential operation, create a proposal record bound to task, target/scope, and exact payload identity.
- A missing or ambiguous authorization record must not be treated as approval.

**Output:** eligible/blocked work list and, if relevant, a non-executing Level D proposal record.

### Stage 5 — Work execution or handoff

- Record a package as IN_PROGRESS only after the applicable start conditions are satisfied.
- The MVP may support a controlled operator-completed work package or an explicit external handoff record.
- Do not claim that the MVP dispatches an AI agent unless a real dispatch integration is separately implemented and tested.
- Record output artifacts, owner/producer, timestamps where available, and revision identity.
- On failure, record FAILED and block dependent packages while preserving independent branches.

**Output:** work result or explicit blocked/failed/handoff state.

### Stage 6 — Verification

- Bind verification to the exact candidate artifact revision/checksum or equivalent stable revision identity.
- Keep producer and verifier responsibilities distinct.
- Record evidence references and verifier identity/access mode where known.
- Permit only PASS, FAIL, or INDETERMINATE outcomes.
- A missing verifier, inaccessible target, stale receipt, mismatched checksum, or insufficient evidence must not yield PASS.
- A material artifact change invalidates the previous receipt's applicability.

**Output:** revision-bound verification record, defects, and a clear outcome.

### Stage 7 — Review, closeout, and handoff

- When all packages are COMPLETED, move the task to REVIEW, not directly to DONE.
- Require applicable verification and operator acceptance before recording accepted closeout.
- If verification fails, return the affected work for bounded rework and a fresh verification of the revised artifact.
- If evidence is indeterminate, preserve that state and leave the task open/blocked for decision.
- Produce a final handoff containing completed items, unresolved items, evidence, known limitations, decisions required, and the next deterministic action.

**Output:** accepted closeout, rejected/rework state, or explicit INDETERMINATE/awaiting-decision state.

---

## 5. Minimum components and interfaces

The component names below describe responsibilities, not a mandate to create separate services, processes, packages, or personas.

| Component / boundary | Minimum responsibility | Minimum interface / record | Important limitation |
|---|---|---|---|
| Intake validator | Validate request envelope and classification | Structured request → accepted/rejected result | No implicit task creation from invalid input |
| Task identity/workspace manager | Create isolated task identity and locate task records | `TASK_ID`, workspace/namespace, task manifest | Path confinement and durable storage must be proven |
| DAG compiler | Validate dependency graph and classify branches | Work-package dependency map → order, cycles, blocked nodes, reasons | SNT-010 is a reference prototype, not live dispatch |
| Task state manager | Validate transitions and recalculate readiness | State snapshot + transition request → new state or rejection | A local transition check is not host authorization |
| Governance preflight | Identify approval requirements and validate proposal shape/binding | Proposal ID, task ID, target/scope, payload checksum | No Level D execution in MVP |
| Work result/handoff adapter | Record operator/external work result and provenance | Package ID, producer, artifact/revision, outcome | No assumed agent dispatch or provider connectivity |
| Evidence/verification ledger | Bind evidence and verifier outcome to exact artifact revision | Evidence references + revision ID + PASS/FAIL/INDETERMINATE receipt | Independent access/read-back may be UNKNOWN |
| Closeout/report generator | Produce state-consistent summary and next action | Task record → closeout/handoff report | Report must not upgrade unknown evidence |
| Persistence adapter | Save/load task and audit records | Versioned read/write interface | Technology and durability guarantees unresolved |
| User interface | Let operator submit, inspect, and review tasks | CLI or another selected interface | CLI is a candidate, not a decision |

### 5.1 Interface principles

- Prefer explicit, versioned, structured input/output contracts.
- Keep business/state logic separate from the selected presentation interface.
- Make state transitions deterministic and reject invalid transitions with reason codes.
- Preserve raw input and relevant event history; do not rely solely on a rendered summary.
- Make records independently inspectable and exportable.
- Use explicit UNKNOWN/INDETERMINATE values when the system cannot establish a fact.
- Keep provider-specific APIs outside the kernel's required interface.
- Do not expose a successful state transition as proof of authorization unless the authorization boundary is independently established.

---

## 6. Capability evidence baseline

This table is a repository-evidence snapshot at the proposal's stated base commit. It distinguishes documented behavior from reference code and from production enforcement. **Reference code is not production enforcement.** “UNKNOWN” means the inspected evidence does not establish the state; it does not mean the capability is absent.

| Proposed behavior | SPECIFIED | IMPLEMENTED | TESTED | VERIFIED | Evidence / boundary |
|---|---|---|---|---|---|
| Sentinel authority and Principal Operator boundary | YES | UNKNOWN | UNKNOWN | UNKNOWN | Manager v4.0 specification states Sentinel/Optimus hierarchy and operator authority; host enforcement is explicitly not claimed. |
| Request classification and intake contract | YES | PARTIAL | UNKNOWN | NO EVIDENCE | Manager specification defines classes; SNT-011 provides a structured intake reference adapter. No complete production intake path is established. |
| Task identity and isolated workspace | YES | PARTIAL | UNKNOWN | NO EVIDENCE | Manager defines task IDs/workspaces; SNT-011 records task state and caller-supplied persistence path. Host path confinement is not proven. |
| Dependency DAG validation and blocked-branch classification | YES | YES — REFERENCE | UNKNOWN | NO EVIDENCE | SNT-010 contains a deterministic DAG compiler and test source. Test execution evidence was not established in the inspected state. |
| Task/work-package lifecycle and readiness propagation | YES | YES — REFERENCE | UNKNOWN | NO EVIDENCE | SNT-011 contains lifecycle/state reference code and test source. It is not activated in the Sentinel runtime. |
| Persistent task-state save/reload | YES | YES — REFERENCE | UNKNOWN | NO EVIDENCE | SNT-011 describes atomic JSON snapshot save/reload; durable shared storage, path confinement, and cross-process locking are not proven. |
| WIP-1 mutation concurrency control | YES | UNKNOWN | UNKNOWN | NO EVIDENCE | Manager defines WIP-1 as a concurrency control; host-level lock enforcement is not established by the inspected prototypes. |
| Level D proposal schema and approval binding | YES | PARTIAL | UNKNOWN | NO EVIDENCE | Manager defines four binding fields; SNT-011 contains a reference approval check. Host execution-path enforcement is tracked separately. |
| Consequential action execution gate | YES | UNKNOWN | UNKNOWN | NO EVIDENCE | Specification exists; production host enforcement is not established. Excluded from this MVP. |
| Independent verifier access and post-change read-back | YES | UNKNOWN | UNKNOWN | NO EVIDENCE | Contract is specified; #53 tracks independent read-back proof. Actual independent access and reproducible evidence remain unestablished here. |
| Artifact-revision-bound verification receipt | YES | UNKNOWN | UNKNOWN | NO EVIDENCE | Manager specification requires receipt binding; no complete production receipt lifecycle is established by the inspected code. |
| REVIEW and verified closeout | YES | PARTIAL | UNKNOWN | NO EVIDENCE | Manager/SNT-011 define REVIEW distinct from DONE; integrated independent verification and operator acceptance are not proven. |
| AI-provider-independent core workflow | PROPOSED | UNKNOWN | UNKNOWN | NO EVIDENCE | Product requirement proposed here; no provider-free end-to-end kernel release has been demonstrated. |

**Evidence interpretation:** SNT-010/SNT-011 test files being present is evidence that tests were authored, not that the tests were executed successfully. Their current state records do not provide a complete, independently verified test run for this proposed end-to-end MVP. Where the repository evidence inspected does not establish execution, the table says UNKNOWN rather than asserting failure or absence.

---

## 7. Proposed measurable acceptance criteria

These criteria are proposed for operator review. They become binding MVP acceptance criteria only if the Principal Operator approves this scope and the criteria are reconciled with the governing issues and traceability baseline.

| ID | Proposed acceptance criterion | Measurement / pass condition |
|---|---|---|
| **MVP-01** | Valid intake is deterministic and rejects malformed envelopes. | Same valid input yields equivalent normalized task identity/manifest semantics; missing required fields, duplicate IDs, and malformed references return explicit rejection codes without a false active task. |
| **MVP-02** | Each accepted task has a unique identity and isolated task record. | Two accepted tasks have distinct IDs and separately addressable records; task-local artifacts do not overwrite another task or global control-plane records. |
| **MVP-03** | Dependency compilation is correct and fail-closed. | Valid DAGs produce a valid topological order; cycles, self-loops, unknown nodes, and malformed edges are identified; no invalid graph is silently repaired. |
| **MVP-04** | Readiness is dependency-derived, not authorization-derived. | A package becomes READY only when all prerequisites are COMPLETED; READY alone never authorizes a mutating or consequential operation. |
| **MVP-05** | Lifecycle transitions are validated and auditable. | Every allowed transition is recorded with prior state, requested transition, result, and reason; invalid transitions are rejected without partial state mutation. |
| **MVP-06** | Failure and blocked-state propagation preserve independent work. | A failed/blocked prerequisite blocks its dependants; independent acyclic packages remain eligible where their own conditions are met. |
| **MVP-07** | Ambiguous, missing, corrupt, or contradictory state fails closed. | The system emits UNKNOWN/INDETERMINATE with a reason and recovery/inspection action; it does not invent, silently reset, or promote progress. |
| **MVP-08** | Consequential operations cannot be executed by the MVP. | No MVP workflow invokes a consequential external mutation; proposal validation is non-executing and records any missing authorization as not approved/indeterminate. |
| **MVP-09** | Verification is bound to the exact artifact revision. | A receipt identifies the candidate revision; a changed artifact makes the old receipt inapplicable; checksum/revision mismatch cannot produce PASS. |
| **MVP-10** | Verification supports PASS, FAIL, and INDETERMINATE outcomes. | Positive, negative, and unavailable-evidence tests demonstrate all three outcomes; inaccessible verifier/read-back is never represented as PASS. |
| **MVP-11** | Closeout is distinct from package completion and requires the defined review path. | All packages COMPLETED leads to REVIEW; accepted closeout requires applicable verification and operator acceptance; failed/indeterminate review remains visibly unresolved. |
| **MVP-12** | Core kernel operation is reproducible without an AI provider. | A clean environment can intake, compile, track, report, and close out a non-consequential test task with provider credentials/network integrations absent; setup/run/test instructions reproduce the result. |

### 7.1 Acceptance evidence required

For each criterion, the implementation work should provide:

- requirement ID and exact source/proposal revision;
- implementation path or explicit “not implemented” status;
- named automated/manual test and exact command or procedure;
- expected and observed result;
- raw or machine-readable test output;
- environment/runtime details;
- artifact/commit identity;
- independent verifier disposition where required; and
- explicit gaps, including tests not run.

A test passing in a reference module is evidence for that module and test environment only. It is not proof of production activation, host permission enforcement, independent access, or end-to-end operation.

---

## 8. Representative test scenarios

These scenarios define expected behavior, not claims that the tests have already been run.

| ID | Scenario | Setup / stimulus | Expected result |
|---|---|---|---|
| **T01 — Normal completion** | Valid task with a simple acyclic chain. | Intake a task with research → analysis → draft; complete prerequisites in order; attach a candidate artifact; verify and request closeout. | Deterministic intake and DAG; correct READY transitions; package completion moves task to REVIEW; only applicable verification plus operator acceptance permits accepted closeout. |
| **T02 — Blocked dependency** | One prerequisite fails or belongs to a cyclic branch while another branch is independent. | Graph contains A → B → C and independent D → E; fail A or create a cycle in A/B. | Affected dependants are BLOCKED with reasons; independent branch remains eligible; no blocked package is dispatched as ready. |
| **T03 — Ambiguous or corrupt state** | Persisted task state is missing, malformed, contradictory, or unreadable. | Remove/corrupt a required state record or provide contradictory package statuses. | System returns UNKNOWN/INDETERMINATE, identifies the evidence gap, and stops unsafe progression; it does not fabricate a recovered state or silently reset to READY. |
| **T04 — Verification failure** | Candidate artifact does not meet requirements or its evidence is unsupported. | Submit an artifact with a missing required element, unsupported claim, or altered revision after receipt creation. | Verifier records FAIL and defects; old receipt does not apply to changed revision; task returns to bounded rework/reverification rather than accepted closeout. |
| **T05 — Indeterminate evidence / verifier unavailable** | Required evidence or independent verifier read-back cannot be obtained. | Make verifier target inaccessible, withhold required evidence, or simulate read-back failure. | Outcome is INDETERMINATE; no PASS or verified label is emitted; task remains unresolved/blocked pending a defined next action. |
| **T06 — Approval binding / replay attempt** | Approval data is missing, stale, replayed, or bound to a different task, scope, or payload. | Present a proposal/approval record whose task ID, target/scope, or payload identity does not match; replay a previously consumed or stale record in a non-mutating fixture. | Proposal is rejected or marked not authorized; no consequential action occurs; the record identifies the mismatch. This is a reference-level test only until host enforcement is separately proven. |
| **T07 — Provider unavailable** | No AI-provider credentials or service are configured. | Run intake, DAG, state, blocked reporting, evidence registration, and a manually supplied test work result with provider access absent. | Core kernel functions remain usable; provider-dependent work, if any, is explicitly handed off/blocked; no false claim of model execution or completed specialist work is made. |

---

## 9. Reuse map: SNT-010 and SNT-011

The existing task packs are candidates for reuse as bounded reference components. Their code and tests must be reviewed against the final approved interfaces before integration. Their existence does not establish production readiness.

| Existing artifact | Relevant capability | Proposed MVP reuse | Required qualification / work |
|---|---|---|---|
| `Task_Packs/SNT-010/sentinel_dag.py` | Deterministic dependency graph compilation, cycle and blocked-branch classification | Candidate DAG engine behind the dependency compiler interface | Review input/output contract, error semantics, deterministic ordering, complexity bounds, and tests; integrate only after acceptance against MVP-03/MVP-06. |
| `Task_Packs/SNT-010/test_sentinel_dag.py` | Focused DAG test source | Candidate tests/fixtures | Establish actual test execution and retain raw results; add missing edge cases if needed. |
| `Task_Packs/SNT-010/README.md` and `STATE.md` | Usage and non-production boundary | Reference documentation for reuse provenance | Preserve the explicit non-authoritative, not-integrated, not-production boundary; do not treat task-pack status as runtime activation. |
| `Task_Packs/SNT-011/task_runtime.py` | Intake adapter, state transitions, persistence, readiness propagation, approval binding | Candidate state/intake reference implementation | Review full API, persistence guarantees, atomicity, error handling, path confinement, state migration, and approval semantics against approved requirements. |
| `Task_Packs/SNT-011/test_task_runtime.py` | State lifecycle and negative-path test source | Candidate tests/fixtures | Confirm which tests actually execute; add scenario coverage T01–T07; distinguish unit-level results from host/runtime proof. |
| `Task_Packs/SNT-011/README.md` and `STATE.md` | Intake envelope, state semantics, limitations | Reference contract and known-limitations inventory | Reconcile stale statements (including its Manager “working draft” wording) against the live ratified Manager file before treating any text as authoritative. Do not edit these files as part of this proposal. |

### 9.1 Reuse constraints

- Reuse is conditional on review; no code is copied or changed by this proposal.
- The SNT-010 compiler remains the candidate single source of dependency-graph validation if it passes the agreed interface and test criteria.
- SNT-011 is a reference adapter/state manager, not a production runtime.
- Neither task pack proves real agent dispatch, host-enforced permissions, cross-process concurrency, durable shared storage, independent verifier access, or production read-back.
- The proposal does not authorize modifications to either task pack.

---

## 10. Open decisions for Principal Operator review

No item below is decided by this proposal. A choice must be recorded explicitly before implementation planning is finalized.

| Decision ID | Open decision | Candidate / question | Why it matters |
|---|---|---|---|
| **D-01** | Runtime language and packaging | Python is a candidate due to SNT-010/SNT-011; retain Node tooling, use another stack, or define a split? | Determines source layout, build/test commands, dependencies, and packaging. |
| **D-02** | Primary operator interface | CLI is a candidate due to the SNT-010 JSON stdin/stdout interface; alternatively a local API or minimal UI. | Determines interaction model and testability. |
| **D-03** | Persistence mechanism | Local versioned JSON/SQLite/other store; durability and recovery requirements to be selected. | Affects corruption handling, atomicity, portability, locking, and auditability. |
| **D-04** | Task workspace layout | Per-task directory under an agreed root, or another isolated namespace. | Affects path confinement, backup, access, and task isolation. |
| **D-05** | Verification boundary | What can be independently read back in the first release, by which identity and through which access path? | Determines whether a capability can be called VERIFIED or must remain INDETERMINATE. |
| **D-06** | Work execution model | Operator-completed work packages and handoff records only, or a narrowly scoped local executor? | Prevents accidental commitment to agent dispatch or external actions. |
| **D-07** | Authentication and operator identity | What identity assurance is required in a single-operator local MVP? | A local UI or command does not automatically prove Principal Operator identity. |
| **D-08** | WIP-1 enforcement | Reference-level sequencing only, or a separately proven process/host lock? | Avoids claiming cross-session/cross-process safety without enforcement evidence. |
| **D-09** | Evidence/receipt format | Required raw evidence, revision identity, hashes, verifier identity, and storage/retention. | Necessary for reproducible independent verification and audit. |
| **D-10** | Acceptance authority and closeout | Exact operator action required to accept a verified task and record DONE. | Prevents producer/coordinator self-acceptance. |
| **D-11** | MVP distribution | Local source checkout only, packaged local tool, or another distribution model. | Determines install/update and release artifact requirements. |

---

## 11. Risks and mitigations

| Risk | Consequence | Proposed mitigation / release condition |
|---|---|---|
| Reference code is mistaken for a production runtime | False confidence in enforcement or operational readiness | Label every capability by evidence state; require end-to-end tests and independent evidence before promotion. |
| Local checks are mistaken for host security | Alternate execution paths may bypass controls | Exclude consequential execution; map host paths under #35/#54 before any future execution scope. |
| State corruption or partial writes | Incorrect task progress or unsafe readiness | Versioned records, atomic write strategy, corruption tests, recovery policy, and INDETERMINATE on uncertainty. |
| Path escape or workspace collision | Cross-task data exposure or overwrite | Select and test a confined workspace strategy; reject traversal and ambiguous paths. |
| Stale approval or artifact receipt | A prior decision could be misapplied to changed work | Bind records to task, target/scope, payload/revision identity; require fresh review after material change. |
| False verification | Unsupported work is accepted | Independent verifier boundary, explicit evidence, PASS/FAIL/INDETERMINATE, and no producer self-certification. |
| Scope creep into AI integrations | Delays deterministic kernel and introduces provider/network dependencies | Keep provider integrations out of critical path and MVP acceptance. |
| Premature stack selection | Rework and package churn | Resolve D-01/D-02/D-03 before choosing a runtime/package layout; do not expand `package.json` by assumption. |
| Inconsistent governance documentation | Conflicting authority/status interpretations | Reconcile references under #32–#37; preserve unresolved discrepancies as unresolved. |
| Unproven concurrency | Conflicting writes or duplicate mutation drafting | Treat WIP-1 as a documented rule unless host/process enforcement is separately demonstrated. |

---

## 12. Prerequisites and dependency map

The following work items are relevant prerequisites, evidence dependencies, or downstream implementation gates. Their presence in this map does not imply they are complete or approved.

| Issue | Relationship to this proposal | Required treatment before / during implementation |
|---|---|---|
| **#32 — Evidence-backed test-cycle disposition** | Evidence baseline for governance test claims and unresolved outcomes. | Reconcile test inventory, observed results, and evidence gaps; do not promote synthetic specification dry-runs to empirical test evidence. |
| **#33 — Task-bound Level D approval provenance** | Approval record contract and lifecycle. | Resolve task/scope/payload binding, expiry, revocation, replay, and verifier checks. MVP can validate proposal shape without executing Level D actions. |
| **#34 — Independent deliverable acceptance/rework** | Governs producer/verifier separation and review/rework behavior. | Align artifact requirements, defect handling, bounded rework, and independent acceptance semantics. |
| **#35 — Level D enforcement across execution paths** | Establishes whether consequential authorization is enforced by actual execution paths. | Required before any later scope includes consequential execution. MVP excludes such execution and must not claim host enforcement. |
| **#36 — Authoritative architecture source baseline** | Establishes authoritative requirements and resolves source discrepancies. | Preserve unresolved source conflicts; reconcile requirements before treating architecture statements as final implementation requirements. |
| **#37 — Requirements-to-implementation-to-test map** | Traceability baseline for MVP behaviors and acceptance evidence; also a prerequisite named by #66. | Map every accepted MVP requirement to source, implementation, tests, and independent evidence. Do not treat the matrix itself as proof of working code. |
| **#53 — Independent verifier read-back** | Evidence requirement for independent inspection of exact post-change state. | Define verifier identity/access, payload/commit binding, read-back procedure, and fail-closed behavior. Until proven, read-back status is UNKNOWN/INDETERMINATE. |
| **#54 — Adversarial Level D runtime-gate tests** | Host/runtime test evidence for approval enforcement across paths. | Required for any future consequential execution scope; reference-layer tests alone are insufficient. |
| **#66 — Minimum runnable kernel implementation** | Downstream implementation work item. | Remains blocked pending approved #28 scope, #37 traceability, stable #32–#35 contracts, and applicable #53/#54 evidence. This proposal does not start or authorize #66 implementation. |

### 12.1 Dependency sketch

`#32–#35` (governance, evidence, acceptance, authorization contracts)  
`#36 → #37` (authoritative source baseline → canonical traceability)  
`#53 / #54` (independent read-back and adversarial runtime evidence, as applicable)  
`#28` (operator-approved MVP boundary and measurable criteria)  
`#66` (implementation only after the above prerequisites are accepted/stable)

#36 can proceed independently of #32–#35; #37 consumes the reconciled source baseline and outcomes from the governance/test work. The exact sequencing and any conditional applicability of #53/#54 must be confirmed against their own acceptance criteria. The proposal does not resolve those issues on their behalf.

---

## 13. Sequenced implementation plan — conditional on approval

**No step in this section is authorized to begin by this proposal.** This is a recommended sequence to consider only after the Principal Operator records an explicit decision approving the scope and any required changes.

1. **Scope and prerequisite reconciliation**
   - Record the operator's decision on this proposal.
   - Reconcile #32–#37 and identify which contracts are stable enough to implement.
   - Confirm applicable #53/#54 gates and preserve all unresolved questions.

2. **Architecture and stack decision**
   - Resolve D-01 through D-04 and relevant security/interface decisions.
   - Select runtime, language, CLI/API/UI, persistence, workspace layout, and packaging.
   - Record why the selected design is the smallest sufficient implementation.
   - Do not assume Python, CLI, SQLite, JSON, or Node without an explicit decision.

3. **Traceability and executable contract**
   - Convert MVP-01–MVP-12 into a requirements-to-code-to-test matrix under the agreed #37 model.
   - Define versioned request, task, work-package, state, evidence, verification, and closeout schemas.
   - Define exact state transition tables and error/reason codes.

4. **Deterministic core**
   - Review and conditionally adapt SNT-010 DAG compiler.
   - Review and conditionally adapt SNT-011 intake/state reference implementation.
   - Implement task identity, graph validation, lifecycle, readiness, blocked-state propagation, and provider-independent operation.
   - Add deterministic tests for T01–T03 and T07.

5. **Governance and evidence layer**
   - Implement only the approved non-executing proposal-validation boundary.
   - Bind artifacts and verification records to exact revisions.
   - Add FAIL and INDETERMINATE paths, rework, and closeout controls.
   - Add T04–T06 tests using non-mutating fixtures; do not attempt live consequential actions.

6. **Persistence and recovery validation**
   - Validate atomicity, corruption handling, recovery, path confinement, and concurrent access assumptions.
   - If any guarantee cannot be proven in the selected environment, mark it UNKNOWN and constrain the release claim.

7. **End-to-end evaluation**
   - Run all MVP acceptance criteria and T01–T07 from a clean checkout.
   - Preserve raw test outputs, environment details, revision IDs, and failure evidence.
   - Obtain independent verification/read-back where the governing requirements demand it.
   - Do not promote a behavior to VERIFIED or OPERATIONAL based only on successful local unit tests.

8. **Release candidate and operator acceptance**
   - Produce setup/run/test documentation, release limitations, and a capability evidence table.
   - Submit a reviewable release candidate.
   - Obtain explicit Principal Operator acceptance before any operational or production designation.

---

## 14. Known limitations and unresolved facts

At the proposal baseline:

- The repository contains governance specifications and limited reference implementations; it does not establish a complete production Sentinel application/runtime.
- SNT-010 and SNT-011 are reference artifacts, not activated production controls.
- The inspected task-pack test sources do not by themselves establish that tests were executed successfully.
- Host-enforced permissions, production dispatch, independent verifier access, cross-process WIP-1 locking, and end-to-end read-back are not proven by the inspected references.
- The exact production runtime, language, packaging, persistence mechanism, and operator interface remain unresolved.
- The current Manager specification path on `main` is `00_Control_Plane_v4.0/sentinel-manager.md`. A proposed `00_Sentinel_Control_Plane/` active path is not present on the inspected `main` branch.
- The SNT-011 README contains a statement describing the Manager file as a working draft, while the live Manager specification and active control-plane README describe Kernel v4.0 as ratified. This documentation inconsistency should be reconciled; this proposal does not silently resolve it.
- Where a required fact, permission, test result, or independent observation could not be established from inspected repository evidence, it remains UNKNOWN rather than ABSENT.

---

## 15. Principal Operator Decision

**This section is intentionally uncompleted.** No option is preselected. No signature, decision date, or approval is implied by the drafting direction, branch creation, commit, or Draft PR.

- [ ] **Approve** this proposed MVP scope as written.
- [ ] **Approve with changes** — record the required changes and return the proposal for revision.
- [ ] **Reject** this proposed MVP scope.

**Operator decision / required changes:**

_To be completed by the Principal Operator._

**Decision authority:** Principal Operator  
**Signature / confirmation:** _Not supplied_  
**Decision date:** _Not supplied_

---

**End of proposal — PROPOSED, NOT APPROVED, no implementation authorized.**
