# **DETAILED PROJECT REPORT (DPR): PROJECT OPTIMUS & PROJECT SENTINEL (KERNEL V3.2.0 RECONCILED)**

**Autonomous Personal AI Coworker Fleet, Meta-Compiler & Deterministic Behavioral Governance Kernel**

- **Document Status:** Authoritative Standalone Presentation & Audit Specification \[VERIFIED COMPLETE\]
- **Governing Standard:** Project Sentinel Kernel v3.2.0 (Deterministic Runtime Baseline) & Master Roadmap v3.0 \[VERIFIED COMPLETE\]
- **System Principal & Chief Architect:** Aditya Vijay Dhange (Solapur, Maharashtra, India) \[REPORTED\]
- **Target Audience:** External AI Expert / Principal Systems Architect (Zero-File-Access Self-Explanatory Edition) \[OBSERVED\]
- **Date Synchronized:** 27 October 2026 \[VERIFIED COMPLETE\]
- **Epistemic & Verification Standard Applied:** \[FACT: PRIMARY\_VERIFIED\], \[INFERENCE: DEDUCTIVE\_VALID\], \[GAP: UNVERIFIED\_ABSTENTION\], \[REFUTED: CONTRADICTED\_BY\_SOURCE\] alongside operational audit states (\[REPORTED\], \[OBSERVED\], \[TESTED PASS\], \[VERIFIED COMPLETE\]) \[VERIFIED COMPLETE\]

## **1\. EXECUTIVE SUMMARY & FOUNDATIONAL ENGINEERING THESIS**

### **1.1 The Problem: Five Structural Failure Modes of Frontier LLMs**

While modern frontier Large Language Models (LLMs) exhibit high conversational fluency, deploying them as autonomous coworkers on long-horizon, high-consequence legal, regulatory, and engineering workflows exposes five recurring structural failure modes \[OBSERVED\]:

1. **Autoregressive Context Drift:** As session token length expands across multi-turn workflows, early negative constraints and formatting invariants suffer attention decay ("lost-in-the-middle"), causing models to silently drop critical operational rules \[OBSERVED\].
2. **Conversational Sycophancy:** Reinforcement Learning from Human Feedback (RLHF) tunes models for agreeableness. When an operator presents a flawed legal theory, an unviable statutory interpretation, or an under-dimensioned structural calculation, standard models validate the flawed premise rather than challenging it \[OBSERVED\].
3. **Silent Hallucination Under Completion Pressure:** When primary evidence is missing or ambiguous, standard models bridge evidentiary voids with plausible-sounding fabricated statutory citations, interpolated numbers, or unverified assumptions \[OBSERVED\].
4. **State Amnesia Across Session Boundaries:** Multi-stage projects collapse when context windows reset, mobile apps purge background memory, or tool calls time out—forcing the human operator to reconstruct state from scratch \[OBSERVED\].
5. **Payload Contamination:** When high-density domain workflows (such as environmental litigation or consumer disputes) are processed in long threads, domain-specific facts bleed into the agent's system identity, distorting its general operating rules and corrupting reusable prompt templates \[OBSERVED\].

### **1.2 The Architectural Solution: Project Sentinel & Project Optimus**

To eliminate these five failure modes without relying on fragile single-prompt monoliths, the system is engineered as a strictly decoupled dual-engine architecture \[VERIFIED COMPLETE\]:

- **Project Sentinel (The Governance, Invariant & Safety Kernel):** A deterministic behavioral governance engine comprising **261 Unified Master Engines** and **919 Consolidated Operational Variants** organized across **23 Functional Clusters** and **5 Thematic Guidebook Buckets** (plus **1,560 staged proposed mechanism definitions** in quarantined research registries). Project Sentinel enforces hard epistemic truth floors, anti-sycophancy mandates, untrusted data quarantine envelopes, and human-in-the-loop approval gates \[VERIFIED COMPLETE\].
- **Project Optimus (The Multi-Agent Orchestration, Meta-Compiler & Control Plane Engine):** A 4-layer hierarchical execution fleet of **7 specialized native runtime agent skills** backed by a persistent **5-Register Google Drive Control Plane**. Rather than stuffing hundreds of rules into a single prompt, Optimus uses a **Meta-Compiler (prompt-architect)** to dynamically assemble lean, task-specific sub-agent prompts containing only **3 to 6 canonical Master Engines** per role, coordinated via externalized state boards (\[STATE\_BOARD\]) \[VERIFIED COMPLETE\].

### **1.3 Principal Operator Context & Real-World Operational Mandate**

The system is engineered and operated by **Aditya Vijay Dhange**, operating out of Solapur, Maharashtra, India \[REPORTED\]. Acting as a solo practitioner and authorized representative across family enterprises (**A V Dhange Associates** and **Visons Gallery**) as well as citizen-led public interest environmental litigation, the operator handles complex statutory, regulatory, and engineering workloads without a traditional staff of junior associates, paralegals, or drafting clerks \[REPORTED\].

Project Sentinel and Project Optimus function as an institutional-grade personal AI team handling:

- **Statutory & Technical Corpus Ingestion:** Auditing hundreds of pages of municipal engineering manuals (such as CPHEEO storm water drainage manuals) and statutory notifications (Water Act 1974, Environment Impact Assessment Notification 2006) to pinpoint actionable violations \[REPORTED\].
- **Adversarial Legal & Regulatory Drafting:** Preparing formal pleadings for the National Green Tribunal (NGT) and statutory notices under the Consumer Protection Act, 2019 (CPA 2019) with 100% citation traceability \[REPORTED\].
- **Parametric Engineering & CAD Verification:** Auditing millimetric board breakdowns, beam-deflection physics, and OpenSCAD 3D parametric scripts for architectural woodworking, alongside bezier vector geometry for OEM-style automotive/motorcycle graphics \[REPORTED\].

### **1.4 Real-Life Criteria for System Success**

Success is measured by four non-negotiable operational benchmarks rather than conversational eloquence \[OBSERVED\]:

1. **Zero Fabricated Claims:** Every affirmative claim in a legal brief or technical report is machine-validated against primary sources (\[FACT: PRIMARY\_VERIFIED\]) or deductively derived (\[INFERENCE: DEDUCTIVE\_VALID\]). Missing data forces an explicit halt/placeholder (\[GAP: UNVERIFIED\_ABSTENTION\]) \[VERIFIED COMPLETE\].
2. **Zero Unconsented Consequential Actions:** The system never overwrites/deletes a file, dispatches external communications, or mutates a core skill without halting and presenting a formal **Level D Proposal Envelope** containing the exact diff, irreversible consequence, and rollback path \[VERIFIED COMPLETE\].
3. **Session Interruption Immunity:** If a session terminates mid-workflow, a newly initialized session reads the persistent Google Drive registers and portable \[STATE\_BOARD\] checkpoints to resume execution at the exact pending step with zero state loss \[TESTED PASS\].
4. **Structural Anti-Sycophancy:** Dedicated adversarial role separation ensures the system actively stress-tests and dismantles weak operator premises before any deliverable is drafted \[VERIFIED COMPLETE\].

## **2\. ARCHITECTURAL BIFURCATION: CORE SYSTEM PLANE VS. EPHEMERAL TASK PAYLOADS**

### **2.1 The System vs. Payload Decoupling Invariant (M-0001 & M-0130 / DEC-004)**

A foundational architectural law of Project Sentinel is the **Strict System vs. Task Payload Decoupling Invariant**. In standard LLM setups, domain case facts (such as specific municipal drainage litigation details) are often hardcoded into system prompts, turning a general-purpose architecture into a brittle, single-use chatbot.

Under M-0001 and M-0130, the operating environment is permanently bifurcated into two strictly isolated planes \[VERIFIED COMPLETE\]:

+---------------------------------------------------------------------------------------------------+

| OPERATING ENVIRONMENT TAXONOMY |

+---------------------------------------------------------------------------------------------------+

| PLANE 1: CORE SYSTEM PLANE (Permanent, Domain-Agnostic Architecture) |

| ├── Governance Kernel (Project Sentinel: 261 Active Master Engines / 919 Variants / 5 Buckets) |

| ├── Orchestration & Meta-Compiler Fleet (Project Optimus: 7 Native Runtime Agent Skills) |

| └── Durable Workspace Control Plane (5 Master Google Drive Registers & Deterministic Contracts) |

+---------------------------------------------------------------------------------------------------+

| PLANE 2: EPHEMERAL TASK PAYLOADS (Transient, Quarantined Case Envelopes — \[TASK\_PAYLOAD: <ID>\]) |

| ├── \[PAYLOAD: NGT\_SMC\_DRAINAGE\_2026\] (Environmental Public Interest Litigation) |

| ├── \[PAYLOAD: LIVPURE\_CONSUMER\_2026\] (CPA 2019 Product Liability & Deficiency Notices) |

| ├── \[PAYLOAD: MG\_HECTOR\_DISPUTE\_2026\] (Automotive Undisclosed Feature Deletion Escalation) |

| ├── \[PAYLOAD: WOODWORKING\_CAD\_2026\] (OpenSCAD Parametric Furniture & Structural Mechanics) |

| └── \[PAYLOAD: RE\_THUNDERBIRD\_VECTOR\] (Scale SVG Vector Decals & OEM Badging Geometry) |

+---------------------------------------------------------------------------------------------------+

### **2.2 Ephemeral Payload Domains & Representative Workloads**

| Payload Domain | Classification | Scope & Technical Rigor Required | Representative Operator Directive |
| --- | --- | --- | --- |
| **1\. Environmental Public Interest Litigation** | Ephemeral Payload (\[TASK\_PAYLOAD\]) | NGT Western Zone Bench petitions, urban hydrology, storm water nala concretization, CPHEEO Manual & MoEFCC EIA 2006 statutory compliance \[REPORTED\]. | *"Review the Municipal Corporation drainage DPR against Chapter 3 of the CPHEEO Manual. Identify every clause where natural soil percolation was eliminated without hydrogeological justification and draft an evidentiary comparison table."* |
| --- | --- | --- | --- |
| **2\. Consumer Rights & Statutory Advocacy** | Ephemeral Payload (\[TASK\_PAYLOAD\]) | Consumer Protection Act 2019 notices, e-Daakhil pleadings, warranty breach audits, statutory interest calculations \[REPORTED\]. | *"Analyze the sales prospectus for the MG Hector Plus 7 Sharp Pro MT against our delivery checklist. Draft a Section 35 CPA 2019 notice detailing undisclosed feature deletions, citing exact dealer correspondence."* |
| --- | --- | --- | --- |
| **3\. Parametric 3D CAD & Structural Joinery** | Ephemeral Payload (\[TASK\_PAYLOAD\]) | Millimetric timber cut sheets, carcass joinery clearances, beam-deflection ("Sagulator") math, OpenSCAD parametric code \[REPORTED\]. | *"Write a parametric OpenSCAD script for a 4-foot plywood study desk with overhead hutch. Account for 18mm nominal thickness (calipered at 17.4mm), knockdown fastener clearances, and output a verified cut schedule."* |
| --- | --- | --- | --- |
| **4\. Automotive & Motorcycle Vector Graphics** | Ephemeral Payload (\[TASK\_PAYLOAD\]) | SVG bezier path generation, pinstripe offset geometry, OEM-inspired metallic gold/charcoal/bronze decal masks \[REPORTED\]. | *"Generate isolated SVG path coordinates for a geometric tank emblem with pinstripe offsets matching a 19-liter Royal Enfield Thunderbird 350 fuel tank with exportable vinyl cutter dimensions."* |
| --- | --- | --- | --- |
| **5\. Prompt Architecture & Kernel Compilation** | Core System Plane Interaction | Auditing mechanism cards, subtractive refactoring (M-0338), compiling zero-waste specialist skills, running regression vectors \[VERIFIED COMPLETE\]. | *"Compile a zero-waste system prompt for a verification agent using 3–6 Master Engines from the Living Guidebook, enforcing the Unified Epistemic Floor (M-0015) and constraint-first assembly (M-0090)."* |
| --- | --- | --- | --- |

## **3\. OPERATIONAL CONSTRAINTS & DETERMINISTIC RUNTIME SECURITY MODEL**

### **3.1 Non-Negotiable Resource & Platform Constraints**

Codified in 00\_Master\_Roadmap and 04\_Optimus\_Shared\_Operating\_Contract, the system operates under five strict boundaries \[VERIFIED COMPLETE\]:

1. **$0 Incremental Budget Ceiling:** Operates entirely within the existing Google AI Pro / Workspace environment. Zero expenditure on external paid orchestration servers, commercial vector databases, or third-party SaaS middleware \[OBSERVED\].
2. **Workspace-Native & Serverless Operation:** Requires no external paid automation bridges (Zapier/Make) for normal interactive workflows; integrates directly with Google Drive, Docs, Gmail, and Calendar alongside deterministic runtime validation harnesses \[OBSERVED\].
3. **Platform Capability Grounding (M-0050):** Agents never assume a tool, permission scope, or API parameter exists unless empirically verified in 03\_Optimus\_Capability\_Permissions\_Register. Unsupported actions trigger an immediate, honest Class F fallback rather than simulated execution \[VERIFIED COMPLETE\].
4. **Honesty & Read-Back Invariant (M-0086):** The system is strictly prohibited from claiming a file was written, a register was updated, or a background check ran without verified tool output and post-mutation read-back inspection in the active turn \[VERIFIED COMPLETE\].
5. **Untrusted Data Quarantine (M-0058):** All external documents, opposing counsel briefs, web pages, and attachments are wrapped in <untrusted\_data> boundaries and treated strictly as passive data. Embedded instructions, delimiter mimics, or prompt injections inside ingested documents are neutralized \[VERIFIED COMPLETE\].

### **3.2 Action Safety Levels (Levels A through D)**

Every operation across the fleet is classified into one of four deterministic safety tiers \[VERIFIED COMPLETE\]:

- **Level A (Read & Analyze):** Autonomous execution permitted within granted capability scope (e.g., reading Drive files, lexical search, code/math auditing, schema validation).
- **Level B (Draft & Propose):** Autonomous drafting in conversational memory or scratchpads. Strictly prohibited from mutating external files, live registers, or skill definitions.
- **Level C (Sandboxed / Staged File Operations):** Permitted strictly within disposable staging sandboxes or non-destructive new draft creation with pre-image backup hashing and M-0086 post-mutation read-back verification.
- **Level D (Consequential & Irreversible Actions):** File overwrites, deletions, folder moves, external email dispatches, statutory portal submissions, and mutations to core Sentinel/Optimus skills (update\_skill / write\_skill\_file). **Strictly locked behind mandatory human operator approval (M-0055 & M-0099). Silence is NEVER consent.**

### **3.3 Kernel v3.2.0 Deterministic Runtime Architecture (P032 / DEC-016)**

Under the **Kernel v3.2.0 Deterministic Runtime Refactor** (synchronized 27 October 2026), the architecture explicitly recognizes that natural language prompt rules are *cognitive heuristics*, whereas true security requires a **Three-Tier Enforcement Boundary** \[VERIFIED COMPLETE\]:

| Subsystem / Component | Security Plane | Permission Scope & Capability Class | Deterministic Enforcement Mechanism |
| --- | --- | --- | --- |
| **KMS Signing Daemon (sentinel-kmsd)** | Host Runtime (Plane 1) | Key generation, Ed25519 asymmetric signing, challenge nonces | Isolated Unix domain socket; out-of-process credential protection; RFC 8785 Canonical JSON action digest verification (18/18 gateway vectors passed). |
| --- | --- | --- | --- |
| **Transactional WAL & File Driver** | Host Runtime (Plane 1) | Atomic write, fdatasync, renameat2, openat2 descriptor isolation | Linux kernel directory descriptor anchoring (RESOLVE\_BENEATH); Two-Phase Crash-Resilient Write Pipeline (PREPARED → M-0086 byte-exact read-back → COMMITTED; 16/16 crash vectors passed). |
| --- | --- | --- | --- |
| **Google Drive & Docs APIs** | Platform (Plane 1) | File creation, metadata reading, folder hierarchy reorganization | Scoped OAuth tokens; Level D human approval required for moves, overwrites, or core register updates. |
| --- | --- | --- | --- |
| **Researcher Subagent** | Execution Fleet (Plane 2) | READ\_ONLY strictly; primary document & statutory ingestion | Capability class token lockdown; tool gateway blocks all mutation verbs. |
| --- | --- | --- | --- |
| **Operator Subagent** | Execution Fleet (Plane 2) | Sandboxed file staging; coordinate-free surgical patching (M-0020) | Locked behind Level D Consequential Action Proposal Envelope (M-0099) & single-use capability tokens (CAP-\*). |
| --- | --- | --- | --- |
| **Verifier Officer Subagent** | Execution Fleet (Plane 2) | Independent post-mutation read-back (M-0086), math & citation verification | Read-only inspection; non-bypassable completion assertion gate & Pydantic Claim Registry filter (M-0015). |
| --- | --- | --- | --- |
| **External WAN / Sockets** | Network Sandbox | **HARD-DISABLED** (for sandboxed code execution) | Host network namespace isolation; unauthorized external egress dropped. |
| --- | --- | --- | --- |

**Capability Issuance & Lease Invariants:**

- **Single-Use Capability Tokens (CAP-\*):** Minted under SERIALIZABLE isolation and consumed atomically during mutation preparation.
- **Coordinator Lease Margin:** The tool gateway requires an active coordinator lease margin of greater than 5,000 ms prior to executing any physical write.
- **Epistemic Precondition Gate:** Capability tokens for mutations cannot be issued unless supporting claims have passed M-0015 schema validation.

## **4\. MULTI-AGENT ORCHESTRATION HIERARCHY & THE 7 NATIVE AGENT SKILLS**

### **4.1 4-Layer Orchestration Topology**

Project Optimus replaces monolithic prompting with a **Dispatcher-Specialist Separation of Duties (M-0014)**. Orchestrators decompose, route, and track state, while domain specialists execute isolated cognitive stages \[VERIFIED COMPLETE\]:

\[Layer 1: Chief of Staff & Intake\] ──────► sentinel-manager

(Class A–F Triage, Long-Task Receipts M-0146, Level D Gatekeeper)

│

\[Layer 2: Project Director & State\] ─────► project-coordinator

(Tier 1–3 Selection, DAG Precedence Audit, WIP-1 Lock, \[STATE\_BOARD\])

│

\[Layer 3: Meta-Compiler Engine\] ─────► prompt-architect

(Selects 3–6 Guidebook Master Engines, Cache-Stable Prefix, RFC 8785 Hash)

│

\[Layer 4: Specialist Execution Fleet\] ───┬──────────────────────────┬──────────────────────────┐

▼ ▼ ▼

researcher critical-analyst operator

(Primary Sources, (Hostile Red-Teaming, (Surgical Assembly,

Quote Ledger \[Q#\], Opposing Counsel Sim, Coordinate-Free Diffs,

Epistemic Tagging) Back-Edge Routing) Level D Proposals)

│ │ │

└──────────────────────────┴──────────────────────────┘

│

▼

verifier-officer

(Independent Math Derivation,

Hard-Fail Rubric Gate M-0137,

Post-Mutation Read-Back M-0086)

### **4.2 Comprehensive Specification of the 7 Deployed Runtime Skills**

| Skill Name & Layer | Core Mandate & Role Boundary | Key Governing Mechanisms & Rules | Required Output Contract / Envelope |
| --- | --- | --- | --- |
| **sentinel-manager** (Layer 1 — Chief of Staff) | Normal user-facing entry point. Classifies requests into Classes A–F, handles simple tasks directly, routes complex work to planning, enforces payload decoupling, and halts on Level D actions. | **Long-Task Receipt (M-0146):** Emits \[RECEIPT\] before workflows exceeding 3 steps. **Reframing-as-Refusal Tripwire (M-0240):** Halts if compliance requires inventing benign assumptions. **Envelope Deduplication:** Never stacks duplicate governance footers. | \[RECEIPT: action=... \| scope=... \| completion\_signal=...\] and \[SENTINEL TURN SUMMARY\] (omitted when \[STATE\_BOARD\] or \[LEVEL\_D\_PROPOSAL\] is rendered). |
| --- | --- | --- | --- |
| **project-coordinator** (Layer 2 — Project Director) | Owns multi-step execution plans, dependency graph validation, Execution Tier allocation, checkpoint persistence, and loop-breaking arbitration. | **Pairwise DAG Audit (M-0157):** Validates (Task\_A -> Task\_B) for dependency inversion and cycles. **WIP-1 Lock:** Exactly ONE task in\_progress per thread. **Bounded Ambiguity (M-0159):** Max 2 clarifying questions; explicit \[DEFAULT\_APPLIED\] or \[DATA\_GAP\] halt. **Max-1 Auto-Revision Loop Breaker.** | \--- \[STATE\_BOARD: {TASK\_ID}\] --- (Tracks Payload, Execution Tier, Active Stage, Revision Counter, Completed/Pending Milestones, Active Invariants, and Checkpoint Export readiness). |
| --- | --- | --- | --- |
| **prompt-architect** (Layer 3 — Meta-Compiler Engine) | Translates task specs into lean, deterministic sub-agent prompts using approved Master Engines from the Living Guidebook. | **Zero-Waste Lookup (M-0095):** Loads references/mechanism\_index.md and selects strictly **3 to 6 Master Engines** per compilation. **Canonical Provenance Lock (M-0122 / M-0131):** Uses only ratified M-0001–M-0340 cards; never auto-promotes M-PROP cards. **Constraint-First Layout (M-0090):** # Identity → # Instructions → # Examples → # Context. | \--- \[MISSION\_BRIEF: {TARGET\_ROLE\_OR\_SKILL}\] --- containing Why, What, Mechanisms Loaded, Compiled Prompt Body, and Verification & Test Cases (Normal, Edge, Adversarial). |
| --- | --- | --- | --- |
| **researcher** (Layer 4 — Evidentiary Specialist) | Primary-source discovery, statutory/technical extraction, verbatim quote ledger construction, and evidentiary gap disclosure. Strictly READ\_ONLY (no drafting pleadings or mutating files). | **Primary Source Routing (M-0019):** Rejects blogs/aggregators. **Two-Stage Verbatim Quote Ledger (M-0134 / M-0015):** Extracts verbatim <quotes> (\[Q1\], \[Q2\]) before <analysis>. **Sub-Region Crop & Zoom (M-0135 / M-0328):** Crops dense CAD/schematics before reading pins/dimensions. **Anti-Snippet Grounding (M-0189).** | \[RESEARCH\_DOSSIER: {TOPIC\_OR\_TASK\_ID}\] with Ingestion Mode, Confidence Floor, Primary Citations, Evidence Ledger (<quotes>), Synthesized Findings (4-Tier tagged), Refuted Claims, and Coverage Gaps. |
| --- | --- | --- | --- |
| **critical-analyst** (Layer 4 — Adversarial Red-Team) | Challenges assumptions, simulates opposing counsel/auditors, runs pre-mortem failure analysis, and routes defects to downstream owners. | **Anti-Sycophancy (M-0065 / M-0278):** Penalizes uncritical agreement. **Counterfactual Pre-Mortem (M-0036 & M-0077).** **Severity Tiers:** Fatal Defect, Procedural / Evidentiary Gap, Strategic Vulnerability, Minor / Polish. **Anti-Deadlock:** Respects Epistemic Floor; escalates conflicts to Human Arbitration. | \[CRITICAL\_ANALYSIS: {TARGET\_DELIVERABLE\_ID}\] detailing Opposing Party Simulation, Structural & Evidentiary Vulnerabilities, Latent Failure Modes, and Routed Remediations (\[ROUTE -> PHASE 2 RESEARCHER\] or \[ROUTE -> PHASE 4 OPERATOR\]). |
| --- | --- | --- | --- |
| **operator** (Layer 4 — Assembly & File Specialist) | Prepares formal deliverables, executes surgical code/text patches, enforces scope ceilings, and frames Level D approval proposals. | **Anti-Gold-Plating (M-0132 / M-0276):** Hard scope ceiling; logs extras as \[OBSERVED\_OUT\_OF\_SCOPE\]. **Surgical Patching (M-0020):** Byte-exact replacements stripped of line numbers/gutter pipes; 3-line context anchors. **Truncation Gate (M-0139 / M-0259).** **Non-Interactive CLI (M-0022).** | Deliverable drafts preserving epistemic tags and explicit \[INSERT VERIFIED PARAMETER\] placeholders, or --- \[LEVEL\_D\_PROPOSAL: {TASK\_ID}\] --- halting for explicit 'APPROVE' confirmation. |
| --- | --- | --- | --- |
| **verifier-officer** (Layer 4 — Independent Auditor) | Independent calculation verification from first principles, statutory cross-checking, lexicographic rubric gating, and post-mutation read-back validation. Never audits its own drafts. | **Independent Generator-Grader Decoupling (M-0133 / M-0180):** Ignores generator CoT; audits strictly against ground truth. **Materialized Intermediate Tables (M-0136 / M-0163).** **Hard-Fail Lexicographic Rubric (M-0137 / M-0324):** Stage 1 Binary Invariants must pass 100% before Stage 2 Quality is scored. **Multi-Dimensional Gate (M-0140 / M-0318).** | \--- \[VERIFICATION\_AUDIT: {TARGET\_DELIVERABLE\_ID}\] --- reporting Audit Result, Revision Counter, Hard-Fail Invariant Audit, Material Claims & Epistemic Grounding, Acceptance Checklist, and Gate Verdict. |
| --- | --- | --- | --- |

### **4.3 Request Triage Classes (A–F) & Selective Execution Tiers (Tiers 1–3)**

To prevent multi-turn latency on simple tasks while guaranteeing exhaustive rigor on high-stakes tasks, sentinel-manager and project-coordinator enforce dynamic routing \[VERIFIED COMPLETE\]:

- **Six Request Classification Fast-Paths (sentinel-manager):**
  - **Class A (Simple / Direct Task):** Handled immediately in a single turn without background coordination.
  - **Class B (Existing-Project Update):** Batch-expands project-coordinator + stage specialist(s), loads active checkpoint, and executes the next pending milestone.
  - **Class C (New Complex Project):** Batch-expands project-coordinator + researcher, initializes a Task ID, assigns an Execution Tier, and stages a \[STATE\_BOARD\].
  - **Class D (Prompt / Skill Design):** Batch-expands prompt-architect + verifier-officer, selects 3–6 Master Engines from mechanism\_index.md, and compiles a \[MISSION\_BRIEF\].
  - **Class E (Consequential Action):** Batch-expands operator, halts before execution, and emits a \[LEVEL\_D\_PROPOSAL\] envelope.
  - **Class F (Blocked or Unsupported):** Transparently reports platform limitations and provides the smallest viable manual fallback.
- **Three Selective Execution Tiers (project-coordinator):**
  - **Tier 1 (Full 6-Phase Pipeline):** For high-stakes litigation, novel engineering designs, or complex multi-party disputes. Runs: Phase 1 (Plan & Scope) → Phase 2 (Researcher Ingestion) → Phase 3 (Critical Analyst Red-Team) → Phase 4 (Operator Synthesis) → Phase 5 (Verifier Officer Audit) → Phase 6 (Level D Human Approval Gate).
  - **Tier 2 (Fast-Track Pipeline):** For routine replies, bounded updates, or tasks with pre-verified legal/technical premises. Skips adversarial simulation to conserve tokens: Phase 1 (Plan) → Phase 2 (Researcher) → Phase 4 (Operator) → Phase 5 (Verifier).
  - **Tier 3 (Audit-Only Pipeline):** For stress-testing and verifying existing user-supplied drafts, spreadsheets, or OpenSCAD scripts: Phase 3 (Critical Analyst) → Phase 5 (Verifier).
- **Critical Workflow Control Loops:**
  - **Phase 3-to-Phase 2 Back-Edge Rule:** If critical-analyst in Phase 3 uncovers a Procedural / Evidentiary Gap (\[GAP: UNVERIFIED\_ABSTENTION\]) requiring new primary sources, the coordinator routes **backward** directly to Phase 2 (Researcher) in Targeted Gap-Fill Mode rather than allowing operator to guess or search unverified sources.
  - **Max-1 Auto-Revision Loop Breaker:** If a deliverable fails critique or verification once, it routes back for a single targeted revision (Revision Counter = 1). If it fails a **second time**, or if critical-analyst (strategic posture) and verifier-officer (epistemic floor) issue conflicting demands, automated looping halts immediately (ARBITRATION REQUIRED) and escalates to the human operator with a side-by-side Arbitration Brief.

## **5\. THE LIVING GUIDEBOOK & SUBTRACTIVE KERNEL EVOLUTION**

### **5.1 Unified 4-Tier Epistemic Truth Floor (M-0015)**

Every specialist agent in Project Sentinel is bound by M-0015 (Unified Epistemic Truth, Citation & Closed-Context Floor). No material claim can exist without one of four explicit machine-auditable tags \[VERIFIED COMPLETE\]:

1. **\[FACT: PRIMARY\_VERIFIED\]:** Explicitly stated in an authoritative primary source (statute, gazette notification, court order, engineering standard, or verified workspace record) with an exact section/clause citation and verbatim quote reference (\[Q#\]).
2. **\[INFERENCE: DEDUCTIVE\_VALID\]:** Logically deduced from one or more \[FACT: PRIMARY\_VERIFIED\] premises; requires explicitly stating the underlying verified premise(s) and the deductive step.
3. **\[GAP: UNVERIFIED\_ABSTENTION\]:** Missing from accessible primary records; requires human investigation, Right to Information (RTI) discovery, or physical caliper measurement. Agents are strictly forbidden from bridging a \[GAP\] with plausible speculation and must render it as a visible placeholder (\[INSERT VERIFIED PARAMETER: ...\]).
4. **\[REFUTED: CONTRADICTED\_BY\_SOURCE\]:** Directly contradicted by authoritative primary text, empirical log, or first-principles mathematical calculation. Automatically scrubbed from affirmative drafts.

### **5.2 Evolution of the Governance Kernel & Subtractive Refactoring (M-0338)**

A major engineering insight during Project Sentinel's development was that continuously adding micro-rules creates instruction bloat and attention dilution. Under the **Subtractive Kernel Refactoring Invariant (M-0338)**, overlapping micro-cards are systematically merged into unified **Master Engines** \[VERIFIED COMPLETE\]:

| Kernel Version & Milestone | Date | Architectural Milestone & Corpus Metrics |
| --- | --- | --- |
| **Kernel v1.8 (Legacy Baseline)** | Early Oct 2026 | Monolithic markdown prompts and initial persona drafts (subsequently quarantined in 00\_Archive\_Legacy). |
| --- | --- | --- |
| **Kernel v2.3.6 (Roadmap v2.1)** | 21 Oct 2026 | Codified 89 Canonical Mechanism Cards across 5 thematic Guidebook Buckets; deployed all 7 native skills and 5 Master Control Plane Registers (P000–P026). |
| --- | --- | --- |
| **Kernel v3.0 (P027 / DEC-011)** | 26 Oct 2026 | Elevated Control Plane to 297 Canonical Mechanisms, Dynamic Ephemeral Swarms, and Stigmergic State Boards (M-0123). |
| --- | --- | --- |
| **Kernel v2.8.0 Corpus Ingestion (P028)** | 26 Oct 2026 | Full 342-Card Mechanism Corpus Ingestion (M-0001 to M-0340). Promoted 43 Master Engines (M-0298–M-0340), cataloged 840 operational variants, and staged 22 reference proposals. |
| --- | --- | --- |
| **Kernel v3.1.0 Subtractive Refactor (P029–P031 / DEC-013–015)** | 26–27 Oct 2026 | Executed 3 Subtractive Refactoring Passes pursuant to M-0338. Consolidated 102 fragmented micro-cards into **23 Functional Master Engine Clusters**, establishing a lean canonical baseline of **261 Active Master Engines** and **919 Consolidated Operational Variants**, plus **1,560 staged proposed mechanism definitions** in quarantined reference files (proposed\_core\_techniques.md and proposed\_mechanisms.md). |
| --- | --- | --- |
| **Kernel v3.2.0 Deterministic Runtime (P032 / DEC-016)** | 27 Oct 2026 | Implemented 3-tier enforcement boundary, transactional WAL + crash recovery reconciler (16/16 vectors passed), KMS Ed25519 RFC 8785 signing (18/18 vectors passed), Pydantic Claim Registry (M-0015), and Stage 3-C Canary Mutation (TSK-CANARY-MUTATION-001) with byte-exact read-back (M-0086). |
| --- | --- | --- |

### **5.3 The 5 Thematic Buckets of 02\_The\_Living\_Guidebook**

The canonical index (M-0001 through M-0340) is structured across five functional buckets \[VERIFIED COMPLETE\]:

1. **Bucket 1 — Directives, Identity & Orchestration:** Governs system vs. payload decoupling (M-0001), autonomous sovereignty (M-0005), dispatcher-specialist separation (M-0014), weighted arbitration (M-0135), truth-precedence ladders (M-0136), long-task receipts (M-0146), and phase-aware posture switching (M-0148 / M-0304).
2. **Bucket 2 — Cognitive Logic, Reasoning & Verification:** Governs observe-before-mutate gates (M-0150), staged generate-audit-refine lifecycles (M-0151), DAG task sequencing & WIP-1 locks (M-0157), tiered ambiguity triage (M-0159), materialized intermediate-state tables (M-0163), independent generator-grader decoupling (M-0180), and computation tool escalation (M-0300).
3. **Bucket 3 — Context & Data Ingestion:** Governs zero-recovery single-pass ingestion (M-0184), chrono-inverted ingestion (M-0185: PARSE\_CONTENT → LOAD\_CONTEXT → READ\_QUERY → ANSWER to prevent anchoring bias), tiered repository reconnaissance (M-0189), phase-budgeted token reservation (M-0308: max 15% scoping, max 65% generation, 20% locked verification reserve), and triadic scope specification (M-0329).
4. **Bucket 4 — Output Architecture & Constraints:** Governs unified surgical code patching (M-0020), constraint-first prompt assembly (M-0090), complete-asset emission with zero placeholders (M-0206), programmatic JSON schema validation & backward substring scanning (M-0209), structural output bounding (M-0228), typographic normalization (M-0270), spreadsheet formula reactivity (M-0271), and direct output delivery envelopes (M-0277).
5. **Bucket 5 — Safety, Guardrails & Kernel Policy:** Governs core skill mutation gates (M-0052), Level D consequential action gating (M-0055 & M-0099), multiplexed injection quarantine (M-0058), post-mutation read-back verification (M-0086), system prompt leak screening (M-0242), secret-safe execution (M-0247), truncation detection (M-0259), refusal decoupling (M-0272), bounded 3-cycle strategy rotation (M-0280), and anti-lockdown operator sovereignty (M-0299).

### **5.4 Complete Reference of the 23 Consolidated Master Engine Clusters (Kernel v3.1.0 / v3.2.0)**

For the reviewing AI expert, the table below details all **23 Consolidated Master Engine Clusters** stored in references/consolidated\_parent\_mechanisms.md that power the prompt-architect Meta-Compiler \[VERIFIED COMPLETE\]:

| Cluster # | Master Engine ID & Title | Merged Constituent Cards | Consolidated Engineering Directive |
| --- | --- | --- | --- |
| **Cluster 1** | **M-0020** — Unified Surgical Code Patching & Block Integrity | M-0020, M-0061, M-0062, M-0066, M-0204, M-0205 | Byte-exact search/replace stripped of line numbers/gutter pipes; 3-line contextual anchors; literal // ... existing code ... markers; unique match verification (=1); re-authorization if rewrite exceeds 50%. |
| --- | --- | --- | --- |
| **Cluster 2** | **M-0015** — Unified Epistemic Truth, Citation & Closed-Context Floor | M-0015, M-0031, M-0200, M-0335 | Enforces 4-tier epistemic tags (FACT, INFERENCE, GAP, REFUTED); bans plausible gap-bridging; mandates two-stage Verbatim Quote Ledgers; deterministic NOT\_IN\_SOURCES fallback on missing RAG context. |
| --- | --- | --- | --- |
| **Cluster 3** | **M-0022** — Non-Interactive Headless Shell, Terminal & Package Discipline | M-0022, M-0251, M-0269, M-0340 | Injects GIT\_PAGER=cat, --no-pager, -y; bans stream editing (sed -i, echo >, cat <<EOF) & destructive commands; locks package manifests. |
| --- | --- | --- | --- |
| **Cluster 4** | **M-0180** — Independent Generator-Grader Decoupling & Objective Auditing | M-0133, M-0180, M-0257 | Strips generator CoT/scratchpads from verification contexts; mandates evaluation solely against raw ground truth, statutory texts, and test assertions. |
| --- | --- | --- | --- |
| **Cluster 5** | **M-0055** — Level D Consequential Action Gating & Human Approval Envelopes | M-0055, M-0099, M-0256 | Halts execution prior to permanent file overwrites, deletions, external submissions, or skill mutations; presents a proposal envelope; requires explicit operator sign-off. |
| --- | --- | --- | --- |
| **Cluster 6** | **M-0123** — Stigmergic State Board Persistence & Session Recovery | M-0071, M-0086, M-0123, M-0339 | Maintains structured \[STATE\_BOARD\] blocks at milestone boundaries; forces independent read-back verification (M-0086) after file writes; enables 100% resume after session resets. |
| --- | --- | --- | --- |
| **Cluster 7** | **M-0324** — Lexicographic Hard-Fail Rubric Gating & Quality Standard | M-0093, M-0137, M-0318, M-0324 | Evaluates deliverables via strict lexicographic precedence (Safety/Invariants > Completeness > Style); any Tier 1 failure assigns score 0 immediately; requires score at least 4 per independent axis without averaging. |
| --- | --- | --- | --- |
| **Cluster 8** | **M-0328** — Empirical Multimodal Inspection & Visual Debugging Standard | M-0080, M-0084, M-0196, M-0197, M-0198, M-0328 | Explicit channel mapping across text and vision; bans guessing UI/CSS layout bugs or inferring visual correctness from exit code 0; mandates programmatic crop, zoom, and DOM inspection before fixes. |
| --- | --- | --- | --- |
| **Cluster 9** | **M-0308** — Phase-Budgeted Token Reservation & Adaptive Compression Standard | M-0128, M-0199, M-0282, M-0308 | Partitions output budget into non-negotiable reserves (up to 15% scoping, up to 65% generation, 20% locked verification reserve); triggers dense tabular compression at 90% budget; re-anchors invariants over deep context. |
| --- | --- | --- | --- |
| **Cluster 10** | **M-0157** — Directed Acyclic Task-Graph Sequencing & WIP-1 Concurrency Lock | M-0070, M-0141, M-0157, M-0158 | Decomposes goals into directed acyclic graphs (DAGs); conducts pre-dispatch pairwise audits for dependency inversion and cycles; enforces single-item work-in-progress (WIP-1) lock per active thread. |
| --- | --- | --- | --- |
| **Cluster 11** | **M-0058** — Multiplexed Delimited Control Plane & Injection Quarantine | M-0058, M-0127, M-0138, M-0310 | Separates supervisory commands (>>, /, {...}) from passive data; wraps external uploads/web content in <untrusted\_data> envelopes; neutralizes delimiter mimics and jailbreak triggers. |
| --- | --- | --- | --- |
| **Cluster 12** | **M-0159** — Tiered Ambiguity Triage, Interrogation Gating & Bounded Defaults | M-0143, M-0159, M-0160, M-0283 | Audits input ambiguity across 5 axes: if more than 2 critical parameters are missing, halts and asks max 1–2 questions; if 2 or fewer minor parameters are missing, applies explicit \[DEFAULT\_APPLIED\] inline defaults. |
| --- | --- | --- | --- |
| **Cluster 13** | **M-0005** — Autonomous Sovereignty, Tool Exhaustion & Safe-Harbor Authorization | M-0005, M-0142, M-0306, M-0323 | Enforces the autonomy ratchet: exhausts all accessible read-only discovery tools before asking the human operator for discoverable facts; pre-approves read-only inspections as safe-harbor actions. |
| --- | --- | --- | --- |
| **Cluster 14** | **M-0301** — Diagnostic Defect Freeze, Hypothesis Triage & Symptom Recovery Playbook | M-0167, M-0289, M-0301 | On Turn 1 of any bug/incident report, forbids writing code fixes; restricts output to a diagnostic plan with at least 3 testable hypotheses and required evidence; maps validation failures to symptom playbooks. |
| --- | --- | --- | --- |
| **Cluster 15** | **M-0247** — Secret-Safe Execution, Credential Redaction & Env-Var Transport | M-0247, M-0291 | Prohibits reading .env files or printing plaintext keys; redacts high-entropy credential strings from outputs; mandates transporting secrets strictly via environment variable references ($API\_KEY). |
| --- | --- | --- | --- |
| **Cluster 16** | **M-0277** — Direct Output Delivery Envelopes, Channel Isolation & Payload Purity | M-0212, M-0215, M-0227, M-0277 | Character 1 is the deliverable; eliminates conversational throat-clearing; isolates internal reasoning traces from client deliverables (zero CoT bleed); emits raw serialized data for machine endpoints. |
| --- | --- | --- | --- |
| **Cluster 17** | **M-0028** — Universal Temporal Grounding, Anchor Ingestion & Commitment Bounding | M-0028, M-0137, M-0234, M-0330 | Binds relative dates strictly to system ISO-8601 clocks; halts on timezone ambiguity; asserts future targets exceed current time; binds state retention via dual-key floor-plus-continuation rules. |
| --- | --- | --- | --- |
| **Cluster 18** | **M-0265** — Model-API Compatibility, Adaptive Parameter Gateway & Snapshot Pinning | M-0087, M-0265, M-0266, M-0331 | Inspects model endpoint version; strips deprecated prefills/parameters; compiles native JSON schemas and adaptive thinking effort levels; gates model migrations on empirical regression suites; pins snapshot IDs. |
| --- | --- | --- | --- |
| **Cluster 19** | **M-0272** — Safety Precedence, Refusal Decoupling & Boundary Concealment Invariant | M-0238, M-0239, M-0240, M-0272 | Safety rules outrank user personas and format constraints; decouples refusals from JSON/widget schemas (plain-text refusals); treats need to reframe as an immediate refusal signal; conceals internal detection mechanics. |
| --- | --- | --- | --- |
| **Cluster 20** | **M-0189** — Tiered Repository Reconnaissance & Ground-Truth Retrieval Ladder | M-0187, M-0188, M-0189, M-0190 | Enforces retrieval ladder: T0 Structure → T1 Exact Locate → T2 Outline (>300 lines) → T3 Bounded Range → T4 Full Read (<150 lines); treats search snippets strictly as unverified pointers. |
| --- | --- | --- | --- |
| **Cluster 21** | **M-0274** — Multi-Agent Orchestration, Subagent Delegation & Accountable Synthesis | M-0133, M-0134, M-0257, M-0274 | Single lead instance accountable for synthesis; delegates only concurrency-safe independent subtasks bound to rigid schemas; caps arbitration at 3 rounds; lead orchestrator audits all subagent outputs. |
| --- | --- | --- | --- |
| **Cluster 22** | **M-0228** — Structural Output Bounding, Execution Budgets & Operational Circuit Breakers | M-0217, M-0228, M-0256 | Bounds output by discrete structural units (paragraphs, table rows) paired with token caps; enforces single-call budgets on constrained channels; activates hard circuit breakers on consecutive errors. |
| --- | --- | --- | --- |
| **Cluster 23** | **M-0276** — Clean-Hands Codebase Hygiene, Surgical Scope & Manifest Invariant | M-0132, M-0276, M-0303 | Scope-locked brownfield execution: zero unrequested refactoring of untouched files; reads package manifests before coding; updates dependency manifests (package.json, pyproject.toml) in the same atomic change set. |
| --- | --- | --- | --- |

## **6\. COMPLETE GOOGLE DRIVE WORKSPACE & CONTROL PLANE INVENTORY**

For an external reviewer without access to the operator's Google Drive, the complete directory topology and file inventory inside the Project Sentinel workspace is documented below \[VERIFIED COMPLETE\]:

Project Sentinel/ (Root Workspace Folder)

│

├── Project Optimus — Personal AI Team/ (Authoritative Control Plane Directory)

│ ├── 00\_Master\_Roadmap\_v2.1 / v3.0

│ ├── 00\_Optimus\_Sentinel\_System\_Architecture\_DPR (Kernel v3.0 & v2.3.6 Standalone Specifications)

│ ├── 01\_Optimus\_Master\_Task\_Register (Kernel v3.2.0 Reconciled — Work Packages P000 to P032)

│ ├── 02\_Optimus\_Decisions\_Approval\_Ledger (Kernel v3.0 / v3.2.0 Reconciled — DEC-001 to DEC-016)

│ ├── 03\_Optimus\_Capability\_Permissions\_Register (Kernel v3.2.0 Reconciled — Security Matrix & Tokens)

│ ├── 04\_Optimus\_Shared\_Operating\_Contract (Kernel v3.2.0 Reconciled — Levels A–D & Runtime Invariants)

│ └── 05\_Optimus\_Skills\_Registry (Reconciled Fleet Specifications & Verification Benchmarks)

│

├── 01\_Bootstrapper\_Engine/

│ └── System initialization seeds, boot sequences, and environment grounding templates.

│

├── 02\_The\_Living\_Guidebook/ (Canonical Mechanism Repository)

│ ├── Master\_Index\_v2.md (Synchronized with local references/mechanism\_index.md — M-0001 to M-0340)

│ ├── Bucket\_1\_Directives\_v2.md (Directives, Identity & Orchestration Cards)

│ ├── Bucket\_2\_Cognitive\_Logic\_v2.md (Reasoning, Math Derivation & State Board Cards)

│ ├── Bucket\_3\_Context\_Ingestion\_v2.md (Primary Source Routing, RAG & Token Budgeting Cards)

│ ├── Bucket\_4\_Output\_Constraints\_v2.md (Surgical Patching, JSON Schemas & XML Layout Cards)

│ └── Bucket\_5\_Guardrails\_v2.md (Epistemic Floor, Level D Gates, Quarantine & Safety Cards)

│

├── 03\_The\_Personas/

│ └── Role archetype definitions and domain specialist behavioral overlays.

│

└── 00\_Archive\_Legacy/ (Quarantined Historical Snapshots — Isolated from Active Execution)

├── 00\_Archive\_Legacy\_v1.8/ (9 deprecated v1.8 root files quarantined under DEC-001)

├── \[SUPERSEDED\_20261026\] 00\_Optimus\_Sentinel\_System\_Architecture\_DPR

├── \[SUPERSEDED\_20261026\] 02\_Optimus\_Decisions\_Approval\_Ledger

├── To Be Deleted (Old Register Snapshots)/ (8 intermediate register snapshots quarantined under P026)

└── To Be Deleted (Old Guidebook Drafts)/ (8 intermediate guidebook drafts quarantined under P026)

**Local Runtime Skill Resource Registries (Bound to user:prompt-architect):** In addition to the Google Drive files, the active runtime houses four dense reference registries inside the prompt-architect skill directory \[VERIFIED COMPLETE\]:

1. references/mechanism\_index.md — The active canonical index (M-0001 through M-0340 / 261 Master Engines & 919 Variants).
2. references/consolidated\_parent\_mechanisms.md — Lineage mapping of all 23 Master Engine clusters merged under M-0338.
3. references/proposed\_core\_techniques.md — Staged registry of 1,418 draft mechanism rows consolidated into **538 distinct core techniques** (M-PROP-CORE-001 to M-PROP-CORE-0538) extracted from Techniques\_docx.txt (Chunks C01–C18).
4. references/proposed\_mechanisms.md — Staged registry of **142 multi-source candidate mechanisms** (DRAFT-M-C01 through C11 plus the audited 103-card batch M-PROP-0298 to M-PROP-0400, holding 22 active reference benchmark proposals).

## **7\. END-TO-END OPERATIONAL WALKTHROUGHS (3 REPRESENTATIVE PIPELINES)**

To illustrate how the 7 skills, 5 registers, and Guidebook mechanisms interact at runtime, below are three concrete end-to-end execution traces across Tiers 1, 2, and 3 \[VERIFIED COMPLETE\]:

### **7.1 Workflow 1: High-Stakes NGT Environmental Statutory Brief (Tier 1: Full 6-Phase Pipeline)**

- **Operator Prompt:** *"Prepare Section 4 (Grounds) of the NGT petition challenging Solapur Municipal Corporation's concretization of the Bhawani Peth storm water nala. Base arguments strictly on the 2024 CPHEEO drainage manual and NGT Western Zone precedents."*
- **Step 1 — Intake & Classification (sentinel-manager):** Emits a Long-Task Receipt (M-0146). Classifies the request as **Class C (New Complex Project)**, encapsulates case data inside \[TASK\_PAYLOAD: TASK-NGT-SMC-001\], and expands project-coordinator + researcher.
- **Step 2 — DAG Staging (project-coordinator):** Selects **Tier 1 (Full 6-Phase Pipeline)**, validates pairwise task dependencies (M-0157), locks WIP-1, and emits the initial \[STATE\_BOARD: TASK-NGT-SMC-001\].
- **Step 3 — Primary Evidentiary Extraction (researcher):** Operating in READ\_ONLY mode, ingests the CPHEEO Manual and NGT orders from Drive. Constructs a Two-Stage Verbatim Quote Ledger (<quotes>\[Q1\]...</quotes>). Tags verified clauses as \[FACT: PRIMARY\_VERIFIED\] (e.g., CPHEEO Manual Section 3.4.2 prohibiting impervious bed concretization in natural recharge watercourses). Identifies missing 2025 local rainfall intensity tables and flags \[GAP: UNVERIFIED\_ABSTENTION: Solapur 2025 rainfall intensity data missing from primary records\].
- **Step 4 — Hostile Stress-Testing (critical-analyst):** Simulates Senior Counsel for the Municipal Corporation (M-0075). Raises a Procedural / Evidentiary Gap: *"The Corporation will argue concretization was executed under emergency flood-mitigation powers under Section 67 of the Maharashtra Municipal Corporations Act."* Invokes the **Phase 3-to-Phase 2 Back-Edge Rule**, routing \[ROUTE -> PHASE 2 RESEARCHER (Back-Edge)\] to extract statutory limits on municipal emergency powers before any drafting occurs.
- **Step 5 — Surgical Assembly (operator):** Ingests the updated research dossier and counter-plea rebuttals. Drafts Section 4 of the NGT pleading preserving all \[FACT: PRIMARY\_VERIFIED\] citations and inserting an explicit visible placeholder \[INSERT VERIFIED PARAMETER: 2025 IMD Solapur Rainfall Data\] for the unresolved gap (M-0015).
- **Step 6 — Independent Ground-Truth Audit (verifier-officer):** Audits the draft with generator CoT stripped (M-0180). Runs Stage 1 Binary Invariant checks (M-0137 / M-0324) verifying every statutory section against the verbatim quote ledger and confirming zero silent gap-bridging. Issues \[VERIFICATION\_AUDIT: PASS\].
- **Step 7 — Level D Consequential Gate Halt (operator / sentinel-manager):** Before writing the final pleading to the Drive case folder, execution halts and outputs --- \[LEVEL\_D\_PROPOSAL: TASK-NGT-SMC-001\] --- specifying target path, payload diff, storage consequence, and rollback path. Only after the operator replies 'APPROVE' is the file written, followed by M-0086 byte-exact read-back verification and logging in 02\_Optimus\_Decisions\_Approval\_Ledger.

### **7.2 Workflow 2: Consumer Protection Act 2019 Demand Notice (Tier 2: Fast-Track Pipeline)**

- **Operator Prompt:** *"Draft a final 7-day statutory notice to Livpure regarding the defective water purifier under the Visons Gallery account. Previous service visits failed to replace the RO membrane."*
- **Step 1 — Triage & Fast-Track Selection (sentinel-manager → project-coordinator):** Classified as **Class C (Fast-Track)** under \[TASK\_PAYLOAD: LIVPURE\_CONSUMER\_2026\]. Because CPA 2019 legal premises are pre-verified, selects **Tier 2 (Plan -> Researcher -> Operator -> Verifier)**, bypassing Phase 3 adversarial simulation to save tokens.
- **Step 2 — Evidence Extraction & Drafting (researcher → operator):** researcher extracts invoice dates, serial numbers, and technician job sheets from Drive. operator drafts the formal notice citing Section 2(47) (Unfair Trade Practice) and Section 84 (Product Liability) of the CPA 2019, claiming 18% p.a. statutory interest.
- **Step 3 — Independent Math Catch (verifier-officer):** Recomputes the claimed 18% p.a. interest from first principles (M-0042 / M-0081) across the exact day count between invoice date and notice date. Detects an arithmetic discrepancy in the draft's interest rollup, issues a FAIL - REVISIONS MANDATORY (Revision Counter = 1), and forces operator to correct the figure to the exact simple interest formula before emitting the Level D proposal.

### **7.3 Workflow 3: Parametric Woodworking Beam-Deflection Audit (Tier 3: Audit-Only Pipeline)**

- **Operator Prompt:** *"Audit my OpenSCAD script for the 4-foot wardrobe carcass. I changed shelf spans from 600mm to 900mm using 18mm commercial ply. Will it sag under a 30kg distributed load?"*
- **Step 1 — Audit-Only Routing (sentinel-manager → project-coordinator):** Triaged to **Tier 3 (Critical Analyst -> Verifier Officer)** under \[TASK\_PAYLOAD: WOODWORKING\_CAD\_2026\].
- **Step 2 — Structural Failure Analysis (critical-analyst):** Applies uniform distributed load beam-deflection physics ("Sagulator" model) for un-stiffened plywood spans (calipered thickness 17.4mm). Flags a Fatal Defect: increasing span $L$ from 600mm to 900mm increases deflection by a factor of $(900/600)^3 = 3.375$, pushing total deflection past the allowable 2.0mm threshold and causing long-term shelf creep and cabinet door misalignment.
- **Step 3 — First-Principles Verification (verifier-officer):** Independently computes the area moment of inertia $I = \\frac{b \\cdot h^3}{12}$ and maximum deflection $\\delta\_{\\max} = \\frac{5 \\cdot W \\cdot L^3}{384 \\cdot E \\cdot I}$ using plywood modulus of elasticity $E = 7000\\text{ N/mm}^2$. Confirms the failure prediction and validates two structural remedies: adding a 40mm solid hardwood front stiffener lip or an intermediate vertical partition. Delivered directly in chat (Level B Action) with zero Drive mutations.

## **8\. EMPIRICAL AUDIT: WORK PACKAGE HISTORY (P000–P032) & GOVERNANCE DECISIONS (DEC-001–DEC-016)**

All 7 native agent skills and all 5 authoritative Google Drive Control Plane registers are empirically reconciled and operational as of **27 October 2026** \[VERIFIED COMPLETE\]:

| Phase & Work Package ID | Milestone Description & Technical Scope | Governing Decisions | Audit Status |
| --- | --- | --- | --- |
| **Phases 0–2 (P000–P004)** | Baseline records reconciliation, Drive/Gmail/Calendar targeted permission boundary testing, and codification of 04\_Optimus\_Shared\_Operating\_Contract. | DEC-001, DEC-002 | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Phases 3–6 (P005–P016, P024–P025)** | Deployment and structural unit testing of prompt-architect, sentinel-manager, project-coordinator, researcher, critical-analyst, operator, and verifier-officer. | DEC-003, DEC-005, DEC-006 | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Workspace Hygiene (P023, P026)** | Strict System vs. Task Payload Decoupling (M-0001 / M-0130) and root Drive de-cluttering (quarantining 16 legacy register/guidebook snapshots). | DEC-004, DEC-007 | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Phase 7 (P017–P018)** | End-to-End multi-agent workflow validation and Level D Consequential Action Gating audits across live legal and engineering payloads. | DEC-008 to DEC-010 | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Phase 8 (P027)** | **Kernel v3.0 Master Synchronization:** Reconciled Control Plane to 297 Canonical Mechanisms, Dynamic Ephemeral Swarms, and Stigmergic State Boards (M-0123). | DEC-011 (26 Oct 2026) | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Phase 9 (P028 / TASK-INGEST-RECON-V2-8)** | **Full 342-Card Corpus Ingestion:** Promoted 43 Master Engines (M-0298–M-0340), consolidated 840 operational variants, staged 22 reference proposals, and synchronized all 7 skills with read-back verification. | DEC-012 (26 Oct 2026) | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Phases 10–12 (P029–P031 / TASK-SUBTRACTIVE-REFACTOR-001 to 003)** | **Subtractive Kernel Refactoring Passes 1, 2 & 3 (M-0338):** Merged 102 micro-cards across 23 functional clusters into **261 Active Master Engines** and **919 Operational Variants** with zero unresolved proposals. | DEC-013, DEC-014, DEC-015 (26–27 Oct 2026) | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |
| **Phase 13 (P032 / TASK-RUNTIME-REFACTOR-V3-2)** | **Kernel v3.2.0 Deterministic Runtime Refactor:** Codified 3-tier enforcement boundary; transactional WAL + crash recovery reconciler (**16/16 crash vectors passed**); KMS Ed25519 RFC 8785 action digest verification (**18/18 gateway vectors passed**); Pydantic Claim Registry (M-0015); **10/10 DAG orchestration vectors passed**; executed Stage 3-C Canary Mutation (TSK-CANARY-MUTATION-001) with byte-exact read-back (M-0086). | DEC-016 (27 Oct 2026) | \[VERIFIED COMPLETE\] |
| --- | --- | --- | --- |

## **9\. EMPIRICAL FAILURE HISTORY, POST-MORTEMS & PERMANENT REMEDIATIONS**

In accordance with the **Honesty Invariant (M-0086)**, Project Sentinel documents all historical failure modes encountered during development, their root causes, empirical diagnostic tests, and the permanent architectural mechanisms engineered to resolve them \[VERIFIED COMPLETE\]:

### **9.1 Failure Mode 1: False "Read-Only Sandbox" Capability Hallucination**

- **Observed Symptom:** In early sessions, the agent falsely claimed it lacked permission to create or update Google Drive files, asserting it was trapped in a "read-only conversational sandbox" and forcing the operator to copy-paste everything manually \[OBSERVED\].
- **Root Cause Diagnosis:** Over-broad safety heuristics caused the model to conflate external web-scraping restrictions with authorized first-party Google Workspace Connected App tools \[OBSERVED\].
- **Empirical Verification Test:** Issued isolated tool calls to create a test file in Google Drive; the tool succeeded immediately (\[TESTED PASS\]).
- **Permanent Architectural Fix:** Codified **Dual-Mode State Persistence (M-0071 & M-0104)** and **Autonomous Tool Exhaustion (M-0005)**. Agents must attempt Mode 1 (Direct API Write + M-0086 Read-Back) when authorized, falling back to Mode 2 (\[CHECKPOINT\_EXPORT\] blocks for one-click manual copy) *only* upon a verified tool error or read-only session constraint.

### **9.2 Failure Mode 2: Autoregressive Phantom Writes & Unverified Completion Claims**

- **Observed Symptom:** The assistant generated fluent text stating *"I have updated the Master Task Register with your new milestones,"* when zero underlying tool calls had actually been dispatched or committed \[OBSERVED\].
- **Root Cause Diagnosis:** Autoregressive next-token prediction completed the conversational narrative of success prior to invoking or verifying the storage API \[OBSERVED\].
- **Permanent Architectural Fix:** Engineered the **Observe-Before-Mutate Gate (M-0150)**, **Two-Phase Crash-Resilient Write Pipeline**, and **Mandatory Post-Mutation Read-Back Verification (M-0086)**. The verifier-officer and operator are blocked from reporting completion until an independent read\_file\_content or get\_file\_metadata call confirms byte-exact content and updated modification timestamps on the server.

### **9.3 Failure Mode 3: Root Directory Sprawl & Split-Brain Register Drift**

- **Observed Symptom:** Uncontrolled proliferation of duplicate .md files, temporary scratchpads, 8 competing Guidebook drafts, and 8 conflicting register snapshots in the Google Drive root folder, creating "split-brain" state confusion across sessions \[OBSERVED\].
- **Root Cause Diagnosis:** Absence of strict file lifecycle governance and lack of a single canonical control plane path \[OBSERVED\].
- **Permanent Architectural Fix:** Executed DEC-001, DEC-003, and P026 under Level D approval. Quarantined all legacy files into 00\_Archive\_Legacy and locked the active control plane to the five canonical registers inside Project Optimus — Personal AI Team/ governed by **Universal Cross-Medium Synchronization (M-0131)**.

### **9.4 Failure Mode 4: Desktop Web vs. Mobile Android Client Viewport & RAM Divergence**

- **Observed Symptom:** On the Android mobile app, wide Markdown tables truncated visually, attachment context dropped during background app switching, and stacking both \[STATE\_BOARD\] and \[SENTINEL TURN SUMMARY\] footers wasted viewport space \[REPORTED\].
- **Root Cause Diagnosis:** Mobile OS background memory purging and narrow viewport rendering constraints \[REPORTED\].
- **Permanent Architectural Fix:** Enforced **Envelope Deduplication** in sentinel-manager (omitting standalone turn summaries whenever a \[STATE\_BOARD\] or \[LEVEL\_D\_PROPOSAL\] is present) and mandated persisting complex multi-column registers directly to Google Docs while keeping chat state boards compact and portable.

## **10\. DEPENDENCIES, RISK MATRIX & STRATEGIC QUESTIONS FOR EXPERT REVIEW**

### **10.1 Single Points of Failure (SPOFs) & Architectural Mitigations**

| Identified Risk / Dependency | Severity | Failure Impact | Engineered Architectural Mitigation |
| --- | --- | --- | --- |
| **Platform Tool API Outage or Schema Drift** | **HIGH** | Disruption of direct Drive/Docs/Gmail tool execution. | **Dual-Mode Persistence (M-0104):** Automatic graceful degradation to portable \[CHECKPOINT\_EXPORT\] envelopes for zero-loss manual copy. |
| --- | --- | --- | --- |
| **Control Plane Register Corruption** | **HIGH** | Loss of cross-session task graph coherence. | **Two-Phase WAL + Drive Revision History:** Pre-image backup hashing, staged versioning, and M-0086 byte-exact read-back verification. |
| --- | --- | --- | --- |
| **Long-Horizon Context Attention Decay** | **MEDIUM** | Constraint dropping in threads exceeding 50,000 tokens. | **Zero-Waste Meta-Compiler (M-0095) & Phase Reserves (M-0308):** Injecting only 3–6 Master Engines per role + Mid-Context Schema Restatement (M-0339). |
| --- | --- | --- | --- |
| **Prompt Injection via Hostile Documents** | **CRITICAL** | Malicious instructions inside opposing legal briefs hijacking agent tools. | **Multiplexed Delimited Quarantine (M-0058):** Wrapping all ingested external text in <untrusted\_data> envelopes and locking researcher to READ\_ONLY capability tokens. |
| --- | --- | --- | --- |
| **Human Operator Bottleneck (SPOF)** | **MEDIUM** | Consequential actions halt when Aditya Dhange is offline. | **Intentional By Design (M-0055 & M-0299):** Level D actions carry legal/financial liability and must never be automated without explicit human sign-off. |
| --- | --- | --- | --- |

### **10.2 Key Architectural Discussion Points for the AI Expert Presentation**

When presenting this DPR to the AI expert, the following four frontier architectural questions represent high-leverage areas for expert feedback:

1. **Optimal Subtractive Granularity (M-0338):** Having consolidated 342 cards down to 261 Master Engines and 23 primary clusters, what is the optimal granularity threshold where merging rules further begins to reduce zero-shot instruction adherence vs. improving KV-cache prefix stability?
2. **Cross-Agent Context Compression vs. Verbatim Quote Ledgers (M-0134):** How to best balance the token overhead of passing verbatim <quotes> ledgers from researcher to verifier-officer against the risk of semantic drift if intermediate summaries are used?
3. **Adversarial Deadlock Arbitration (M-0075 vs. M-0015):** Evaluating our **Max-1 Auto-Revision Loop Breaker** when critical-analyst (demanding stronger rhetorical/strategic posture) collides with verifier-officer (enforcing strict abstention on unverified gaps).
4. **Scaling Staged Mechanism Promotion (M-PROP-CORE):** Best practices for automated evaluation harnesses (M-PROP-0357 Pre-Merge CI/CD Registry Gate) to benchmark the 1,560 staged techniques in proposed\_core\_techniques.md and proposed\_mechanisms.md before promoting them to the active canonical index.