from heapq import heappush, heappop
from collections import defaultdict

def read_input(file_path):
    with open(file_path) as f:
        return [[int(x) for x in line.strip()] for line in f]

def get_neighbors(pos, direction, steps, min_steps, max_steps):
    r, c = pos
    dr, dc = direction
    neighbors = []
    
    # Continue straight if under max steps
    if steps < max_steps:
        neighbors.append(((r + dr, c + dc), direction, steps + 1))
    
    # Turn left or right if minimum steps met
    if steps >= min_steps:
        for new_dr, new_dc in [(dc, -dr), (-dc, dr)]:  # 90 degree turns
            neighbors.append(((r + new_dr, c + new_dc), (new_dr, new_dc), 1))
            
    return neighbors

def find_path(grid, min_steps=1, max_steps=3):
    height, width = len(grid), len(grid[0])
    target = (height - 1, width - 1)
    
    # State: (heat_loss, (row, col), (dir_row, dir_col), steps)
    queue = [(0, (0, 0), (0, 1), 0), (0, (0, 0), (1, 0), 0)]
    seen = set()
    costs = defaultdict(lambda: float('inf'))
    
    while queue:
        heat_loss, pos, direction, steps = heappop(queue)
        
        if pos == target and steps >= min_steps:
            return heat_loss
            
        state = (pos, direction, steps)
        if state in seen:
            continue
        seen.add(state)
        
        for new_pos, new_dir, new_steps in get_neighbors(pos, direction, steps, min_steps, max_steps):
            r, c = new_pos
            if 0 <= r < height and 0 <= c < width:
                new_heat = heat_loss + grid[r][c]
                new_state = (new_pos, new_dir, new_steps)
                
                if new_heat < costs[new_state]:
                    costs[new_state] = new_heat
                    heappush(queue, (new_heat, new_pos, new_dir, new_steps))
    
    return float('inf')

def part1(grid):
    return find_path(grid, min_steps=1, max_steps=3)

def part2(grid):
    return find_path(grid, min_steps=4, max_steps=10)

def main():
    grid = read_input("2023/Day17/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()