from collections import deque

def is_wall(x, y, seed):
    if x < 0 or y < 0:
        return True
    val = x*x + 3*x + 2*x*y + y + y*y + seed
    binary = bin(val)[2:]
    return binary.count('1') % 2 == 1

def solve(seed, target_x, target_y, max_steps=None):
    start = (1, 1)
    queue = deque([(start, 0)])
    visited = {start}
    locations = set()
    
    while queue:
        (x, y), steps = queue.popleft()
        locations.add((x, y))
        
        if (x, y) == (target_x, target_y):
            return steps, len(locations)
        
        if max_steps is not None and steps >= max_steps:
            continue
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not is_wall(nx, ny, seed) and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))
    
    return None, len(locations)

def part1(seed, target_x, target_y):
    steps, _ = solve(seed, target_x, target_y)
    return steps

def part2(seed):
    _, locations = solve(seed, 0, 0, max_steps=50)
    return locations

if __name__ == "__main__":
    seed = 1352
    target_x, target_y = 31, 39
    
    print("Part 1:", part1(seed, target_x, target_y))
    print("Part 2:", part2(seed))