from collections import deque
from itertools import combinations

def read_input(file_path):
    with open(file_path) as f:
        grid = [list(line.strip()) for line in f]
    return grid

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return (r, c)
    return None

def get_neighbors(pos, grid, infinite=False):
    r, c = pos
    height, width = len(grid), len(grid[0])
    
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_r, new_c = r + dr, c + dc
        if infinite:
            grid_r, grid_c = new_r % height, new_c % width
            if grid[grid_r][grid_c] != '#':
                yield (new_r, new_c)
        else:
            if (0 <= new_r < height and 0 <= new_c < width
                and grid[new_r][new_c] != '#'):
                yield (new_r, new_c)

def count_reachable_plots(grid, steps, infinite=False):
    start = find_start(grid)
    current = {start}
    
    for _ in range(steps):
        next_positions = set()
        for pos in current:
            for neighbor in get_neighbors(pos, grid, infinite):
                next_positions.add(neighbor)
        current = next_positions
    
    # Include positions reachable in exactly 'steps' moves
    return len(current)

def extrapolate_infinite_steps(grid, target_steps):
    size = len(grid)
    steps_required = target_steps % size
    full_grids = target_steps // size
    
    # Calculate points at key positions
    points = []
    for n in range(3):
        steps = steps_required + (n * size)
        points.append(count_reachable_plots(grid, steps, infinite=True))
    
    # Use quadratic formula to find pattern
    a = (points[2] + points[0] - 2 * points[1]) // 2
    b = points[1] - points[0] - a
    c = points[0]
    
    n = full_grids
    return a * n * n + b * n + c

def part1(grid):
    return count_reachable_plots(grid, 64)

def part2(grid):
    return extrapolate_infinite_steps(grid, 26501365)

def main():
    grid = read_input("2023/Day21/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()