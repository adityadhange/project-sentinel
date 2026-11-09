# Project Sentinel & Optimus — Expert Advisory Session Notes

**Date:** 28 October 2026  
**Session Scope:** Full Expert Advisory Session (Core Questions, Residual Risks & Corpus Audit)  
**Objective:** Ingest architectural critique, failure mode analysis, and optimization suggestions from external AI systems expert without in-session mutation.

## 1\. Executive Summary: The Structural Shift

The external expert session identified a foundational vulnerability across the architecture: **the conflation of descriptive volume with empirical efficacy**. Project Sentinel's 261 active Master Engines and 1,560 staged cards represent a "corpus awaiting proof" rather than a validated governance kernel.

The primary recommendation across all domains is **empirical instrumentation**: replace design assertions with measured curves, replace count-based rules with cluster-bounded cache units, and enforce a **Corpus Firing Audit** before adding any new mechanisms.

## 2\. Topic-by-Topic Technical Recommendations

### Topic 1: Adversarial Deadlock Arbitration (Q3)

- **Problem Statement:** Coordinator auto-synthesis + presentation order introduces systemic framing bias (defaulting to verifier conservatism). Max-1 loop breaker risks deadlocking the fleet.
- **Architectural Tie-Breaker Protocol:**
  1. **Symmetric Frame (Bias Elimination):**
    - Coordinator strictly forbidden from writing synthesis summaries.
    - Randomized/order-alternating presentation logged for audit trails.
    - Identical word budgets and fixed schema: \[CLAIM\], \[EVIDENCE\], \[WHAT\_WOULD\_CHANGE\_MY\_MIND\].
  2. **Pre-Defined Operator Classifications:**
    - **(R1) Evidentiary:** Verifier wins; back-edge to Researcher for missing primary source.
    - **(R2) Strategic-with-Flag:** Critical Analyst wins; deliverable marked with visible \[UNVERIFIED\_STRATEGIC\_POSITION\] tag (hard-blocked from filing until removed).
    - **(R3) Scope-Split:** Proceed on verified ground only; defer contested strategic claim to an isolated follow-up payload.
  3. **Deterministic Timeout Default:**
    - If operator silent > T: default to **R3-halt** (not R1). Removes verifier home-field advantage while guaranteeing epistemic safety.
  4. **Conflict-of-Interest Gate:** Neither specialist may recommend R1, R2, or R3 (triggers invariant penalty).

### Topic 2: Subtractive Granularity vs. KV-Cache Stability (Q1 & Q4)

- **Status Calibration:** Demote 3–6 engine rule from "cardinal architecture" to an operational working heuristic pending measurement.
- **Architectural Solution:**
  1. **Instrument Before Merging:** Dedicated offline benchmark harness across 23 clusters sampling 10–20 held-out tasks across 3/4/5/6/8 engines scored against a fixed rubric (~2,300 batched runs).
  2. **Cluster-Bounded Prefix as Unit:** Make the functional cluster the cacheable prefix segment. Engines only load within their owning cluster; cross-cluster links resolve strictly by pointer, stabilizing KV-cache prefix reuse while preserving M-0122 provenance.
  3. **Falsifiable Pre-Registered Acceptance Gate:** Pre-register exact promotion thresholds (e.g., $X \\ge 95%$ max adherence at $Y \\le 60%$ token overhead) before evaluating.
  4. **Resource Model:** Run in dedicated offline batch window; never siphon live conversational phase reserves (M-0308).

### Topic 3: Context Compression vs. Verbatim Quote Ledgers (Q2)

- **Asymmetric Tiering Architecture:**
  - **T1 (Verbatim Audit Floor):** Every quote a material claim directly cites. Immutable and full text.
  - **T2 (Hash-Anchored Pointer):** Quotes cited as context or staged during ingestion (\[Q#\] + sha256 + 1-line locator).
  - **T3 (Summary Only):** Background/extraneous context. Hard prohibition against citing T3 in affirmative claims.
- **Claim-Driven Promotion Lifecycle:**
  1. **Phase 2 (Ingestion):** Researcher stages all extracted evidence as T2 by default.
  2. **Phase 4 (Drafting):** Operator binding a claim to \[Q#\] automatically promotes it to T1 in the deliverable payload envelope.
  3. **Phase 5 (Verification):** Verifier audits promoted T1s; triggers \[DEMAND\_READ: Q#\] on demand for any T2 background context.
  4. **Fail-Closed Gate:** Binary fail on any T1 hash mismatch (M-0324 Stage 1).

### Topic 4: \[UNBOUND\_CLAIM\] Detection without Paralyzing Prose

- **Core Principle:** Do not classify whole sentences. Classify verifiable propositions by grammatical shape.
- **Narrow High-Precision Gate:**
  - **Hard-Fail Shapes:** Numeric assertions ($X = N$, units, percentages, dates), statutory/standard citations (§, Section N, Clause N, "per CPHEEO"), causal/empirical assertions ("caused", "exceeds", "fails to"), and superlatives/comparatives ("only", "highest").
  - **Pass Reasoning Prose:** Transitions, rhetorical framing, legal argument connectors, boilerplate ("Accordingly", "It is submitted that", "Under settled law") carry zero factual weight and pass cleanly.
  - **Gray Zone Soft Flag:** Factual-looking statements lacking \[Q#\] trigger \[UNBOUND\_CLAIM: REVIEW\]—requiring operator quote binding or explicit \[INFERENCE: DEDUCTIVE\_VALID\] tagging.
- **Decoupled Operator Linter:** Run shape check as a cheap deterministic linter in Phase 4 (operator-side) before audit. Verifier audits linter output rather than raw prose, preventing style policing.

### Topic 5: Indirect Prompt Injection Isolation via Dual-Channel Quotes (M-0058)

- **Core Reframe:** T1 text is data to be reproduced, never data to be interpreted.
- **Dual-Channel Architecture:**
  1. **Evidence Channel (Reproduction Only):** Raw, byte-exact, hash-locked string. Used solely to render into the deliverable and verify sha256. Never exposed to an LLM reasoning prompt.
  2. **Quarantine Channel (Reasoning Inert):** Wrapped in <untrusted\_data id=Q#> and structured as {quote\_id, sha256, byte\_exact\_string, provenance\_locator}. Treated strictly as inert values.
- **Reversible Escaping over Stripping:** Wrapper-relevant tokens (</untrusted\_data>, fake \[FACT:...\] or \[SYSTEM OVERRIDE\] tags) are reversibly escaped inside the quarantine envelope. Stored source bytes are never mutated; rendered deliverable un-escapes cleanly.
- **Deterministic Non-LLM Verification:** Verifier's PASS/FAIL on quote accuracy is computed via deterministic string/hash comparison, not by reading the quote and "deciding."
- **Semantic Analysis Quarantine:** When an agent must reason over quote semantics (e.g., critical-analyst probing an opposing pleading), it runs in a strictly read-only, no-tool, no-verdict posture—it may flag issues for human attention but cannot alter state or issue audit verdicts.

### Topic 6: The Corpus Fallacy & The Firing Log Mandate (Direct Library Critique)

- **Core Diagnosis:**
  - 261 active engines + 1,560 staged cards is a **corpus awaiting proof**, not an active governance kernel.
  - "A card that never fires is dead weight that looks like rigor."
  - Merging 342 down to 261 was done by arithmetic counting rather than causal impact. Counting is not evidence of efficacy.
  - The 1,560 staged cards are currently a "graveyard giving false comfort," not a pipeline.
- **Direct Remedies Mandated:**
  1. **Immediate Corpus Freeze:** Zero new mechanism cards (including proposed M-PROP cards) may be drafted or added until an empirical firing audit is executed.
  2. **The Firing Log & Hit Counter:**
    - Instrument every card in the active index with a verifiable telemetry counter:
      - Loaded\_Count: How often the card was selected by prompt-architect.
      - Evaluation\_Count: How often an invariant on the card was evaluated.
      - Outcome\_Impact\_Count: How often the card caused a state change, forced a revision, prevented a hallucination, or flipped a verifier PASS/FAIL.
  3. **Demotion to Documentation / Quarantine:**
    - Any active card with $0$ outcome impact across test batches is demoted out of the active compilation path into documentation/archive. Documentation does not belong in the runtime prompt.
  4. **The Staged Backlog Dilemma:**
    - The 1,560 quarantined cards must either be tied directly to the Q4 evaluation promotion harness or permanently archived. An unmeasured backlog is self-deception.

## 3\. Prioritized Post-Session Action Register (Principal Triage)

| Priority | Action Item | Target Artifact / Skill | Governing Principle |
| --- | --- | --- | --- |
| **P0** | **Corpus Freeze & Firing Audit** | 02\_The\_Living\_Guidebook | Freeze additions; instrument Hit Counters (Loaded vs Outcome\_Changed). Demote zero-effect cards. |
| --- | --- | --- | --- |
| **P0** | **Unbound Claim Shape Linter** | operator (Phase 4) & verifier-officer (Phase 5) | Grammatical shape check on numbers, dates, citations. Binary fail on unbound facts; pass connective prose. |
| --- | --- | --- | --- |
| **P1** | **Dual-Channel Quote Engine** | researcher & verifier-officer | Split evidence (byte-exact reproduction) from quarantine channel (inert reasoning data with reversible escape). |
| --- | --- | --- | --- |
| **P1** | **Deterministic Verification Gate** | verifier-officer (M-0086 / M-0324) | Quote accuracy validated via non-LLM sha256/string equality, immune to prompt injection persuasion. |
| --- | --- | --- | --- |
| **P1** | **Symmetric Deadlock Tie-Breaker** | project-coordinator | R1/R2/R3 operator rubric; no coordinator synthesis; randomized order; R3-halt timeout default. |
| --- | --- | --- | --- |
| **P2** | **Cluster-Bounded Prefix Unit** | prompt-architect | Shift unit of compilation from 3–6 card count to 1 cluster = 1 cacheable prefix segment. |
| --- | --- | --- | --- |
| **P2** | **Offline Eval Harness (~2,300 runs)** | Dedicated Batch Sandbox | Run adherence curves across 23 clusters; gate promotion of staged backlog or archive it. |
| --- | --- | --- | --- |