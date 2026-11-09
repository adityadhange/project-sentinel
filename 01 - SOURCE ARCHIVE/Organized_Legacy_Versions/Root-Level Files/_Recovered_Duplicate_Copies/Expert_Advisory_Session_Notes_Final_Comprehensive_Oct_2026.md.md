# Project Sentinel & Optimus — Expert Advisory Session Notes

**Date:** 28 October 2026  
**Session Duration:** Extended Expert Advisory Session  
**Objective:** Ingest architectural critique, failure mode analysis, and optimization suggestions from external AI systems expert without in-session mutation.

## 1\. Core Discussion Questions Addressed

1. **Adversarial Deadlock Arbitration (Q3):** Eliminating coordinator framing bias and managing loop stalling.
2. **Subtractive Granularity & Evaluation Harnesses (Q1 & Q4):** Empirical calibration of rule density, cluster-bounded prefix compilation, and promotion benchmarking.
3. **Context Compression vs. Verbatim Quote Ledgers (Q2):** Asymmetric tiering, hash-anchored evidence, and claim-driven quote promotion.
4. **\[UNBOUND\_CLAIM\] Detection & Stylistic Prose Isolation:** Grammatical shape checking vs. syntactic sentence classification, operator-side linter decoupling.
5. **Indirect Prompt Injection via Ingested Opposing Evidence (M-0058):** Dual-channel quote architecture, reversible delimiter escaping, and deterministic non-LLM verification.

## 2\. Detailed Expert Feedback & Technical Blueprints

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
  4. **Staged Technique (M-PROP) Promotion Pipeline:** The exact same cluster-bounded harness gates promotion of the 1,560 staged techniques in quarantined registries.
  5. **Resource Model:** Run in dedicated offline batch window; never siphon live conversational phase reserves (M-0308).

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
- **Deterministic Non-LLM Verification:** Verifier's PASS/FAIL on quote accuracy is computed via deterministic string/hash comparison, not by reading the quote and "deciding." A quote cannot manipulate the verifier because the verdict logic is non-interpretive code.
- **Semantic Analysis Quarantine:** When an agent must reason over quote semantics (e.g., critical-analyst probing an opposing pleading), it runs in a strictly read-only, no-tool, no-verdict posture—it may flag issues for human attention but cannot alter state or issue audit verdicts.

### Topic 6: Summary of Residual Vulnerabilities & Master Invariant

1. **Under-Citation Shield:** Verifier-enforced \[UNBOUND\_CLAIM\] hard fail stops operators from bypassing T1 promotion.
2. **Demand-Read Caps:** Bound per audit cycle ($\\le N$, requiring batched reads thereafter) to prevent slow-drip turn exhaustion.
3. **Scope-Split Reunion Links:** Mandatory \[DEFERRED\_LINK: <parent\_task\_id>\] on deferred branches and visible \[SCOPE\_SPLIT\_PENDING\] markers on parent briefs.
4. **Governing Master Invariant Proposed:**
  - **"Evidence Control Is Not a Drafting Privilege"** (M-0341): Formalizes that evidentiary promotion, classification, and scope splitting are governed by deterministic system rules rather than the drafting agent's discretion.

## 3\. Post-Session Action Register (Principal Triage)

- Codify **M-0341 (Evidence Control Is Not a Drafting Privilege)** in Bucket\_5\_Guardrails\_v2.md.
- Implement Dual-Channel Quote Promotion (Evidence Channel vs. Quarantine Channel with reversible escaping) in researcher and operator.
- Implement deterministic string/hash verification in verifier-officer (decoupling quote auditing from LLM interpretation).
- Add Phase 4 pre-audit deterministic shape linter for numbers, dates, and statutory sections to catch unbound claims before verifier gating.
- Update project-coordinator with the Symmetric Deadlock Arbitration Protocol (R1/R2/R3 + R3-halt default).
- Specify and schedule the offline ~2,300-run cluster adherence evaluation harness.