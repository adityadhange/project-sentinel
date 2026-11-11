03 — Capability & Permissions Register (Canonical Consolidated, Kernel v3.2.0 Reconciled)

Project: Optimus & Sentinel AI Coworker Team

Governing Standard: Master Roadmap v3.0 & Kernel v3.2.0 (Deterministic Runtime Baseline)

Operational Posture: CONTROLLED OPERATIONAL STAGING

Date synchronized / audited: 27 October 2026 (primary); 18 October 2026 (earlier Gate 1 audit records)

Evidence Standard: REPORTED | OBSERVED | TESTED PASS | TESTED PARTIAL | TESTED FAIL | NOT TESTED

Runtime Capability & Security Separation Matrix

KMS Signing Daemon (sentinel-kmsd) — Security Plane: Host Runtime (Plane 1). Permission Scope & Capability Class: Key generation, Ed25519 asymmetric signing, challenge nonces. Enforcement Mechanism: Isolated Unix domain socket; out-of-process credential protection.

Transactional WAL & File Driver — Security Plane: Host Runtime (Plane 1). Permission Scope & Capability Class: Atomic write, fdatasync, renameat2, openat2 descriptor isolation. Enforcement Mechanism: Linux kernel directory descriptor anchoring (RESOLVE_BENEATH).

Google Drive & Docs APIs — Security Plane: Platform (Plane 1). Permission Scope & Capability Class: File creation, metadata reading, folder hierarchy reorganization. Enforcement Mechanism: Scoped OAuth tokens; Level D human approval required for moves/creates.

Researcher Subagent — Security Plane: Execution Fleet (Plane 2). Permission Scope & Capability Class: READ_ONLY strictly; primary document ingestion. Enforcement Mechanism: Capability class token lockdown; tool gateway blocks all mutation verbs.

Operator Subagent — Security Plane: Execution Fleet (Plane 2). Permission Scope & Capability Class: Sandboxed file staging; coordinate-free surgical patching (M-0020). Enforcement Mechanism: Locked behind Level D Consequential Action Proposal Envelope (M-0099).

Verifier Officer Subagent — Security Plane: Execution Fleet (Plane 2). Permission Scope & Capability Class: Independent post-mutation read-back (M-0086), math verification. Enforcement Mechanism: Read-only inspection; non-bypassable completion assertion gate.

External WAN / Sockets — Security Plane: Network Sandbox. Permission Scope & Capability Class: HARD-DISABLED. Enforcement Mechanism: Host network namespace isolation; external network egress dropped.

Capability Issuance & Lease Lifecycle Invariants

Single-Use Capability Tokens: Capability tokens (CAP-*) are minted in PostgreSQL under SERIALIZABLE isolation and consumed atomically during mutation preparation.

Lease Margins: Tool gateway requires an active coordinator lease margin of > 5,000 ms prior to executing any physical write.

Epistemic Gate: Capability tokens for mutations cannot be issued unless supporting claims have passed M-0015 schema validation.

Capability & Integration Matrix (Verified Actions, Scopes, Tests)

Google Drive & Docs

Intended use: Authoritative project state, registers, Guidebook storage, checkpoint persistence.

Exact verified actions: search_files, read_file_content, create_file, update_file (moving parent directories).

Permission/access scope: Full authenticated access to Project Sentinel and Optimus Drive structures.

Test method: Created folders, authored registers, verified file moves, performed programmatic read-back checks.

Verified status: TESTED PASS

Limitations: Binary file editing (e.g., inside compiled zips) unsupported; plain-text/Docs operate natively.

Transparent fallback: Stage content in Google Docs; export or manual insertion for complex formats.

Last audited: 2026-10-18

Skill Invocation & Execution

Intended use: Dynamic loading of specialized agent capability packs and compilation logic.

Exact verified actions: Sub-agent compilation, Guidebook extraction, skill creator/updater hooks.

Permission/access scope: Native prompt and sub-agent execution context in Gemini.

Test method: Validated ingestion schemas and active compilation prompts against Canonical Buckets 1–5.

Verified status: TESTED PASS

Limitations: Ephemeral sub-agents must not assume cross-session persistence unless state is persisted.

Transparent fallback: Pass structured <state_board> into prompt envelopes and persist to Drive checkpoints.

Last audited: 2026-10-18

Google Search

Intended use: Real-time research, statutory grounding, fact-checking, current-date verification.

Exact verified actions: Real-time web queries, citation discovery, primary-source retrieval.

Permission/access scope: Read-only search API integration in Gemini.

Test method: Retrieved grounded context and statutory precedents.

Verified status: TESTED PASS

Limitations: Cannot bypass paywalls or access internal authenticated portals; secondary aggregators filtered per M-0019.

Transparent fallback: Disclose coverage gaps; request manual source dump if gated.

Last audited: 2026-10-18

Gmail

Intended use: Communication briefings, reading relevant threads on explicit instruction.

Exact verified actions: Search message metadata, read permitted threads, draft communications (Level B).

Permission/access scope: Authenticated read/draft via Google Workspace connector.

Test method: Retrieved inbox context without unsolicited outbound transmission.

Verified status: TESTED PASS

Limitations: Direct outbound sending without explicit operator confirmation blocked (Level D).

Transparent fallback: Present exact draft in chat for operator approval before sending.

Last audited: 2026-10-18

Google Calendar

Intended use: Schedule inspection, timeline audits, recurring workflow scheduling.

Exact verified actions: Read scheduled events, query timeline constraints.

Permission/access scope: Authenticated read via Google Workspace connector.

Test method: Inspected schedule constraints and timestamps.

Verified status: TESTED PASS

Limitations: Automated recurring event modification without approval restricted.

Transparent fallback: Propose modifications and require explicit operator confirmation.

Last audited: 2026-10-18

Autonomous Scheduled Actions

Intended use: Recurring weekly briefings and background query prep.

Exact verified actions: Background query prep and summary generation.

Permission/access scope: Native Gemini scheduled tasks framework.

Test method: Audited architecture requirements against Roadmap P020.

Verified status: TESTED PARTIAL

Limitations: Must be manual-first; must never automate Level D consequential actions (payments, deletions, outbound emails).

Transparent fallback: Operator triggers or inspects drafts prior to dissemination.

Last audited: 2026-10-18

Gate 1 Evaluation: Capability Readiness (consolidated)

Skill Creation & Invocation: Verified operational.

Workspace Drive Storage & Read-Back: Verified operational with zero data loss.

Safety & Level D Gating: Strict human-in-the-loop controls verified; automated destructive or outbound external actions remain hard-blocked.

Gate 1 Verdict: PASSED — System authorized to establish Shared Operating Contract (Phase 2).

Notes and Version Reconciliation

Source material included records labeled Kernel v3.0, v3.2.0, and earlier v2.0 Gate-1 audit notes. This consolidated register uses Kernel v3.2.0 as the primary reconciled baseline while preserving Gate 1 audit findings dated 18 October 2026.

Kernel v3.0 notes (platform reality & graceful degradation) are preserved conceptually: browser/tool boundaries, transparent limitation reporting, and manual fallback protocols remain enforced under v3.2.0 deterministic runtime posture.
