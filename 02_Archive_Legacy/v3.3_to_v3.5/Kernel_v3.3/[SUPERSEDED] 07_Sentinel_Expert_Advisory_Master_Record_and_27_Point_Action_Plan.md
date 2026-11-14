# Project Sentinel — Expert Advisory Master Record & Complete 27-Point Action Plan

**Date:** 28 October 2026  
**Status:** Authoritative Post-Advisory Synthesis & Implementation Blueprint  
**Objective:** Complete record of external AI systems expert review, architectural blueprints, and prioritized execution roadmap.

## 1\. Executive Grounding & Review Scope

An exhaustive 30-minute + extended architectural audit was conducted with an external AI systems expert on the Project Sentinel DPR, addressing five structural LLM failure modes, multi-agent coordination, epistemic truth floors, evidence handling, and governance hierarchy.

### Topics Dissected:

1. **Adversarial Deadlock Arbitration (Q3):** Eliminating coordinator framing bias and managing loop stalling.
2. **Subtractive Granularity & Evaluation Harnesses (Q1 & Q4):** Empirical calibration of rule density, cluster-bounded prefix compilation, and promotion benchmarking.
3. **Context Compression vs. Verbatim Quote Ledgers (Q2):** Asymmetric tiering, hash-anchored evidence, and claim-driven quote promotion.
4. **\[UNBOUND\_CLAIM\] Detection & Stylistic Prose Isolation:** Grammatical shape checking vs. syntactic sentence classification, operator-side linter decoupling.
5. **Indirect Prompt Injection via Ingested Opposing Evidence (M-0058):** Dual-channel quote architecture, reversible delimiter escaping, and deterministic non-LLM verification.
6. **Corpus Reality Check & The Firing Log Mandate:** Dismantling catalog sprawl, demoting un-fired cards, and defining the true empirical kernel (~30 engines).
7. **Negative Invariant Instrumentation & Pre-Eval Static Pruning:** Three-state firing taxonomy (\[FIRED\], \[DEFENDED\], \[UNPROVEN\]) and pre-benchmark static screening.
8. **Resolution of the Hierarchy Inversion Bug:** Single-Kernel Monism (Sentinel as substrate, Optimus as orchestration subsystem), re-layering the fleet, and returning the epistemic gate to Sentinel authority.

## 2\. Detailed Expert Feedback & Technical Blueprints

### Topic 1: Adversarial Deadlock Arbitration (Q3)

- **Problem Statement:** Coordinator auto-synthesis + presentation order introduces systemic framing bias (defaulting to verifier conservatism). Max-1 loop breaker risks deadlocking the fleet.
- **Architectural Tie-Breaker Protocol:**
  1. **Symmetric Frame (Bias Elimination):** Coordinator strictly forbidden from writing synthesis summaries. Randomized/order-alternating presentation logged for audit trails. Fixed schema: \[CLAIM\], \[EVIDENCE\], \[WHAT\_WOULD\_CHANGE\_MY\_MIND\].
  2. **Pre-Defined Operator Classifications:**
    - (R1) Evidentiary: Verifier wins; back-edge to Researcher.
    - (R2) Strategic-with-Flag: Critical Analyst wins; deliverable marked with visible \[UNVERIFIED\_STRATEGIC\_POSITION\].
    - (R3) Scope-Split: Proceed on verified ground only; defer contested claim to follow-up payload.
  3. **Deterministic Timeout Default:** Default to **R3-halt** (not R1). Epistemically safe without verifier bias.
  4. **Conflict-of-Interest Gate:** Neither specialist may recommend an outcome.

### Topic 2: Subtractive Granularity vs. KV-Cache Stability (Q1 & Q4)

- **Status Calibration:** 3–6 engine rule demoted to working default pending measurement.
- **Architectural Solution:**
  1. **Instrument Before Merging:** Dedicated offline benchmark harness across 23 clusters sampling 10–20 held-out tasks across 3/4/5/6/8 engines (~2,300 batched runs).
  2. **Cluster-Bounded Prefix as Unit:** Make the functional cluster the cacheable prefix segment; cross-cluster links resolve by citation/pointer.
  3. **Falsifiable Pre-Registered Gate:** Pre-register threshold ($X \\ge 95%$ adherence at $Y \\le 60%$ token overhead).
  4. **Staged Technique Promotion Pipeline:** Same cluster harness gates promotion of 1,560 staged techniques.
  5. **Resource Model:** Dedicated offline batch window; never siphon live M-0308 reserves.

### Topic 3: Context Compression vs. Verbatim Quote Ledgers (Q2)

- **Tiered Asymmetric Architecture:**
  - **T1 (Verbatim Audit Floor):** Immutable, full text for directly cited material claims.
  - **T2 (Hash-Anchored Pointer):** \[Q#\] + sha256 + 1-line locator for contextual staging.
  - **T3 (Summary Only):** Background context. Citing T3 in affirmative claims is prohibited.
- **Claim-Driven Promotion Lifecycle:**
  1. Researcher stages all extracted evidence as T2 by default.
  2. Operator binding a claim to \[Q#\] promotes it to T1 in the deliverable envelope.
  3. Verifier audits promoted T1s; triggers \[DEMAND\_READ: Q#\] on demand for T2.
  4. Binary fail on any T1 hash mismatch (M-0324 Stage 1).

### Topic 4: \[UNBOUND\_CLAIM\] Detection without Paralyzing Prose

- **Core Principle:** Classify verifiable propositions by grammatical shape, not whole sentences.
- **Narrow High-Precision Gate:**
  - **Hard-Fail Shapes:** Numbers ($X = N$), dates, statutory sections (§, Clause N), causal/empirical assertions, superlatives/comparatives.
  - **Pass Reasoning Prose:** Connectors, legal transitions, and boilerplate pass cleanly.
  - **Gray Zone Soft Flag:** Factual statements without quotes trigger \[UNBOUND\_CLAIM: REVIEW\].
- **Decoupled Operator Linter:** Deterministic Phase 4 operator-side linter runs before verifier audit.

### Topic 5: Indirect Prompt Injection via Dual-Channel Quotes (M-0058)

- **Core Reframe:** T1 text is data to be reproduced, never data to be interpreted.
- **Dual-Channel Architecture:**
  1. **Evidence Channel:** Raw byte-exact string, used strictly for reproduction and deterministic sha256 matching.
  2. **Quarantine Channel:** Reversibly escaped and wrapped inside inert data structures (<untrusted\_data id=Q#>).
- **Deterministic Verification:** Verifier PASS/FAIL on quote fidelity is a deterministic string/hash comparison, not an LLM reading.
- **Semantic Analysis Quarantine:** Agents reasoning over quote semantics run in read-only, no-tool, no-verdict posture.

### Topic 6: The Corpus Reality Check & The Firing Log Mandate

- **Core Vulnerability Exposed:** 261 active + 1,560 staged is a corpus awaiting proof, not a verified governance kernel. Subtractive refactoring was taxonomical, not empirical.
- **The 4-Part Mandate:**
  1. **Corpus Freeze:** Zero additions until an empirical firing audit is executed.
  2. **Firing Log:** Tag every card with LOAD\_COUNT vs. CAUSAL\_FIRING\_COUNT.
  3. **Demotion to Reference:** Cards with zero observed effect leave the execution path.
  4. **Purge / Hard-Archive:** The 1,560 staged cards must pass the promotion eval harness or be archived.

### Topic 7: Operationalizing the Audit, Negative Constraints & Kernel Sizing

- **Measuring Negative Constraints Without Global Ablation:**
  - *Cheap Proxy:* Violation-rate deltas against known-adversarial red-team probe suites (injection payloads, unbound-claim drafts, phantom writes). If probe fails to breach, log as \[PROBE\_SURVIVED\].
  - *Targeted Offline Ablation:* Run with/without ablation on only the 15–25 high-stakes load-bearing negative invariants in a dedicated batch window.
  - *Honest Firing Taxonomy:*
    - \[FIRED\]: Positive formatters/transforms with diff-proven execution.
    - \[DEFENDED\]: Negative invariants where red-team probes survived without breach.
    - \[UNPROVEN\]: Cards that have never faced an empirical test case.
- **Pre-Benchmark Static Triage (Pruning Before 2,300 Eval Runs):**
  - Screen 1: *Does it specify an observable state change or falsifiable check?* (file ops, token classes, hashes, tags, gates, numeric predicates). If merely aspirational ("be careful / prioritize rigor") → demote to documentation immediately.
  - Screen 2: *Is it referenced by any deployed runtime skill contract?* If unreferenced → archive immediately without wasting eval runs.
- **Target Kernel Metric vs. Corpus Metric:**
  - Production multi-agent systems typically require only **15 to 40 provable canonical engines**.
  - **Working Target:** **~30 provable canonical engines** supported by a secondary documented variant layer.
  - *Governing Principle:* "Every active card must have a named test or a named probe." Optimize for test coverage, not catalog count.

### Topic 8: The Hierarchy Inversion Bug & Single-Kernel Monism

- **Core Structural Flaw Identified:** Framing Sentinel and Optimus as "co-equal engines" created a hierarchy inversion where the orchestration subsystem (incentivized for throughput and completion) could override the governance kernel (abstention and safety). The governed party cannot contain its own governor.
- **The Architectural Correction (Single-Kernel Monism):**
  1. **One System, One Kernel:** Project Sentinel is the sole system, containing substrate, governance, and execution plane. Optimus is demoted to a named orchestration subsystem residing inside Sentinel's execution plane.
  2. **Re-Layered Fleet Topology:** sentinel-manager is the intake gate into the kernel sitting above Optimus. Optimus coordinates task execution. verifier-officer is an independent Sentinel epistemic authority called by the workflow. The 5 Drive registers are Sentinel's control plane.
  3. **Retirement of Co-Equal Language:** Purge all "dual-engine" and peer terminology.
  4. **The End-to-End Tracing Invariant Test:** Request $\\rightarrow$ Sentinel Intake Gate $\\rightarrow$ Optimus Orchestration $\\rightarrow$ Sentinel Verification Gate $\\rightarrow$ Sentinel Level D Gate $\\rightarrow$ Execution.

## 3\. The Complete 27-Point Action Plan (Implementation Register)

### Phase 1: Architectural Hierarchy & Single-Kernel Monism (Immediate Priority)

1. **Retire "Dual-Engine / Peer" Architecture:** Eliminate all framing of Sentinel and Optimus as co-equal engines across the DPR, system prompts, and registers. Establish Single-Kernel Monism: Project Sentinel is the sole system, containing substrate, governance, and control plane. Optimus is subordinated as a named orchestration subsystem within Sentinel's execution plane.
2. **Re-Layer Fleet Authority Boundaries:**
  - sentinel-manager: Position as Sentinel’s external intake boundary sitting above Optimus (intake, classification, and Level D gatekeeper).
  - Optimus Execution Plane: Subordinate project-coordinator, prompt-architect, researcher, critical-analyst, and operator as task-execution roles.
  - verifier-officer: Establish as an independent Sentinel-owned authority (governor of M-0015) called by Optimus workflows, answering strictly to Sentinel.
3. **Control Plane Governance Transfer:** Formally designate the 5 Drive registers as Sentinel’s persistent control plane, administered on Sentinel's behalf by Optimus.
4. **End-to-End Authority Tracing Invariant:** Enforce that every task traces: User Request $\\rightarrow$ Sentinel Intake Boundary $\\rightarrow$ Optimus Execution Plane $\\rightarrow$ Sentinel Verification Authority $\\rightarrow$ Sentinel Level D Gate $\\rightarrow$ Mutation, ensuring execution never escapes Sentinel authority.

### Phase 2: Evidence Integrity, Quote Tiering & Anti-Tampering

1. **Codify M-0341: "Evidence Control Is Not a Drafting Privilege":** Formalize that evidentiary promotion, classification, and scope splitting are governed by deterministic rules rather than the drafting agent's discretion.
2. **Deploy Three-Tier Asymmetric Evidence Ledger:**
  - Tier 1 (T1 — Verbatim Audit Floor): Immutable, full-text quotes directly supporting affirmative material claims.
  - Tier 2 (T2 — Hash-Anchored Pointer): Contextual quotes carrying \[Q#\] + sha256 + 1-line locator.
  - Tier 3 (T3 — Summary Only): Background/extraneous material. Strictly prohibited from supporting claims.
3. **Implement Claim-Driven Promotion Lifecycle:** researcher stages all extracted evidence as T2 by default during ingestion. When operator binds a claim to a \[Q#\], it is automatically promoted to T1 in the deliverable envelope. verifier-officer audits promoted T1s and issues \[DEMAND\_READ: Q#\] only when inspecting background T2 context.
4. **Dual-Channel Evidence Pipeline (Anti-Injection Quarantine):**
  - Evidence Channel: Raw, byte-exact, hash-locked string used strictly for reproduction into the final deliverable and sha256 verification. Never exposed as instructions in reasoning prompts.
  - Quarantine Channel: Reversibly escaped and wrapped inside <untrusted\_data id=Q#> structures for agents to inspect as inert data.
5. **Deterministic Verifier Hash Gate:** Convert quote verification in verifier-officer from an LLM interpretation check to a deterministic code/string/hash comparison, making prompt injection structurally incapable of forcing an unearned PASS.
6. **Semantic Analysis Quarantine:** Any agent analyzing opposing evidence (e.g., critical-analyst probing an adversary's brief) operates in a strictly read-only, no-tool, no-verdict posture.
7. **Narrow High-Precision \[UNBOUND\_CLAIM\] Detection:** Classify propositions by grammatical shape rather than arbitrary sentence classification. Hard-fail shapes: Numbers ($X=N$, units, percentages, dates), statutory citations (§, Section N, Clause N), causal assertions ("caused", "fails to"), and comparatives/superlatives ("only", "exceeds"). Connectors, transitions, and boilerplate pass freely. Gray zone triggers soft flag \[UNBOUND\_CLAIM: REVIEW\].
8. **Decoupled Operator-Side Pre-Audit Linter:** Deploy a deterministic shape linter in Phase 4 (operator) executing via tool-assisted regex (screening for un-cited digits, §, percentages, and comparative markers lacking adjacent \[Q#\] tags) rather than autoregressive self-grading, resolving unbound claims before the verifier gate.
9. **Demand-Read Budget Caps:** Cap \[DEMAND\_READ: Q#\] requests at N = 3 individual reads per audit cycle; any subsequent verification demands strictly require a single batched manifest (\[DEMAND\_READ: Q1, Q4, Q8\]) to prevent context-window exhaustion loops.
10. **Scope-Split Reunion Links & Expiration Lifecycle:** Mandate that deferred payloads carry \[DEFERRED\_LINK: <parent\_task\_id>\] and parent deliverables carry a visible \[SCOPE\_SPLIT\_PENDING\] tag. Add an auto-termination lifecycle: any deferred claim not promoted into an active task within 14 calendar days or 3 subsequent sessions automatically transitions to \[SCOPE\_SPLIT\_ABANDONED\], clearing the parent deliverable for permanent sign-off.

### Phase 3: Symmetric Deadlock Arbitration Protocol (Q3 Resolution)

1. **Prohibit Coordinator Synthesis Summaries:** The coordinator is strictly forbidden from writing synthesis or arbitration summaries when presenting conflicts to the human operator.
2. **Symmetric, Order-Alternating Escalation Template:** Enforce identical word budgets and a rigid schema for both agents: \[CLAIM\], \[EVIDENCE\], \[WHAT\_WOULD\_CHANGE\_MY\_MIND\]. Randomize/alternate presentation order per conflict and log it for auditability.
3. **Standardized 3-Option Operator Decision Rubric:**

- (R1) Evidentiary: Verifier wins; back-edge to Researcher to obtain missing source.
- (R2) Strategic-with-Flag: Critical Analyst wins; deliverable marked with \[UNVERIFIED\_STRATEGIC\_POSITION\] (hard-blocked from filing until removed).
- (R3) Scope-Split: Proceed on verified grounds only; defer contested claim to follow-up payload.

1. **Synchronous Next-Turn Interrupt Default:** Prohibit idle wall-clock timer dependencies. If an unresolved symmetric arbitration envelope is active in the state board and the operator submits any subsequent directive without selecting R1, R2, or R3, the system automatically applies **(R3: Scope-Split)** at the next turn to prevent pipeline stall, archives the contested claim, and proceeds with the verified baseline.
2. **Conflict-of-Interest Penalty Gate:** Neither specialist agent may recommend an outcome (R1/R2/R3); doing so triggers an invariant violation penalty.

### Phase 4: Corpus Pruning, Firing Logs & Empirical Kernel Calibration

1. **Corpus Freeze:** Freeze the canonical index at M-0340. Prohibit adding new active or staged mechanism cards until the empirical audit is complete.
2. **Pre-Benchmark Static Triage (Pruning before evals):**

- Screen 1 (Observable State Change): Demote any card lacking an observable state change, token class, hash, tag, or numeric predicate to reference documentation (removes aspirational prose).
- Screen 2 (Skill Reference Audit): Demote or archive any card not referenced by an active skill contract.

1. **Instrument Three-State Firing Log:** Tag every mechanism card with runtime metrics:

- \[FIRED\]: Positive formatters/transforms with diff-proven execution.
- \[DEFENDED\]: Negative invariants where known-adversarial red-team probes survived without breach.
- \[UNPROVEN\]: Cards that have never faced an empirical test case.

1. **Targeted Offline Invariant Ablation:** Schedule a dedicated offline batch window to run with/without ablations on the 15–25 high-stakes load-bearing negative invariants using free-tier headless Python batch scripts (via Google AI Studio API / Colab) logging directly to a Google Sheets evaluation ledger, strictly preserving the $0 incremental budget ceiling.
2. **Transition to Cluster-Bounded Prefix Units:** Shift compilation units from arbitrary engine counts (3–6) to functional cluster prefix segments. Cross-cluster dependencies resolve by citation/pointer rather than text expansion, maximizing KV-cache reuse while preserving provenance.
3. **2-Tier Prompt Architecture & Cluster Units:** Structure compiled prompts into two layers: (1) an immutable, byte-identical ~1,500-token Universal Frozen Substrate shared across all 7 skills for maximum KV-cache hits, followed by (2) the Modular Functional Cluster Prefix. Cross-cluster dependencies resolve by pointer reference.
4. **Pre-Register Falsifiable Acceptance Gate:** Lock pre-registered cluster promotion gates to >= 98% Invariant Adherence (zero tolerance for unflagged hallucinations or missing Level D gates) and <= 40% Token Overhead over a bare baseline.
5. **Purge / Archive the 1,560 Staged Backlog:** Run the staged cards through the cluster promotion eval harness in offline batch windows using free-tier headless Python batch scripts logging directly to a Google Sheets evaluation ledger; permanently archive all un-evaluated or failing cards while strictly maintaining the $0 budget limit.

## 4\. Priority Implementation Checklist Table

| Priority | Task Description | Target Subsystem / File |
| --- | --- | --- |
| **P0** | Refactor architecture to Single-Kernel Monism (Sentinel = Kernel; Optimus = Subsystem) | DPR Sections 1 & 2, 04\_Shared\_Operating\_Contract |
| --- | --- | --- |
| **P0** | Re-layer sentinel-manager (Intake Gate) and verifier-officer (Sentinel Authority) | Native Agent Skills (sentinel-manager, verifier-officer) |
| --- | --- | --- |
| **P1** | Codify **M-0341 (Evidence Control Is Not a Drafting Privilege)** | Bucket\_5\_Guardrails\_v2.md |
| --- | --- | --- |
| **P1** | Deploy Symmetric Deadlock Arbitration Protocol (R1/R2/R3 + R3-halt default) | project-coordinator, Bucket\_1\_Directives\_v2.md |
| --- | --- | --- |
| **P1** | Implement Dual-Channel Evidence Pipeline & Deterministic Verifier Hash Gate | researcher, operator, verifier-officer |
| --- | --- | --- |
| **P2** | Deploy Phase 4 Pre-Audit Deterministic Shape Linter (\[UNBOUND\_CLAIM\]) | operator skill contract |
| --- | --- | --- |
| **P2** | Static Pruning Pass (Screen 1: Falsifiable; Screen 2: Active Skill Reference) | 02\_The\_Living\_Guidebook |
| --- | --- | --- |
| **P3** | Build Offline Eval Harness (~2,300 batched runs) for Cluster Prefixes & M-PROP cards | Offline Test Suite (Dedicated Batch Window) |
| --- | --- | --- |
| **P3** | Calibrate the ~30 Provable Core Engines with dedicated test/probe suites | Canonical Index (Master\_Index\_v2.md) |
| --- | --- | --- |

## 5\. Master Record Addendum: Operational Amendments & Empirical Parameter Calibrations

**Date Integrated:** 28 October 2026  
**Status:** Ratified Operational Addendum

### 1\. Concrete Parameter Calibrations:

- **Demand-Read Budget Cap (Point 13):** Set to N = 3 individual reads before mandatory batching manifest.
- **Falsifiable Promotion Gates (Point 25):** Set to >= 98% Invariant Adherence and <= 40% Token Overhead.
- **Scope-Split Expiration (Point 14):** 14 calendar days or 3 sessions before auto-transition to \[SCOPE\_SPLIT\_ABANDONED\].

### 2\. Operational Invariant Safeguards:

- **Synchronous Next-Turn Interrupt Gate:** Replaces passive wall-clock timeout defaults with active turn-level unblocking on silence/diversion.
- **Deterministic Tool-Assisted Linter:** Operator pre-audit runs regex code screening, prohibiting LLM self-reflection sycophancy.
- **Two-Tier Cache Architecture:** Universal Frozen Substrate (~1,500 tokens) + Modular Cluster Prefix to guarantee cross-role KV-cache persistence.
- **Zero-Dollar Eval Infrastructure:** Headless Python scripts and Google Sheets evaluation logging decoupled from interactive chat budgets.