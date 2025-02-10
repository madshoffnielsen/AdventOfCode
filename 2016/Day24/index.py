from collections import deque
from itertools import permutations

def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def find_positions(grid):
    positions = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell.isdigit():
                positions[int(cell)] = (x, y)
    return positions

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    visited = set([start])
    distances = {}
    
    while queue:
        (x, y), dist = queue.popleft()
        
        if grid[x][y].isdigit():
            distances[int(grid[x][y])] = dist
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))
    
    return distances

def calculate_all_distances(grid, positions):
    all_distances = {}
    for pos in positions:
        all_distances[pos] = bfs(grid, positions[pos])
    return all_distances

def tsp(distances, start, return_to_start=False):
    points = list(distances.keys())
    points.remove(start)
    min_path = float('inf')
    
    for perm in permutations(points):
        path_length = 0
        current = start
        for point in perm:
            path_length += distances[current][point]
            current = point
        if return_to_start:
            path_length += distances[current][start]
        min_path = min(min_path, path_length)
    
    return min_path

def main():
    grid = read_input("2016/Day24/input.txt")
    positions = find_positions(grid)
    distances = calculate_all_distances(grid, positions)
    
    part1 = tsp(distances, 0)
    part2 = tsp(distances, 0, return_to_start=True)
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()