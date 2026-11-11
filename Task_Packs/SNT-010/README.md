# SNT-010 — Deterministic DAG Compiler Prototype

**Status:** ACTIVE TASK-PACK PROTOTYPE — NON-AUTHORITATIVE  
**Task owner:** ChatGPT  
**Base commit:** `7e8d1863559d11dc1e028c177a26de68565e0d12`  
**Runtime status:** Not integrated; not activated; not a production control.

## Objective

Implement one concrete Manager capability already specified in the Sentinel Manager working specification: compile task dependencies, reject cyclic dependency branches, identify downstream blocked work, and preserve independent acyclic work for possible dispatch.

## Deliverable

- `sentinel_dag.py`: dependency-graph compiler and JSON stdin/stdout CLI.
- `test_sentinel_dag.py`: focused standard-library tests for valid order, cycle isolation, self-loops, malformed references, and deterministic output.
- `STATE.md`: task-pack state and boundaries.

## Input

The CLI accepts one JSON object:

```json
{
  "dependencies": {
    "research": [],
    "analysis": ["research"],
    "draft": ["analysis"]
  }
}
```

Each key is a node ID; each value is the list of prerequisite node IDs.

## Output semantics

- `cycle_components`: strongly connected components that contain a cycle.
- `blocked_nodes`: cycle nodes plus every downstream dependant that cannot proceed.
- `runnable_order`: stable topological order for independent nodes outside blocked branches.
- `blocked_reasons`: direct cycle membership or blocked prerequisites.

A cycle does not invalidate independent branches. No dependency is silently removed.

## Run

From this directory:

```bash
python -m unittest -v
printf '%s' '{"dependencies":{"A":["B"],"B":["A"],"C":["B"],"D":[],"E":["D"]}}' | python sentinel_dag.py --pretty
```

Python standard library only. No network, GitHub, model, credential, or external-service access.

## Boundary

This prototype is an isolated task-pack artifact. It does not establish the final runtime interface, approve the draft Manager specification, modify canonical skills, or authorize production dispatch. Integration requires a separate architecture/implementation decision.
