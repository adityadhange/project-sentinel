# Project Sentinel & Optimus — Expert Advisory Session Notes

**Date:** 28 October 2026  
**Session:** Complete Advisory & Corpus Audit Specification  
**Objective:** Ingest architectural critique, failure mode analysis, and optimization suggestions from external AI systems expert without in-session mutation.

## 1\. Core Discussion Questions Addressed

1. **Adversarial Deadlock Arbitration (Q3):** Eliminating coordinator framing bias and managing loop stalling.
2. **Subtractive Granularity & Evaluation Harnesses (Q1 & Q4):** Empirical calibration of rule density, cluster-bounded prefix compilation, and promotion benchmarking.
3. **Context Compression vs. Verbatim Quote Ledgers (Q2):** Asymmetric tiering, hash-anchored evidence, and claim-driven quote promotion.
4. **\[UNBOUND\_CLAIM\] Detection & Stylistic Prose Isolation:** Grammatical shape checking vs. syntactic sentence classification, operator-side linter decoupling.
5. **Indirect Prompt Injection via Ingested Opposing Evidence (M-0058):** Dual-channel quote architecture, reversible delimiter escaping, and deterministic non-LLM verification.
6. **Corpus Reality Check & The Firing Log Mandate:** Dismantling catalog sprawl, demoting un-fired cards, and defining the true empirical kernel.

## 2\. Detailed Expert Feedback & Technical Blueprints

### Topic 1: Adversarial Deadlock Arbitration (Q3)

- **Problem Statement:** Coordinator auto-synthesis + presentation order introduces systemic framing bias. Max-1 loop breaker risks deadlocking the fleet.
- **Architectural Tie-Breaker Protocol:**
  1. **Symmetric Frame (Bias Elimination):** Coordinator strictly forbidden from writing synthesis summaries. Randomized/order-alternating presentation. Fixed schema: \[CLAIM\], \[EVIDENCE\], \[WHAT\_WOULD\_CHANGE\_MY\_MIND\].
  2. **Pre-Defined Operator Classifications:**
    - (R1) Evidentiary: Verifier wins; back-edge to Researcher.
    - (R2) Strategic-with-Flag: Critical Analyst wins; deliverable carries visible \[UNVERIFIED\_STRATEGIC\_POSITION\].
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

### Topic 6: The Corpus Reality Check & Firing Log Mandate (Expert Critique)

- **The Core Vulnerability Exposed:**
  - 261 active + 1,560 staged is a corpus awaiting proof, not a governance kernel.
  - Subtractive refactoring was conducted by taxonomic counting, not empirical efficacy.
  - Staged backlog is an unmeasured graveyard giving false comfort of rigor.
  - "VERIFIED COMPLETE" in the DPR signified textual reconciliation and deduplication, NOT causal verification.
- **The 4-Part Mandate:**
  1. **Corpus Freeze:** Zero additions to active or staged until an empirical firing audit is executed.
  2. **Firing Log & Hit Counter:** Instrument every mechanism card with LOAD\_COUNT vs. CAUSAL\_FIRING\_COUNT (did it change an outcome, trigger a gate, or alter verifier pass/fail).
  3. **Demotion to Inactive:** Cards with zero observed causal effect must be demoted out of the active kernel into reference documentation.
  4. **Purge / Hard-Archive:** The 1,560 staged cards must either pass the promotion eval harness or be permanently archived. Documentation does not belong in the execution path.

## 3\. Master Post-Session Action Register

- **M-0341: Evidence Control Is Not a Drafting Privilege** (unbound claim detection, demand-read caps, scope-split reunion links).
- **Corpus Freeze & Firing Audit Protocol**: Freeze canonical index at M-0340; instrument load-vs-fire counters.
- **Dual-Channel Evidence Pipeline**: Separate Evidence Channel (byte-exact reproduction) from Quarantine Channel (escaped reasoning data).
- **Deterministic Verifier Hash Gate**: Transition quote audit from LLM evaluation to deterministic code comparison.
- **Symmetric Deadlock Arbitration**: Codify R1/R2/R3 + R3-halt timeout in coordinator.
- **Offline Evaluation Harness**: Schedule batch window for 23-cluster adherence and staged technique promotion.