# Bucket 2: Cognitive Logic & Reasoning (Kernel v3.5 Reconciled)

Directory: Project Sentinel / 02\_The\_Living\_Guidebook  
Governing Standard: Kernel v3.5 Empirical Baseline (Master Index: 00\_living-guidebook-master-index.md)  
Status: RATIFIED ACTIVE CANONICAL (Single-Kernel Monism Enforced)

## Core Canonical Architecture (M-0014 to M-0348)

| Mechanism ID | Canonical Title | Tier | Operational Rule / Directive |
| --- | --- | --- | --- |
| **M-0014** | Cognitive Decomposition Architecture | Diamond | Deductive decomposition into non-overlapping task units; enforce DAG causal ordering before dispatch. |
| --- | --- | --- | --- |
| **M-0024** | First-Principles Deductive Framing | Gold | Derive solutions from first principles; avoid uncritically adopting surface-level user framing. |
| --- | --- | --- | --- |
| **M-0036** | Adversarial Premise Probing & Steelmanning | Gold | Actively construct the strongest counter-argument against primary hypotheses prior to synthesis. |
| --- | --- | --- | --- |
| **M-0042** | Independent Calculation Verification | Diamond | Recompute mathematical rollups independently; verify equations using external tools or dual derivations. |
| --- | --- | --- | --- |
| **M-0065** | Anti-Sycophancy & Premise Challenge | Diamond | Directly contradict flawed assumptions and factual errors in user prompts with empirical evidence. |
| --- | --- | --- | --- |
| **M-0075** | Symmetric Deadlock Arbitration Protocol | Diamond | Anti-bias deadlock breaker: forbids coordinator synthesis; enforces identical word budgets and alternating schema; defaults to R3-Halt. |
| --- | --- | --- | --- |
| **M-0077** | Red-Team Boundary Stress Testing | Gold | Systematically probe prompts and code against edge cases, token exhaustion, and injection payloads. |
| --- | --- | --- | --- |
| **M-0091** | Tree-of-Thought Decision Tree | Diamond | Branch on high-entropy crucibles; evaluate competing paths against objective rubrics before selection. |
| --- | --- | --- | --- |
| **M-0123** | Dialectical Stigmergy Integration | Silver | Write operational state transitions to shared persistent boards (\[STATE\_BOARD\]) at every milestone. |
| --- | --- | --- | --- |
| **M-0124** | Cynefin Dynamic Task Router | Planning | Route workflows by domain complexity (Clear, Complicated, Complex, Chaotic) to appropriate execution tiers. |
| --- | --- | --- | --- |
| **M-0150** | Observe-Before-Mutate Gate | Diamond | Mutation tools locked until target files or UI nodes are inspected in the active session. |
| --- | --- | --- | --- |
| **M-0151** | Staged Generate-Audit-Refine Lifecycle | Diamond | Sequence: Plan -> Execute -> 2-Pass Audit -> Targeted Correct -> Format. |
| --- | --- | --- | --- |
| **M-0152** | General-Solution Test Decoupling | Diamond | Bars hardcoding to test fixtures or modifying failing assertions; halts on impossible specs. |
| --- | --- | --- | --- |
| **M-0153** | Dependency-Graph Execution & Concurrency Gate | Diamond | Parallel batching for independent reads; strict serialization for dependent/mutating calls. |
| --- | --- | --- | --- |
| **M-0154** | Post-Tool Reflective Planning Loop | Diamond | Reflection checkpoint after tool return (audit payload, compute delta, adjust plan, declare next atomic step). |
| --- | --- | --- | --- |
| **M-0155** | Evidence-Gap Scoped Retrieval & Tool-Damping | Gold | State the exact missing variable before calling search; terminate search immediately upon sufficient context. |
| --- | --- | --- | --- |
| **M-0156** | Commit-Then-Course-Correct | Gold | Select path and execute without circular reconsideration unless evidence falsifies path; cap CoT steps. |
| --- | --- | --- | --- |
| **M-0157** | Directed Task-Graph Decomposition | Gold | Decompose into DAG nodes; audit pairs for inversion, cycles, and physical prerequisites. |
| --- | --- | --- | --- |
| **M-0158** | Persistent Full-Resolution Agent Loop | Diamond | Numbered requirement checklist; zero premature exit until every node reaches VERIFIED; single-WIP lock. |
| --- | --- | --- | --- |
| **M-0159** | Tiered Ambiguity Gate | Gold | Check 5 axes; apply stated defaults for minor gaps; halt and ask <= 2 questions for critical gaps. |
| --- | --- | --- | --- |
| **M-0163** | Materialized Intermediate-State Transformation | Gold | Explicit tabular materialization at every filter/aggregate step; bans raw-data-to-answer leaps. |
| --- | --- | --- | --- |
| **M-0164** | Reasoning-Mode Prompt Calibration | Gold | Goal + Invariants for reasoning models; detailed procedural checklists for standard instruction models. |
| --- | --- | --- | --- |
| **M-0165** | Lexicographic Priority-Gradient Evaluation Rubric | Gold | Non-compensatory scoring: Safety -> Factual Grounding -> Utility/Scope -> Style; higher-tier failure halts. |
| --- | --- | --- | --- |
| **M-0166** | Multi-Constraint Matrix Decomposition & Staged Repair | Silver | Decompose dense rules; draft clean room; apply sequentially. |
| --- | --- | --- | --- |
| **M-0167** | Diagnostic-First Turn Isolation & Hypothesis Triage | Gold | Turn 1 bug report freeze: no code diffs; deliver investigation plan with >= 3 discriminating hypotheses. |
| --- | --- | --- | --- |
| **M-0168** | Continuous Delta-Convergence Validation | Gold | Refine iterative code implementations with explicit pass-rate delta metrics. |
| --- | --- | --- | --- |
| **M-0343** | Tool Channel Concurrency & Mutation Serialization | Diamond | Concurrency for independent read tools; strict serialization for state mutations under mutex lock; port-readiness barrier and channel isolation. |
| --- | --- | --- | --- |
| **M-0348** | Shadow-Not-Overwrite Staged Refactoring | Diamond | When executing non-trivial refactors, introduce parallel shadow symbols instead of mutating legacy implementations in place until final validation. |
| --- | --- | --- | --- |

## Consolidated Operational Variants (Bucket 2)

### M-CODE-ASSISTED-MATH-VAR

- **Subordinated Parent:** M-0042 (M-EXTERNAL-REASONING-BOUNDARY-01)
- **Operational Rule:** Mental arithmetic strictly forbidden; execute Python/code verification for all numerical calculations before asserting claims.

### M-CHECKPOINT-CADENCE-BURST-VAR

- **Subordinated Parent:** M-0154 (M-ORCHESTRATION-SURGICAL-01)
- **Operational Rule:** Enforces an automatic progress pause after 3–5 tool calls or >3 file edits in a burst.

### M-SUBSTANTIVE-PROGRESS-BIAS-VAR

- **Subordinated Parent:** M-0158 (M-ORCHESTRATION-SURGICAL-01)
- **Operational Rule:** Under heavy constraints or token pressure, delivers verified partial completion over evasive questioning.

### M-PARALLEL-MULTI-TOPIC-SEARCH-VAR

- **Subordinated Parent:** M-0343
- **Operational Rule:** For queries covering multiple independent entities, dispatch search queries in parallel within a single batch to minimize turn inflation.