"""Deterministic dependency-graph compiler prototype for Project Sentinel.

Input edges are expressed as node -> prerequisite IDs. The compiler identifies
strongly connected cycle components, blocks their downstream dependants, and
returns a stable topological order for independent runnable nodes.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from collections.abc import Mapping, Sequence
from heapq import heappop, heappush
from typing import Any


def _normalize(dependencies: Mapping[str, Sequence[str]]) -> dict[str, tuple[str, ...]]:
    if not isinstance(dependencies, Mapping):
        raise ValueError("dependencies must be an object mapping node IDs to prerequisite lists")

    graph: dict[str, tuple[str, ...]] = {}
    for node, prereqs in dependencies.items():
        if not isinstance(node, str) or not node.strip():
            raise ValueError("node IDs must be non-empty strings")
        if isinstance(prereqs, (str, bytes)) or not isinstance(prereqs, Sequence):
            raise ValueError(f"prerequisites for {node!r} must be a list of node IDs")
        if any(not isinstance(dep, str) or not dep.strip() for dep in prereqs):
            raise ValueError(f"prerequisites for {node!r} must contain non-empty string IDs")
        if len(set(prereqs)) != len(prereqs):
            raise ValueError(f"prerequisites for {node!r} contain duplicates")
        graph[node] = tuple(sorted(prereqs))

    unknown = sorted({dep for prereqs in graph.values() for dep in prereqs if dep not in graph})
    if unknown:
        raise ValueError("unknown prerequisite node(s): " + ", ".join(unknown))
    return graph


def compile_dag(dependencies: Mapping[str, Sequence[str]]) -> dict[str, Any]:
    """Compile a dependency map into cycle, blocked, and runnable classifications."""
    graph = _normalize(dependencies)
    nodes = sorted(graph)

    # Build reverse edges: prerequisite -> direct dependants.
    dependants: dict[str, list[str]] = {node: [] for node in nodes}
    for node, prereqs in graph.items():
        for prereq in prereqs:
            dependants[prereq].append(node)
    for values in dependants.values():
        values.sort()

    # Kosaraju SCC pass 1: iterative DFS post-order avoids recursion limits.
    visited: set[str] = set()
    finish_order: list[str] = []
    for start in nodes:
        if start in visited:
            continue
        stack: list[tuple[str, bool]] = [(start, False)]
        while stack:
            node, expanded = stack.pop()
            if expanded:
                finish_order.append(node)
                continue
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, True))
            for prerequisite in reversed(graph[node]):
                if prerequisite not in visited:
                    stack.append((prerequisite, False))

    # Kosaraju SCC pass 2 on the reversed graph.
    assigned: set[str] = set()
    components: list[tuple[str, ...]] = []
    for start in reversed(finish_order):
        if start in assigned:
            continue
        component: list[str] = []
        stack = [start]
        assigned.add(start)
        while stack:
            node = stack.pop()
            component.append(node)
            for dependant in reversed(dependants[node]):
                if dependant not in assigned:
                    assigned.add(dependant)
                    stack.append(dependant)
        components.append(tuple(sorted(component)))

    cycle_components = sorted(
        component
        for component in components
        if len(component) > 1 or component[0] in graph[component[0]]
    )
    cyclic_nodes = {node for component in cycle_components for node in component}

    # A cycle blocks every downstream dependant, not independent branches.
    blocked = set(cyclic_nodes)
    queue = deque(sorted(cyclic_nodes))
    while queue:
        prerequisite = queue.popleft()
        for dependant in dependants[prerequisite]:
            if dependant not in blocked:
                blocked.add(dependant)
                queue.append(dependant)

    # Stable Kahn ordering over the remaining independent acyclic subgraph.
    runnable = set(nodes) - blocked
    indegree = {
        node: sum(prerequisite in runnable for prerequisite in graph[node])
        for node in runnable
    }
    ready: list[str] = []
    for node, degree in indegree.items():
        if degree == 0:
            heappush(ready, node)

    order: list[str] = []
    while ready:
        node = heappop(ready)
        order.append(node)
        for dependant in dependants[node]:
            if dependant not in runnable:
                continue
            indegree[dependant] -= 1
            if indegree[dependant] == 0:
                heappush(ready, dependant)

    if len(order) != len(runnable):
        raise RuntimeError("internal compiler error: residual cycle in runnable subgraph")

    reasons: dict[str, dict[str, Any]] = {}
    for component in cycle_components:
        for node in component:
            reasons[node] = {"kind": "cycle", "component": list(component)}
    for node in sorted(blocked - cyclic_nodes):
        reasons[node] = {
            "kind": "blocked_by_prerequisite",
            "blocked_dependencies": sorted(
                prerequisite for prerequisite in graph[node] if prerequisite in blocked
            ),
        }

    return {
        "valid": not cycle_components,
        "cycle_components": [list(component) for component in cycle_components],
        "blocked_nodes": sorted(blocked),
        "runnable_order": order,
        "blocked_reasons": reasons,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pretty", action="store_true", help="pretty-print JSON output")
    args = parser.parse_args(argv)
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict) or set(payload) != {"dependencies"}:
            raise ValueError("input must be a JSON object with exactly one 'dependencies' field")
        result = compile_dag(payload["dependencies"])
    except (json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
