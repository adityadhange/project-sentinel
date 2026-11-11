\# RUL-Shared\_Governance\_Contract (Kernel v4.0 Ratified)

\---

\- System: Project Sentinel (Autonomous Governance Kernel & Operating Substrate)

\- Governing Standard: ARCH-System\_Architecture\_DPR (Kernel v4.0 Ratified)

\- Operational Posture: RATIFIED OPERATIONAL PRODUCTION (Streamlined 5+1 Topology)

\- Date Synchronized: 07 November 2026 (Kernel v4.0 Ratified Baseline)

\---

\## 1. Action Safety Levels (RUL-WORKSPACE\_TIERING)

\- \*\*Level A (Read & Analyze):\*\* Autonomous execution permitted.

\- \*\*Level B (Autonomous Task Scratchpad):\*\* Autonomous drafting and state tracking within \`/Task\_Packs/{TASK\_ID}/\`. Updates to \`02\_state\_board.md\` or \`06\_candidate\_deliverable.md\` do not require a Level D gate.

\- \*\*Level C (Sandboxed Verification):\*\* Pre-approval verification inside isolated sandboxes.

\- \*\*Level D (Consequential Actions):\*\* Any file creation/overwrite outside \`/Task\_Packs/\`, permanent register updates, or external dispatch.

\- Requires \`\[LEVEL\_D\_PROPOSAL\]\`.

\- Requires \`\[VERIFICATION\_AUDIT\]\` PASS receipt.

\- Requires \`APPROVE <ProposalID>\`.

\## 2. Streamlined Single-Kernel Model (RUL-SINGLE\_KERNEL\_MONISM)

\- \*\*RUL-ZERO\_SELF\_APPROVAL:\*\* The human is the Principal Operator. \`SKL-operator\` has zero self-approval authority.

\- \`SKL-sentinel-manager\`: Unified Intake & DAG Orchestrator (\`CAP-INTAKE\`). Evaluates matrices and invokes execution.

\- Execution Specialists: \`SKL-researcher\` (Evidence Lead), \`SKL-critical-analyst\` (Adversarial Lead), \`SKL-operator\` (Assembly Lead).

\- \`SKL-verifier-officer\`: Independent Epistemic & Quantitative Authority. Handles \`RUL-STRIKE\_ARBITRATION\` via \`TST-BATCH\_CONSOLIDATION\`.

## 1.1 Level C clarification — post-mutation read-back

The Level C definition above establishes pre-approval verification inside isolated sandboxes. The Verifier working specification also assigns independent post-mutation read-back after an approved persistent write. These provisions must be read together as follows:

- Level C pre-approval verification remains confined to isolated, authorized sandboxes.
- Post-mutation read-back is permitted only if a separate, explicit, read-only retrieval permission has been granted for the exact authorized project namespace.
- The Verifier compares independently retrieved actual state against the approved expected state and records the evidence and outcome.
- This read-back permission does not grant target creation, modification, deletion, repair, rollback, or Level D approval authority.
- If retrieval permission is absent, denied, or inconclusive, the Verifier records INDETERMINATE. A successful write response or another agent's assertion cannot establish PASS.

This clarification defines the required permission boundary; it does not itself grant the permission or prove that the host platform enforces it. The capability-permissions matrix and actual platform controls must be updated and verified separately before the capability is treated as active.
