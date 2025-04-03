from typing import List, Set, Dict, Tuple
from collections import defaultdict, deque

Grid = List[str]
Point = Tuple[int, int]
Graph = Dict[Point, Dict[Point, int]]

def read_input(file_path: str) -> Grid:
    """Read the hiking trail map."""
    with open(file_path) as f:
        return [line.strip() for line in f]

def get_neighbors(grid: Grid, pos: Point, slopes: bool = True) -> List[Point]:
    """Get valid neighboring positions."""
    x, y = pos
    neighbors = []
    
    # Handle slopes if enabled
    if slopes:
        match grid[y][x]:
            case '>':
                return [(x+1, y)] if x+1 < len(grid[0]) else []
            case '<':
                return [(x-1, y)] if x-1 >= 0 else []
            case '^':
                return [(x, y-1)] if y-1 >= 0 else []
            case 'v':
                return [(x, y+1)] if y+1 < len(grid) else []
    
    # Check all directions
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(grid[0]) and 
            0 <= ny < len(grid) and 
            grid[ny][nx] != '#'):
            neighbors.append((nx, ny))
    
    return neighbors

def build_graph(grid: Grid, slopes: bool = True) -> Graph:
    """Convert grid to graph of junctions."""
    start = (1, 0)
    end = (len(grid[0])-2, len(grid)-1)
    graph = defaultdict(dict)
    
    # Find all junctions (points with more than 2 neighbors)
    junctions = {start, end}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '#':
                neighbors = get_neighbors(grid, (x, y), slopes)
                if len(neighbors) > 2:
                    junctions.add((x, y))
    
    # Find paths between junctions
    for junction in junctions:
        stack = [(junction, 0, {junction})]
        while stack:
            pos, dist, visited = stack.pop()
            
            if pos in junctions and pos != junction and dist > 0:
                graph[junction][pos] = max(graph[junction].get(pos, 0), dist)
                continue
                
            for next_pos in get_neighbors(grid, pos, slopes):
                if next_pos not in visited:
                    stack.append((next_pos, dist + 1, visited | {next_pos}))
    
    return graph

def find_longest_path(graph: Graph, start: Point, end: Point) -> int:
    """Find longest path from start to end using DFS."""
    def dfs(pos: Point, visited: Set[Point]) -> int:
        if pos == end:
            return 0
            
        max_length = float('-inf')
        visited.add(pos)
        
        for next_pos, dist in graph[pos].items():
            if next_pos not in visited:
                length = dfs(next_pos, visited)
                if length != float('-inf'):
                    max_length = max(max_length, length + dist)
                    
        visited.remove(pos)
        return max_length
    
    return dfs(start, set())

def part1(grid: Grid) -> int:
    """Find longest path considering slopes."""
    graph = build_graph(grid, slopes=True)
    return find_longest_path(graph, (1, 0), (len(grid[0])-2, len(grid)-1))

def part2(grid: Grid) -> int:
    """Find longest path ignoring slopes."""
    graph = build_graph(grid, slopes=False)
    return find_longest_path(graph, (1, 0), (len(grid[0])-2, len(grid)-1))

def main():
    """Main program."""
    print("\n--- Day 23: A Long Walk ---")
    
    grid = read_input("2023/Day23/input.txt")
    
    result1 = part1(grid)
    print(f"Part 1: {result1}")
    
    result2 = part2(grid)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()