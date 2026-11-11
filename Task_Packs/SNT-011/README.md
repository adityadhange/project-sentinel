# SNT-011 — Task Intake and State Integration

**Status:** Implementation submitted for review; stacked on SNT-010.  
**Depends on:** SNT-010 deterministic DAG compiler.  
**Runtime status:** Reference implementation only; not activated in Sentinel runtime.

## Purpose

Connect structured task intake and work-package lifecycle tracking to the SNT-010 dependency compiler. The compiler remains the single source of dependency-graph validation and topological classification. This task pack adds the intake adapter, state transitions, persistence, and dependency-triggered readiness updates.

## Intake envelope

```json
{
  "task_id": "PROJECT-042",
  "payload": "Prepare a verified research and drafting deliverable",
  "work_packages": [
    {"id": "research", "depends_on": [], "owner": "researcher"},
    {"id": "analysis", "depends_on": ["research"], "owner": "critical-analyst"},
    {"id": "draft", "depends_on": ["analysis"], "owner": "operator"}
  ]
}
```

The intake adapter validates task identity, payload, work-package IDs and prerequisite references, then passes the dependency map to `compile_dag`. Unknown IDs, malformed edges, duplicate IDs and cyclic dependencies are not repaired or silently discarded.

## State semantics

| State | Meaning |
|---|---|
| `PENDING` | Valid work package waiting for prerequisites |
| `READY` | All declared prerequisites are actually `COMPLETED` |
| `IN_PROGRESS` | Manager has recorded an authorized start |
| `BLOCKED` | Cycle, blocked/failed prerequisite, or explicit Manager hold |
| `COMPLETED` | Work package reports completion; downstream readiness is recalculated |
| `FAILED` | Work package failed; downstream dependants are blocked |
| `CANCELLED` | Reserved terminal state for an explicit cancellation record |

At intake, only dependency-free nodes are initially READY (unless the compiler marks them blocked). A node becomes READY only after every prerequisite is COMPLETED. Topological position alone never makes a node dispatch-eligible.

When a package completes, only newly eligible dependants are released. A failure or explicit block propagates to downstream dependants; independent branches remain eligible.

The task-level derived status is `ACTIVE` when any package is READY or IN_PROGRESS, `WAITING` when all remaining work is pending, `BLOCKED` when no work is currently eligible and blocked/failed/cancelled work remains, and `REVIEW` when all packages are completed. `REVIEW` is not final acceptance or task closure.

## Manager and governance boundary

- `SKL-sentinel-manager` owns intake, classification, task identity, compilation invocation, state-board updates and dispatch decisions.
- Optimus specialists execute only work packages assigned to them.
- This module records a Manager-authorized start; it does not authenticate the caller or enforce a platform permission.
- READY means dependency-eligible, not automatically authorized. Scope, owner, WIP-1, capability, evidence and governance checks remain mandatory.
- Level D approval, verifier receipts, mutation execution and independent read-back remain outside this module and are not bypassed.
- The module does not dispatch agents, invoke external services, modify canonical skills or alter permissions/workflows.
- The v4.0 Manager file remains a working draft; this task pack does not ratify it.

## Persistence and operation

The state manager can write an atomic JSON state snapshot to a caller-supplied task-pack path and reload it. The host must ensure the path remains inside the assigned task workspace; path confinement and cross-process locking are not claimed by this prototype.

Run from this directory (with the SNT-010 task pack present as its sibling):

```bash
python -m unittest -v
```

## Acceptance boundary

This is a reviewable integration reference implementation. It demonstrates compiler-connected intake, state initialization, lifecycle transitions, persistence and readiness propagation. It is not production activation or proof of host-enforced permissions, durable shared storage, concurrency safety, or live runtime wiring.
