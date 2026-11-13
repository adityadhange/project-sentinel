"""Benchmark the existing Sentinel DAG compiler without modifying it.

Run from the repository root:
    python Task_Packs/SNT-010/benchmark_dag.py

The benchmark reports end-to-end compile_dag latency and peak Python allocation
for representative graph topologies. Timing is collected without tracemalloc;
peak memory is measured in a separate invocation to avoid distorting timings.
"""
from __future__ import annotations

import argparse
import gc
import statistics
import time
import tracemalloc
from collections.abc import Callable

from sentinel_dag import compile_dag


Graph = dict[str, list[str]]
GraphFactory = Callable[[int], Graph]
NODE_COUNTS = (10, 100, 500)
DEFAULT_REPEATS = 5


def make_chain_graph(node_count: int) -> Graph:
    """Each node (except the first) depends on its immediate predecessor."""
    return {
        f"node_{index:04d}": (
            [] if index == 0 else [f"node_{index - 1:04d}"]
        )
        for index in range(node_count)
    }


def make_branching_graph(node_count: int) -> Graph:
    """A binary dependency tree: each node depends on its parent."""
    return {
        f"node_{index:04d}": (
            [] if index == 0 else [f"node_{(index - 1) // 2:04d}"]
        )
        for index in range(node_count)
    }


def make_dense_graph(node_count: int) -> Graph:
    """A complete acyclic DAG: each node depends on every earlier node."""
    return {
        f"node_{index:04d}": [
            f"node_{prerequisite:04d}" for prerequisite in range(index)
        ]
        for index in range(node_count)
    }


def make_cyclic_graph(node_count: int) -> Graph:
    """A directed ring in which every node belongs to one cycle."""
    return {
        f"node_{index:04d}": [
            f"node_{(index - 1) % node_count:04d}"
        ]
        for index in range(node_count)
    }


TOPOLOGIES: tuple[tuple[str, GraphFactory], ...] = (
    ("chain", make_chain_graph),
    ("branching", make_branching_graph),
    ("dense", make_dense_graph),
    ("cyclic", make_cyclic_graph),
)


def average_runtime_ms(graph: Graph, repeats: int) -> float:
    """Return mean compile_dag wall-clock time, excluding memory tracing."""
    # Warm up imports, caches, and interpreter paths before collecting samples.
    compile_dag(graph)

    samples_ms: list[float] = []
    for _ in range(repeats):
        started = time.perf_counter()
        compile_dag(graph)
        samples_ms.append((time.perf_counter() - started) * 1_000)

    return statistics.fmean(samples_ms)


def peak_memory_kb(graph: Graph) -> float:
    """Return peak traced Python allocation for one compile_dag invocation."""
    gc.collect()
    tracemalloc.start()
    try:
        tracemalloc.reset_peak()
        compile_dag(graph)
        _current_bytes, peak_bytes = tracemalloc.get_traced_memory()
        return peak_bytes / 1_024
    finally:
        tracemalloc.stop()


def run_benchmarks(repeats: int = DEFAULT_REPEATS) -> None:
    if repeats < 1:
        raise ValueError("repeats must be at least 1")

    heading = (
        f"{'Topology':<12} {'Nodes':>7} {'Edges':>9} "
        f"{'Avg time (ms)':>16} {'Peak memory (KB)':>19}"
    )
    print(heading)
    print("-" * len(heading))

    for topology_name, graph_factory in TOPOLOGIES:
        for node_count in NODE_COUNTS:
            graph = graph_factory(node_count)
            edge_count = sum(len(prerequisites) for prerequisites in graph.values())
            average_ms = average_runtime_ms(graph, repeats)
            peak_kb = peak_memory_kb(graph)

            print(
                f"{topology_name:<12} {node_count:>7,d} {edge_count:>9,d} "
                f"{average_ms:>16.3f} {peak_kb:>19.2f}"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repeats",
        type=int,
        default=DEFAULT_REPEATS,
        help=f"timed runs per graph (default: {DEFAULT_REPEATS})",
    )
    args = parser.parse_args()

    try:
        run_benchmarks(args.repeats)
    except ValueError as error:
        parser.error(str(error))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
