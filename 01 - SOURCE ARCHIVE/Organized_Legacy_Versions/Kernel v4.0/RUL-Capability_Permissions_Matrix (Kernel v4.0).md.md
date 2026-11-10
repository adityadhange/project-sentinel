\# RUL-Capability\_Permissions\_Matrix (Kernel v4.0 Ratified)

\---

\- Project: Project Sentinel (Governance Kernel) & Project Optimus (Execution Fleet)

\- Governing Standard: ARCH-System\_Architecture\_DPR (Kernel v4.0 Ratified)

\- Security Model: Three-Tier Enforcement Taxonomy (E0 / E1 / E2) & Level B / Level D Tiering

\- Date Synchronized: 07 November 2026 (Kernel v4.0 Ratified Baseline)

\---

\## 1. Runtime Capability & Security Separation Matrix

| \*\*Subsystem / Persona\*\* | \*\*Capability Class & Permissions\*\* | \*\*Enforcement Tier & Boundary\*\* |

| :--- | :--- | :--- |

| \*\*\`SKL-sentinel-manager\`\*\* | SENTINEL\_INTAKE\_ORCHESTRATOR. Class A/B/C/E/F/M triage. DAG compilation (\`CAP-INTAKE\`). WIP-1 mutation lock. Level D gatekeeper (\`APPROVE <ProposalID>\`). | E0 / E1. Enforces \`RUL-SINGLE\_KERNEL\_MONISM\` and \`RUL-WORKSPACE\_TIERING\`. |

| \*\*\`SKL-researcher\`\*\* | READ\_ONLY\_STRICT. Asymmetric Evidence Ledger (\`MTH-3\_TIER\_LEDGER\`), High-res zoom (\`MTH-VISUAL\_ZOOM\`). | E0 / E1 (Read-Only). |

| \*\*\`SKL-critical-analyst\`\*\* | READ\_ONLY\_STRICT. Opposing-party simulation (\`MTH-OPPOSING\_PARTY\`), adversarial pre-mortem (\`CAP-ADVERSARIAL\_PROBE\`). | E0 / E1 (Read-Only Sandbox). |

| \*\*\`SKL-operator\`\*\* | SANDBOX\_OPERATOR. Autonomous Level B scratchpad writes. Mandatory E2 Python execution for math (\`CAP-DETERMINISTIC\_COMPUTATION\`). Level D proposal framing. | E1 (Workspace Sandbox) / E2 (Mandatory Code Tools). Restricted by \`RUL-ZERO\_SELF\_APPROVAL\`. |

| \*\*\`SKL-verifier-officer\`\*\* | SENTINEL\_EPISTEMIC\_AUTHORITY. E2 recalculations, tripartite citation verification, single-pass defect reporting (\`TST-BATCH\_CONSOLIDATION\`). | E2 (Code Tools). Sole arbiter for \`RUL-STRIKE\_ARBITRATION\`. |

| \*\*\`SKL-co-developer\`\*\* | ARCHITECTURE\_CO\_DEVELOPER (Offline). | Advisory / M-Class proposals. |

## 2.1 Verifier read-back permission clarification

The `SKL-verifier-officer` row above assigns E2 recalculation, tripartite citation verification, single-pass defect reporting, and sole arbitration authority. The v4.0 Verifier working specification also assigns independent post-mutation read-back responsibility.

**Permission gap:** The row does not expressly grant the independent, read-only retrieval capability required to perform that responsibility. Until separately authorized and enforced, post-mutation retrieval is a defined responsibility with an unresolved platform permission prerequisite; it must not be represented as an active capability.

The intended permission, if approved, is limited to retrieving and inspecting resulting target state within an explicitly authorized project namespace. It grants no create, modify, delete, repair, rollback, or Level D approval authority. A matrix statement alone does not provision or prove host-side enforcement.
