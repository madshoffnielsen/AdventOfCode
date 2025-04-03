from typing import Dict, List, Set, Tuple
from collections import defaultdict
import networkx as nx

Graph = Dict[str, Set[str]]

def read_input(file_path: str) -> Graph:
    """Read component connections into a graph."""
    graph = defaultdict(set)
    with open(file_path) as f:
        for line in f:
            source, targets = line.strip().split(': ')
            for target in targets.split():
                graph[source].add(target)
                graph[target].add(source)
    return graph

def find_min_cut(graph: Graph) -> int:
    """Find minimum cut using NetworkX."""
    # Convert our graph to NetworkX graph
    G = nx.Graph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)
    
    # Find the minimum cut
    cut_value, partition = nx.stoer_wagner(G)
    if cut_value == 3:  # We found the desired cut
        return len(partition[0]) * len(partition[1])
    return 0

def part1(graph: Graph) -> int:
    """Find product of group sizes after cutting 3 wires."""
    return find_min_cut(graph)

def main():
    """Main program."""
    print("\n--- Day 25: Snowverload ---")
    
    graph = read_input("2023/Day25/input.txt")
    
    result1 = part1(graph)
    print(f"Part 1: {result1}")
    print("Part 2: Merry Christmas! 🎄")

if __name__ == "__main__":
    main()