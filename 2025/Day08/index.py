from typing import List, Tuple
from collections import defaultdict

def read_input(path: str) -> List[Tuple[int, int, int]]:
    points = []
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                x, y, z = map(int, line.split(','))
                points.append((x, y, z))
    return points

def part1(points: List[Tuple[int, int, int]]) -> int:
    n = len(points)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dz = points[i][2] - points[j][2]
            dist_sq = dx * dx + dy * dy + dz * dz
            edges.append((dist_sq, i, j))
    
    edges.sort()
    
    for _, i, j in edges[:1000]:
        union(i, j)
    
    components = defaultdict(int)
    for i in range(n):
        components[find(i)] += 1
    
    sizes = list(components.values())
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def part2(points: List[Tuple[int, int, int]]) -> int:
    n = len(points)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dz = points[i][2] - points[j][2]
            dist_sq = dx * dx + dy * dy + dz * dz
            edges.append((dist_sq, i, j))
    
    edges.sort()
    
    merges = 0
    for dist_sq, i, j in edges:
        if union(i, j):
            merges += 1
            if merges == n - 1:
                p1, p2 = points[i], points[j]
                return p1[0] * p2[0]
    return 0  # shouldn't happen

def main() -> None:
    points = read_input("2025/Day08/input.txt")
    print("Part 1:", part1(points))
    print("Part 2:", part2(points))

if __name__ == "__main__":
    main()