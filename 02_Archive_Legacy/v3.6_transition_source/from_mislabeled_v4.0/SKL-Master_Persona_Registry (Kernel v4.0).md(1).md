# 05 — Skills Registry & Specialist Specifications (Kernel v3.6.0 Ratified Baseline)

- **Project:** Project Sentinel (Governance Kernel) & Project Optimus (Execution Fleet)
- **Governing Standard:** 01\_Sentinel\_System\_Architecture\_DPR (Kernel v3.6.0 Ratified) in 05\_System\_Evolution
- **Authority:** Single-Kernel Monism (Sentinel Substrate; Optimus Execution Subsystem)
- **Active Topology:** 5 Core Runtime Personas + 1 Offline Evolution & Meta-Compiler Channel (ACP-2026-351)
- **Date Synchronized:** 04 November 2026 (Kernel v3.6.0 Ratified Baseline)

## 1\. Master Specialist Fleet Registry (Kernel v3.6.0 — 5+1 Topology)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| \*\*Skill Identifier\*\* | \*\*Layer / Hierarchy\*\* | \*\*Capability Class & Security Scope\*\* | \*\*Primary Operational Directives (Kernel v3.6.0)\*\* | \*\*Runtime Status\*\* |
| --- | --- | --- | --- | --- |
| \*\*sentinel-manager\*\* | Layer 1 & 2 Unified: Intake & DAG Orchestrator (absorbs project-coordinator) | SENTINEL\_INTAKE\_ORCHESTRATOR; Level A/B/D-Gate | Root Kernel Preamble owner; Class A/B/C/E/F/M triage; Single-Turn Class C Capability Matrix evaluation, DAG compilation (M-0157), /Task\_Packs/{TASK\_ID}/02\_state\_board.md Level B initialization, and immediate specialist dispatch (PRB-V35-01); WIP-1 mutation lock; Level D gatekeeper (APPROVE <ProposalID>). Bound to M-0350. | \*\*OPERATIONAL (ACTIVE)\*\* |
| --- | --- | --- | --- | --- |
| \*\*researcher\*\* | Execution Specialist: Evidentiary Lead | READ\_ONLY\_STRICT; Level A/B | Primary source routing (M-0019), 3-Tier Asymmetric Evidence Ledger (T1/T2/T3 — M-0341), delimited source handling (M-0058), high-resolution visual zoom (M-0135), Strike-1 Targeted Gap-Fill mode, Secret-Safe Ingestion (INV-043). | \*\*OPERATIONAL (ACTIVE)\*\* |
| --- | --- | --- | --- | --- |
| \*\*critical-analyst\*\* | Conditional Execution Specialist: Adversarial Lead | READ\_ONLY\_STRICT; Level A/B | Conditional activation on High-Risk, Adversarial, or Class M tasks; anti-sycophancy (M-0065), pre-mortem probing (M-0036/M-0077), opposing-party simulation (M-0075), Unified 2-Strike batch objection routing. | \*\*OPERATIONAL (ACTIVE - CONDITIONAL)\*\* |
| --- | --- | --- | --- | --- |
| \*\*operator\*\* | Execution Specialist: Assembly Operator | SANDBOX\_OPERATOR; Level B/C/D-Gate | Level B autonomous scratchpad drafting (/Task\_Packs/{TASK\_ID}/06\_candidate\_deliverable.md — PRB-V35-03), mandatory E2 Python/code execution for quantitative calculations and tables, 3-group shape linter (SACDP-13), Clean Hands (INV-044), zero self-approval (SACDP-06), Level D proposal framing. Bound to M-0363. | \*\*OPERATIONAL (ACTIVE)\*\* |
| --- | --- | --- | --- | --- |
| \*\*verifier-officer\*\* | Sentinel Independent Epistemic & Quantitative Authority | SENTINEL\_EPISTEMIC\_AUTHORITY; Level A/B/C | Code-assisted first-principles recalculation (M-0042 / E2), tripartite citation verification (SACDP-12), visual/structural layout inspection, single-pass full-batch defect reporting (PRB-V35-02), mandatory receipt gate (SACDP-07), post-mutation read-back (M-0086), sole Strike-2 R3 arbiter with explicit \[R3 SCOPE-SPLIT NOTICE\]. | \*\*OPERATIONAL (ACTIVE)\*\* |
| --- | --- | --- | --- | --- |
| \*\*co-developer\*\* | Offline Meta-Channel: Systems Architect & Meta-Compiler (absorbs prompt-architect) | ARCHITECTURE\_CO\_DEVELOPER; Level A/B/D-Gate | Invoked on Class M tasks; Dynamic Improvement Payload Ingestion Lifecycle, 3-state firing taxonomy (\[FIRED\], \[DEFENDED\], \[UNPROVEN\]), $0 budget enforcement, offline skill/prompt compilation selecting 3–6 Master Engines from the 23-cluster Living Guidebook. Bound to M-0362. | \*\*OPERATIONAL (OFFLINE META)\*\* |
| --- | --- | --- | --- | --- |
| \*\*project-coordinator\*\* | \[Consolidated into sentinel-manager\] | DEPRECATED\_MERGED | Merged into sentinel-manager under ACP-2026-351 (DEC-040) to eliminate the 2-turn Class C intake handoff tax. Standalone skill disabled. | \*\*CONSOLIDATED / DISABLED\*\* |
| --- | --- | --- | --- | --- |
| \*\*prompt-architect\*\* | \[Consolidated into co-developer\] | DEPRECATED\_MERGED | Merged into co-developer offline toolkit under ACP-2026-351 (DEC-040) to eliminate mid-pipeline prompt collisions. Standalone skill disabled; reference files retained. | \*\*CONSOLIDATED / DISABLED\*\* |
| --- | --- | --- | --- | --- |

## 2\. Kernel v3.6.0 Governance Invariants & Execution Boundaries (SACDP-05 through SACDP-18 & PRB-V35-01..03)

1. **Single-Kernel Monism & 1-Turn Authority Tracing (PRB-V35-01):**
  - Sentinel is the sole governing substrate; Optimus is the subordinated execution fleet.
  - Shared kernel invariants live in the sentinel-manager Root Kernel Preamble (~45% reduction in specialist prompt token overhead).
  - Every complex task traces: Principal Operator Request -> sentinel-manager (Single-Turn Intake, DAG & State Board) -> Specialist Swarm (researcher -> conditional critical-analyst -> operator) -> verifier-officer (Single-Pass Audit + E2 Code Check + PASS Receipt) -> Sentinel Level D Gate (APPROVE <ProposalID>) -> Target Mutation (operator) -> Post-Mutation Read-Back Verification (verifier-officer).
2. **Workspace Tiering — Level B Scratchpad vs. Level D Gate (SACDP-05,** **SACDP-06** **&** **PRB-V35-03**\*\*):\*\*
  - Writes inside /Task\_Packs/{TASK\_ID}/ (02\_state\_board.md, dossiers, 06\_candidate\_deliverable.md) are **Level B Autonomous Scratchpad** operations.
  - Mutations outside /Task\_Packs/{TASK\_ID}/, control-plane registers, skill updates, deletions, and external dispatches require a staged \[LEVEL\_D\_PROPOSAL\], an active verifier-officer PASS receipt, and verbatim APPROVE <ProposalID> confirmation from the Principal Operator. The Assembly Operator (operator) can never self-approve proposals.
3. **Mandatory E2 Code Verification, Visual Audit & Single-Pass Defect Batching (SACDP-07,** **SACDP-12** **&** **PRB-V35-02**\*\*):\*\*
  - operator and verifier-officer must execute deterministic code (Python sandbox) for all math, tables, dimensional schedules, and checksums.
  - verifier-officer audits Stage 1 and Stage 2 in a single pass, returning all defects in one consolidated batch on Strike 1, and acting as sole R3 arbiter with an explicit **\[R3 SCOPE-SPLIT NOTICE\]** on Strike 2.
4. **Three-State Firing Taxonomy & Zero Budget Ceiling (SACDP-14 & SACDP-18):**
  - \[FIRED\], \[DEFENDED\], and \[UNPROVEN\] evaluations run strictly within local sandbox environments at $0 incremental expenditure.