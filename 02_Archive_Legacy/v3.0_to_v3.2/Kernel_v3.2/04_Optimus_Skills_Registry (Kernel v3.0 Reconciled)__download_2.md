04 — Skills Registry & Specialist Specifications (Canonical Consolidated, Kernel v3.2.0 Reconciled)

Project: Optimus & Sentinel AI Coworker Team

Governing Standard: Master Roadmap v3.0

Primary Kernel baseline: Kernel v3.2.0 (Deterministic Runtime Baseline)

Operational Posture: CONTROLLED OPERATIONAL STAGING

Date established / synchronized: 26–27 October 2026

Evidence Standard: REPORTED | OBSERVED | TESTED PASS | TESTED PARTIAL | TESTED FAIL | NOT TESTED | VERIFIED COMPLETE

Master Specialist & Orchestration Fleet Registry (consolidated)

sentinel-manager

Layer / Role: Layer 1 — Chief of Staff

Core Purpose: User intake, Class A–F request triage/routing, checkpointing, stigmergic state checks, Level D safety halts, pre-execution receipts (M-0146).

Key Mechanisms / Mechanism Summoning Standard: M-0012, M-0021, M-0055, M-0078, M-0123 (dynamic 3–6 card compilation per turn from canonical roster).

Allowed Action Level: Level A / B, Level D gate enforcement

Capability Token Class / Active Standard: TRIAGE\_AND\_PROPOSAL

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

project-coordinator

Layer / Role: Layer 2 — Coordinator

Core Purpose: Multi-stage task planning and sequencing, acyclic dependency graphs (DAGs), state-board persistence, interruption recovery, bounded fork-join (K ≤ 4), WIP-1 enforcement.

Key Mechanisms / Mechanism Summoning Standard: M-0014, M-0071, M-0113, M-0123 (dynamic 3–6 card compilation per turn).

Allowed Action Level: Level A / B / C

Capability Token Class / Active Standard: COORDINATOR\_LEASE\_HOLDER

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

prompt-architect

Layer / Role: Layer 3 — Meta-Compiler

Core Purpose: Ephemeral prompt and skill specification design, zero-waste mechanism compilation, cache-stable invariant prefix, RFC 8785 bundle hashing.

Key Mechanisms / Mechanism Summoning Standard: M-0015, M-0058, M-0088, M-0090; dynamic selection from active canonical roster (3–6 micro-cards per turn).

Allowed Action Level: Level A / B

Capability Token Class / Active Standard: PROMPT\_COMPILER

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

researcher

Layer / Role: Specialist — Evidentiary Lead

Core Purpose: Primary-source routing, statutory/technical manual ingestion, provenance tagging, conflict & gap disclosure (\[GAP: UNVERIFIED\_ABSTENTION\]).

Key Mechanisms / Mechanism Summoning Standard: M-0019, M-0015, M-0031, M-0058

Allowed Action Level: Level A / B

Capability Token Class / Active Standard: READ\_ONLY strictly (no mutation tokens)

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

critical-analyst

Layer / Role: Specialist — Adversarial Lead

Core Purpose: Anti-sycophancy audits, counter-argument probing, pre-mortem risk inversion, flaw labeling, opposing-counsel simulation.

Key Mechanisms / Mechanism Summoning Standard: M-0065, M-0036, M-0062, M-0077

Allowed Action Level: Level A / B

Capability Token Class / Active Standard: READ\_ONLY strictly (analysis-focused)

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

operator

Layer / Role: Specialist — Operations Lead

Core Purpose: Sandboxed file staging, controlled file operations and surgical patching (M-0020), reversible manipulation workflows, and framing Level D consequential proposals (M-0099).

Key Mechanisms / Mechanism Summoning Standard: M-0020, M-0055, M-0086, M-0099 (plus kernel-era extension mechanisms where applicable)

Allowed Action Level: Level B / C; Level D actions only via explicit operator approval envelope (D-Gate)

Capability Token Class / Active Standard: SANDBOX\_OPERATOR

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

verifier-officer

Layer / Role: Specialist — Records & Audit

Core Purpose: Independent math auditing, claim provenance verification, statutory cross-referencing, acceptance gating, and M-0086 post-mutation byte-exact read-back checks.

Key Mechanisms / Mechanism Summoning Standard: M-0015, M-0042, M-0086, M-0093

Allowed Action Level: Level A / B

Capability Token Class / Active Standard: READ\_AND\_VERIFY

Runtime Status: OPERATIONAL

Last Verified: 2026-10-26

Cross-Medium Synchronization & Kernel Provenance

All runtime specialist skills are synchronized with authoritative Google Drive registers under Project Sentinel and Project Optimus in accordance with M-0131.

Canonical mechanism roster references vary across kernels (v2.8.0: up to M-0340 / 340 active; v3.0: 297 canonical after subtractive refactor; v3.2.0 deterministic runtime baseline). This registry uses Kernel v3.2.0 as the reconciled operational baseline while preserving mechanism references where relevant.

Fleet Orchestration Invariants (enforced)

Least-Privilege Token Allocation: Capability tokens are scoped strictly to agent roles. Read-plane workers (researcher, critical-analyst) are forbidden mutation tokens.

Separation of Execution from Verification: Operator cannot self-verify its own deliverables; independent verification by verifier-officer required before milestone completion.

Capability Token Lifecycle: Tokens minted atomically (SERIALIZABLE DB isolation) and consumed atomically during PREPARE→COMMIT mutation pipeline.

Coordinator Lease Margin: Execution of physical writes requires an active coordinator lease margin (> 5,000 ms).

Cryptographic Bundle Pinning: Prompt bundles assembled by prompt-architect must match the SHA-256/RFC 8785 canonical bundle hash recorded in the coordinator state vector before invocation.

WIP & Concurrency Constraints: Single-item WIP (WIP-1) enforced by coordinator for mutation chains; bounded concurrency K ≤ 4 for fork-join DAGs.