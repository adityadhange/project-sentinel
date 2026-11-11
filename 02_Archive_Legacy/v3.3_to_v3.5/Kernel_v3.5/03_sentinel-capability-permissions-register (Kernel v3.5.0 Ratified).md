# 03 — Capability & Permissions Register (Kernel v3.5.0 Ratified Baseline)

- **Project:** Project Sentinel (Governance Kernel) & Project Optimus (Execution Fleet)
- **Governing Standard:** 01\_Sentinel\_System\_Architecture\_DPR (Kernel v3.5.0 Ratified) in 05\_System\_Evolution
- **Authority:** Single-Kernel Monism (Sentinel Substrate; Optimus Execution Subsystem)
- **Security Model:** Three-Tier Enforcement Taxonomy (E0 / E1 / E2) & Level B / Level D Workspace Tiering
- **Date Synchronized:** 03 November 2026 (Kernel v3.5.0 Ratified Baseline)

## 1\. Runtime Capability & Security Separation Matrix (Streamlined 5+1 Fleet)

| Subsystem / Role | Security Plane | Capability Class & Permissions | Enforcement Tier & Boundary |
| --- | --- | --- | --- |
| **sentinel-manager** | Layer 1 & 2 Unified: Sentinel Intake & DAG Orchestrator (absorbs project-coordinator) | SENTINEL\_INTAKE\_ORCHESTRATOR; Root Kernel Preamble owner; Class A/B/C/E/F/M triage; Single-Turn Class C Capability Matrix evaluation, DAG compilation (M-0157), /Task\_Packs/{TASK\_ID}/02\_state\_board.md Level B initialization, and immediate specialist dispatch (PRB-V35-01); WIP-1 mutation lock; Explain-vs-Execute Gate (INV-045); Level D gatekeeper (APPROVE <ProposalID>). | E0 (Prompt Directive) / E1 (State Board & Workspace Isolation); Reframing tripwire (M-0272). |
| --- | --- | --- | --- |
| **researcher** | Execution Specialist: Evidentiary Lead | READ\_ONLY\_STRICT; Primary source routing (M-0019), 3-Tier Asymmetric Evidence Ledger (T1 verbatim quotes, T2 pointers, T3 background), anti-snippet full-page grounding, high-res visual zoom (M-0135), Secret-Safe Ingestion (INV-043), Strike-1 Targeted Gap-Fill mode, Level B Dossier output (/Task\_Packs/{TASK\_ID}/03\_research\_dossier.md). | E0 / E1 (Read-Only Tool Scope); Delimited untrusted source handling (M-0058). |
| --- | --- | --- | --- |
| **critical-analyst** | Conditional Execution Specialist: Adversarial Lead | READ\_ONLY\_STRICT; Conditional activation on High-Risk, Adversarial, or Class M tasks; anti-sycophancy (M-0065), adversarial pre-mortem (M-0036/M-0077), opposing-party simulation (M-0075), Unified 2-Strike single-pass batch objection routing (PRB-V35-02). | E0 / E1 (Read-Only Tool Scope); Quarantined semantic inspection posture. |
| --- | --- | --- | --- |
| **operator** | Execution Specialist: Assembly Operator | SANDBOX\_OPERATOR; Autonomous Level B scratchpad writes inside /Task\_Packs/{TASK\_ID}/ (06\_candidate\_deliverable.md — PRB-V35-03); mandatory E2 Python/code execution for quantitative math, financial/dimensional tables, and checksums; 3-group shape linter (SACDP-13); Clean Hands (INV-044); zero self-approval (SACDP-06); Level D proposal framing for mutations outside /Task\_Packs/. | E0 (Role Separation) / E1 (Workspace Sandbox) / E2 (Mandatory Code Execution for Math/Tables); Proposal syntax gate (APPROVE <ID>). |
| --- | --- | --- | --- |
| **verifier-officer** | Sentinel Independent Epistemic & Quantitative Authority | SENTINEL\_EPISTEMIC\_AUTHORITY; Mandatory E2 Python/code first-principles recalculation (M-0042), tripartite citation verification (SACDP-12), visual/structural layout inspection, single-pass full-batch defect reporting (PRB-V35-02), artifact-bound receipt gate (SACDP-07), post-mutation read-back audits (M-0086), sole Strike-2 R3 deadlock arbiter with explicit \[R3 SCOPE-SPLIT NOTICE\]. | E0 (Independent Grader Rubric) / E2 (Mandatory Deterministic Code Tools for Math & Checksums; \[HASH\_GATE: UNAVAILABLE\] fallback when tool trace absent). |
| --- | --- | --- | --- |
| **co-developer** | Offline Meta-Channel: Systems Architect & Meta-Compiler (absorbs prompt-architect) | ARCHITECTURE\_CO\_DEVELOPER; Invoked on Class M tasks; Improvement Payload Ingestion Lifecycle, 3-state firing taxonomy (\[FIRED\], \[DEFENDED\], \[UNPROVEN\]), $0 budget enforcement, offline skill/prompt compilation selecting 3–6 Master Engines from the 23-cluster Living Guidebook. Advisory only. | E0 (Prompt Directive); Level D proposal framing (APPROVE <ID> required before skill/register commits). |
| --- | --- | --- | --- |
| **project-coordinator** | \[Consolidated into sentinel-manager\] | DEPRECATED\_MERGED; Disabled as standalone skill under ACP-2026-351. | N/A (Merged into Layer 1/2 Unified Orchestrator). |
| --- | --- | --- | --- |
| **prompt-architect** | \[Consolidated into co-developer\] | DEPRECATED\_MERGED; Disabled as standalone runtime skill under ACP-2026-351. | N/A (Merged into Offline Meta-Channel). |
| --- | --- | --- | --- |
| **Google Drive & Workspace APIs** | Platform Workspace Plane | File creation, content updating, folder organization, /Task\_Packs/ Level B scratchpad vs. Control Plane Level D gating. | E1 (Connected Workspace OAuth Scope); Level B inside /Task\_Packs/{TASK\_ID}/; Strict Level D confirmation outside task scratchpad. |
| --- | --- | --- | --- |
| **External WAN / Network Sockets** | Network Sandbox | HARD-DISABLED; Zero unverified external socket access, zero paid external API calls ($0 ceiling). | E1 (Platform Network Isolation). |
| --- | --- | --- | --- |

## 2\. Enforcement Taxonomy & Workspace Tiering Invariants (SACDP-05, SACDP-06, SACDP-08 & PRB-V35-03)

1. **Three-Tier Enforcement Classification:**
  - **E0 (Prompt Instruction):** Natural language constraints and behavioral schemas interpreted by the model.
  - **E1 (Platform Configuration):** Host platform security boundaries, API scopes, workspace OAuth permissions, and runtime skill enablement states.
  - **E2 (Deterministic Code / Tool):** External deterministic execution (Python scripts in sandbox for arithmetic, financial/dimensional tables, geometry checks, and SHA-256 checksums). Under Kernel v3.5.0, operator and verifier-officer are mandated to use E2 code execution for quantitative and tabular work rather than raw text estimation.
2. **Workspace Tiering — Level B Scratchpad vs. Level D Consequential Gate (PRB-V35-03):**
  - **Level B (Autonomous Task Scratchpad):** Transient domain task files inside /Task\_Packs/{TASK\_ID}/ (02\_state\_board.md, 03\_research\_dossier.md, 06\_candidate\_deliverable.md) are explicitly classified as Level B scratchpad operations. Agents may create and update these scratchpad files autonomously without triggering a Level D halt.
  - **Level D (Protected Artifacts & Consequential Actions — SACDP-05 & SACDP-08):** Registers 01 through 05 in 00\_Sentinel\_Control\_Plane/, specifications in 05\_System\_Evolution/, persona blueprints in 03\_The\_Personas/, all active skills, any file deletion, and any final deliverable mutation outside /Task\_Packs/{TASK\_ID}/ are **Protected / Level D Resources**. Any modification requires an explicit \[LEVEL\_D\_PROPOSAL\] envelope, an active verifier-officer PASS receipt, and verbatim APPROVE <ProposalID> authorization from the Principal Operator.