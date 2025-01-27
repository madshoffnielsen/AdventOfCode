from collections import defaultdict, deque

def parse_input(filename):
    with open(filename) as f:
        return [list(line.rstrip('\n')) for line in f]

def find_portals(maze):
    portals = defaultdict(list)
    height, width = len(maze), len(maze[0])
    
    # Find all portal labels
    for y in range(height):
        for x in range(width):
            if maze[y][x].isupper():
                # Check horizontal portal
                if x+1 < width and maze[y][x+1].isupper():
                    label = maze[y][x] + maze[y][x+1]
                    # Check if portal is on left or right
                    if x+2 < width and maze[y][x+2] == '.':
                        portals[label].append((x+2, y))
                    elif x-1 >= 0 and maze[y][x-1] == '.':
                        portals[label].append((x-1, y))
                # Check vertical portal
                elif y+1 < height and maze[y+1][x].isupper():
                    label = maze[y][x] + maze[y+1][x]
                    # Check if portal is above or below
                    if y+2 < height and maze[y+2][x] == '.':
                        portals[label].append((x, y+2))
                    elif y-1 >= 0 and maze[y-1][x] == '.':
                        portals[label].append((x, y-1))
    return portals

def get_neighbors(pos, maze, portals, recursive=False):
    x, y, level = pos if recursive else (*pos, 0)
    height, width = len(maze), len(maze[0])
    neighbors = []
    
    # Regular moves
    for nx, ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '.':
            if recursive:
                neighbors.append((nx, ny, level))
            else:
                neighbors.append((nx, ny))
    
    # Portal moves
    for label, positions in portals.items():
        if label not in ('AA', 'ZZ') and (x,y) in positions:
            dest = positions[1] if (x,y) == positions[0] else positions[0]
            if recursive:
                # Check if outer or inner portal
                is_outer = (x in (2, width-3) or y in (2, height-3))
                if is_outer and level == 0:
                    continue
                new_level = level + (-1 if is_outer else 1)
                if new_level >= 0:
                    neighbors.append((*dest, new_level))
            else:
                neighbors.append(dest)
                
    return neighbors

def shortest_path(maze, portals, recursive=False):
    start = (*portals['AA'][0], 0) if recursive else portals['AA'][0]
    end = (*portals['ZZ'][0], 0) if recursive else portals['ZZ'][0]
    
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        pos, steps = queue.popleft()
        if pos == end:
            return steps
            
        for next_pos in get_neighbors(pos, maze, portals, recursive):
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))
    
    return float('inf')

# Read and parse input
maze = parse_input('2019/Day20/input.txt')
portals = find_portals(maze)

# Part 1: Find shortest path through regular maze
result1 = shortest_path(maze, portals)
print(f"Part 1: {result1}")

# Part 2: Find shortest path through recursive maze
result2 = shortest_path(maze, portals, recursive=True)
print(f"Part 2: {result2}")