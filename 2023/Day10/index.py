from collections import deque

def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

PIPES = {
    '|': [(1,0), (-1,0)],
    '-': [(0,1), (0,-1)],
    'L': [(-1,0), (0,1)],
    'J': [(-1,0), (0,-1)],
    '7': [(1,0), (0,-1)],
    'F': [(1,0), (0,1)],
    '.': [],
    'S': [(1,0), (-1,0), (0,1), (0,-1)]
}

def find_start(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return (i, j)
    return None

def get_connections(grid, pos):
    r, c = pos
    pipe = grid[r][c]
    valid = []
    
    for dr, dc in PIPES[pipe]:
        new_r, new_c = r + dr, c + dc
        if (0 <= new_r < len(grid) and 
            0 <= new_c < len(grid[0])):
            # Check if connection is valid from other side
            other = grid[new_r][new_c]
            if any(new_r + dr2 == r and new_c + dc2 == c 
                  for dr2, dc2 in PIPES[other]):
                valid.append((new_r, new_c))
    return valid

def find_loop(grid):
    start = find_start(grid)
    visited = {start}
    queue = deque([(start, 0)])
    max_dist = 0
    
    while queue:
        pos, dist = queue.popleft()
        max_dist = max(max_dist, dist)
        
        for next_pos in get_connections(grid, pos):
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, dist + 1))
                
    return visited, max_dist

def find_s_type(grid, start, connections):
    r, c = start
    deltas = []
    for nr, nc in connections:
        deltas.append((nr - r, nc - c))
    
    if (1,0) in deltas and (-1,0) in deltas: return '|'
    if (0,1) in deltas and (0,-1) in deltas: return '-'
    if (-1,0) in deltas and (0,1) in deltas: return 'L'
    if (-1,0) in deltas and (0,-1) in deltas: return 'J'
    if (1,0) in deltas and (0,-1) in deltas: return '7'
    if (1,0) in deltas and (0,1) in deltas: return 'F'
    return 'S'

def count_enclosed(grid, loop):
    # Replace S with actual pipe type
    start = find_start(grid)
    connections = [pos for pos in get_connections(grid, start) if pos in loop]
    s_type = find_s_type(grid, start, connections)
    grid = [row[:] for row in grid]
    grid[start[0]][start[1]] = s_type
    
    count = 0
    for r in range(len(grid)):
        inside = False
        last_corner = None
        for c in range(len(grid[0])):
            if (r,c) in loop:
                pipe = grid[r][c]
                if pipe == '|':
                    inside = not inside
                elif pipe in 'LF':
                    last_corner = pipe
                elif pipe in '7J':
                    if (last_corner == 'L' and pipe == '7') or \
                       (last_corner == 'F' and pipe == 'J'):
                        inside = not inside
            elif inside:
                count += 1
    return count

def part1(grid):
    _, max_dist = find_loop(grid)
    return max_dist

def part2(grid):
    loop, _ = find_loop(grid)
    return count_enclosed(grid, loop)

def main():
    grid = read_input("2023/Day10/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()