# Project Sentinel & Optimus — Expert Advisory Session Notes

**Date:** 28 October 2026  
**Session Duration:** 30 Minutes  
**Objective:** Ingest architectural critique, failure mode analysis, and optimization suggestions from external AI systems expert without in-session mutation.

## 1\. Core Discussion Questions Prepared for Review

1. **Subtractive Granularity & Attention Density (M-0338):**
  - Having consolidated 342 mechanism cards down to 261 Master Engines across 23 functional clusters, where is the empirical inflection point where further merging degrades zero-shot instruction adherence versus benefiting KV-cache prefix stability?
2. **Context Compression vs. Verbatim Quote Ledgers (M-0134 / M-0015):**
  - Managing token economics: passing full <quotes> ledgers from researcher to verifier-officer guarantees epistemic zero-drift, but carries high token overhead. What hybrid compression or extractive pointer mechanisms maintain auditability without semantic leakage?
3. **Adversarial Deadlock Arbitration (M-0075 vs. M-0015):**
  - In our Max-1 Auto-Revision loop, how can we optimize automated arbitration when the adversarial red-team (critical-analyst) demands stronger rhetorical posture and the epistemic auditor (verifier-officer) demands total gap abstention?
4. **Automated Promotion Harness for Staged Techniques (M-PROP-CORE):**
  - Architecture for an automated benchmark/eval harness to validate the 1,560 staged techniques in quarantined registries before promoting to the canonical index.

## 2\. Live Expert Feedback & Technical Recommendations

### Topic 1: Adversarial Deadlock Arbitration (Q3)

- **Problem Statement Identified:**
  - Coordinator auto-synthesis + presentation order introduces systemic framing bias (structural home-field advantage defaulting to verifier conservatism).
  - Max-1 auto-revision loop stalling fleet without a structured resolution rubric.
- **Expert Tie-Breaker Protocol Design:**
  1. **Symmetric Frame (Eliminate Bias):**
    - Coordinator strictly forbidden from generating synthesis summaries.
    - Randomized/order-alternating presentation (logged for audit trail).
    - Identical word budgets and fixed schema for both agents: \[CLAIM\], \[EVIDENCE\], \[WHAT\_WOULD\_CHANGE\_MY\_MIND\].
  2. **Three Pre-Defined Classifications for Human Operator:**
    - **(R1) Evidentiary:** Verifier wins; back-edge to Researcher to obtain missing primary source.
    - **(R2) Strategic-with-Flag:** Critical Analyst wins; deliverable marked with visible \[UNVERIFIED\_STRATEGIC\_POSITION\] tag (hard-blocked from filing until removed).
    - **(R3) Scope-Split:** Proceed on verified ground only; defer contested strategic claim to an isolated follow-up payload.
  3. **Deterministic Timeout Default:**
    - If operator silent > T: default to **R3-halt** (not R1). Removes verifier home-field advantage while guaranteeing epistemic safety.
  4. **Conflict-of-Interest Gate:**
    - Neither specialist may recommend R1, R2, or R3. Doing so triggers a conflict-of-interest invariant penalty.
- **Operational Assessment:**
  - R3-halt does not cause an unacceptable bottleneck because Scope-Split permits uncontentious verified portions to proceed while quarantining only the disputed claim. Perfectly aligns with Tier 1 stakes and intentional operator gating (M-0055/M-0299).

### Topic 2: Subtractive Granularity vs. KV-Cache Stability (Q1 & Q4)

- **Status Grounding:**
  - 3–6 engine rule demoted from "cardinal architecture" to an operational working default / heuristic pending empirical calibration.
- **Expert Architectural Architecture:**
  1. **Instrument Before Merging:** Build a dedicated offline benchmark harness across all 23 clusters sampling 10–20 held-out tasks across 3/4/5/6/8 engines scored against a fixed rubric (~2,300 batched runs).
  2. **Cluster-Bounded Prefix as Unit:** Make the functional cluster the cacheable prefix segment. Engines only load within their owning cluster; cross-cluster links resolve strictly by citation/pointer, stabilizing KV-cache prefix reuse while preserving M-0122 provenance.
  3. **Falsifiable Pre-Registered Acceptance Gate:** Pre-register exact promotion thresholds (e.g., $X \\ge 95%$ max adherence at $Y \\le 60%$ token overhead) before evaluating.
  4. **Staged Technique (M-PROP) Promotion Pipeline:** The exact same cluster-bounded harness gates promotion of the 1,560 staged techniques in quarantined registries.
  5. **Resource Model:** Must run in a dedicated offline batch window; strictly prohibited from siphoning live conversational phase reserves (M-0308).

### Topic 3: Context Compression vs. Verbatim Quote Ledgers (Q2)

- **Tension Identified:**
  - Full verbatim ledgers carry prohibitive token overhead, but semantic summarization introduces drift.
  - Researcher cannot predict which quotes will be load-bearing at ingestion time.
- **Tiered Asymmetric Architecture:**
  - **T1 (Verbatim Audit Floor):** Every quote a material claim directly cites. Immutable and full text.
  - **T2 (Hash-Anchored Pointer):** Quotes cited as context or staged during ingestion (\[Q#\] + sha256 + 1-line locator).
  - **T3 (Summary Only):** Background/extraneous context. Hard prohibition against citing T3 in affirmative claims.
- **Claim-Driven Promotion Lifecycle:**
  1. **Phase 2 (Ingestion):** Researcher stages all extracted evidence as T2 by default.
  2. **Phase 4 (Drafting):** Operator binding a claim to \[Q#\] automatically promotes it to T1 in the deliverable payload envelope.
  3. **Phase 5 (Verification):** Verifier audits promoted T1s; triggers \[DEMAND\_READ: Q#\] on demand for any T2 background context.
  4. **Fail-Closed Gate:** Binary fail on any T1 hash mismatch (M-0324 Stage 1).

### Topic 4: Residual Vulnerabilities & Closing Expert Warnings

1. **Under-Citation / Promotion Bypass (Highest Priority):**
  - *Vulnerability:* Because promotion to T1 is operator-driven, an operator can under-cite material claims, leaving them unbound so they silently stay T2 and evade T1 binary hash audits.
  - *Remediation:* Verifier-officer must run an automated claim-detection pass over the draft and flag any affirmative assertion lacking a bound \[Q#\] as \[UNBOUND\_CLAIM\] → hard-fail. Promotion is operator-driven; coverage is verifier-enforced.
2. **Uncapped Demand-Read Slow-Drip Deadlock:**
  - *Vulnerability:* Verifier issuing unconstrained \[DEMAND\_READ: Q#\] calls in Phase 5 exhausts conversational turns without concluding.
  - *Remediation:* Cap demand-reads per audit cycle ($\\le N$, requiring batched reads thereafter) and register excessive demand-read loops against the Max-1 loop breaker.
3. **R3 Scope-Split Reunion Gap:**
  - *Vulnerability:* Advancing verified grounds while deferring contested claims leaves an open loop where the split payload never rejoins the parent brief, potentially shipping an incomplete deliverable unannounced.
  - *Remediation:* Deferred payloads must carry a \[DEFERRED\_LINK: <parent\_task\_id>\], and the parent deliverable must maintain an explicit, visible \[SCOPE\_SPLIT\_PENDING\] marker until reconciled or formally abandoned by the human operator.
4. **Cross-Cutting Kernel Invariant Proposed:**
  - **"Evidence Control Is Not a Drafting Privilege"**: Extends Level D principles to evidence promotion and scope splitting, eliminating operator/coordinator asymmetry over evidentiary thresholds.

## 3\. Triage & Follow-up Action Items (For Principal Review)

- Draft new mechanism card: **M-0341: Evidence Control Is Not a Drafting Privilege** (covering unbound claim detection, demand-read caps, and scope-split reunion markers).
- Codify Symmetric Deadlock Arbitration Protocol (R1/R2/R3 schema + coordinator synthesis prohibition) into Bucket\_1\_Directives\_v2.md and project-coordinator.
- Formalize Cluster-Bounded Prefix Architecture in prompt-architect and update M-0095/M-0338 documentation.
- Specify offline benchmark eval harness for the 23 clusters and 1,560 staged M-PROP techniques.
- Implement Claim-Driven Quote Promotion (T1/T2/T3) in researcher and verifier-officer.