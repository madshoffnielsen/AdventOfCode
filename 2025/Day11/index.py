from typing import List, Dict, Tuple
from collections import defaultdict

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def build_graph(lines: List[str]) -> Dict[str, List[str]]:
    graph = defaultdict(list)
    for line in lines:
        name, outputs = line.split(': ')
        graph[name] = outputs.split()
    return graph

def count_paths(graph: Dict[str, List[str]], node: str, target: str, memo: Dict[Tuple[str, bool, bool], int], check_visits: bool = False, visited_dac: bool = False, visited_fft: bool = False) -> int:
    if node == target:
        if check_visits:
            return 1 if visited_dac and visited_fft else 0
        else:
            return 1
    key = (node, visited_dac, visited_fft)
    if key in memo:
        return memo[key]
    total = 0
    new_dac = visited_dac or (node == "dac")
    new_fft = visited_fft or (node == "fft")
    for neigh in graph[node]:
        total += count_paths(graph, neigh, target, memo, check_visits, new_dac, new_fft)
    memo[key] = total
    return total

def part1(graph: Dict[str, List[str]]) -> int:
    return count_paths(graph, "you", "out", {}, check_visits=False)

def part2(graph: Dict[str, List[str]]) -> int:
    return count_paths(graph, "svr", "out", {}, check_visits=True)

def main() -> None:
    lines = read_input("2025/Day11/input.txt")
    graph = build_graph(lines)
    print("Part 1:", part1(graph))
    print("Part 2:", part2(graph))

if __name__ == "__main__":
    main()