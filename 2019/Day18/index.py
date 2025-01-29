from collections import deque, defaultdict
from heapq import heappush, heappop
import string

def read_input(filename):
    """Read and parse the maze from input file."""
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def find_start_and_keys(maze):
    """Find the starting position and all keys in the maze."""
    height, width = len(maze), len(maze[0])
    keys = {}
    start = None
    
    for y in range(height):
        for x in range(width):
            if maze[y][x] == '@':
                start = (x, y)
            elif maze[y][x] in string.ascii_lowercase:
                keys[maze[y][x]] = (x, y)
                
    return start, keys

def get_neighbors(pos, maze):
    """Get valid neighboring positions."""
    x, y = pos
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
            if maze[new_y][new_x] != '#':
                yield (new_x, new_y)

def find_reachable_keys(start, maze, collected_keys):
    """Find all reachable keys from current position and the keys needed to reach them."""
    queue = deque([(start, 0, set())])
    visited = {start}
    reachable_keys = {}
    
    while queue:
        pos, dist, doors = queue.popleft()
        x, y = pos
        current = maze[y][x]
        
        # If we found a key we don't have yet
        if current in string.ascii_lowercase and current not in collected_keys:
            reachable_keys[current] = (dist, doors)
            continue
            
        for next_pos in get_neighbors(pos, maze):
            if next_pos not in visited:
                nx, ny = next_pos
                cell = maze[ny][nx]
                
                # If it's a door and we don't have the key, add it to required doors
                new_doors = doors.copy()
                if cell in string.ascii_uppercase and cell.lower() not in collected_keys:
                    new_doors.add(cell.lower())
                    
                visited.add(next_pos)
                queue.append((next_pos, dist + 1, new_doors))
                
    return reachable_keys

def find_shortest_path(maze):
    """Find the shortest path to collect all keys."""
    start, keys = find_start_and_keys(maze)
    total_keys = len(keys)
    
    # Priority queue: (distance, position, collected_keys)
    queue = [(0, start, frozenset())]
    # Cache for visited states
    seen = {}
    
    while queue:
        dist, pos, collected = heappop(queue)
        
        # If we've collected all keys, we're done
        if len(collected) == total_keys:
            return dist
            
        # Skip if we've seen this state with a better distance
        state = (pos, collected)
        if state in seen and seen[state] <= dist:
            continue
        seen[state] = dist
        
        # Find reachable keys from current position
        reachable = find_reachable_keys(pos, maze, collected)
        
        # Try collecting each reachable key
        for key, (key_dist, required_keys) in reachable.items():
            if not required_keys:  # If we can reach the key
                new_collected = frozenset([key]).union(collected)
                new_pos = keys[key]
                new_dist = dist + key_dist
                heappush(queue, (new_dist, new_pos, new_collected))
                
    return float('inf')

def solve_part1(filename):
    """Solve part 1 of the puzzle."""
    maze = read_input(filename)
    return find_shortest_path(maze)

def modify_maze_for_part2(maze, start):
    """Modify the maze for part 2 by creating four separate quadrants."""
    x, y = start
    # Replace the center 3x3 area with walls and new starting positions
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            maze[y + dy][x + dx] = '#'
    # Add the four new starting positions
    maze[y-1][x-1] = '@'
    maze[y-1][x+1] = '@'
    maze[y+1][x-1] = '@'
    maze[y+1][x+1] = '@'
    return maze

def find_shortest_path_part2(maze):
    """Find shortest path for part 2 with four robots."""
    # Find all starts and keys
    starts = []
    keys = {}
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == '@':
                starts.append((x, y))
            elif maze[y][x] in string.ascii_lowercase:
                keys[maze[y][x]] = (x, y)
    
    total_keys = len(keys)
    # Priority queue: (distance, positions, collected_keys)
    queue = [(0, tuple(starts), frozenset())]
    seen = {}
    
    while queue:
        dist, positions, collected = heappop(queue)
        
        if len(collected) == total_keys:
            return dist
            
        state = (positions, collected)
        if state in seen and seen[state] <= dist:
            continue
        seen[state] = dist
        
        # Try moving each robot
        for i, pos in enumerate(positions):
            reachable = find_reachable_keys(pos, maze, collected)
            
            for key, (key_dist, required_keys) in reachable.items():
                if not required_keys:
                    new_collected = frozenset([key]).union(collected)
                    new_positions = list(positions)
                    new_positions[i] = keys[key]
                    new_dist = dist + key_dist
                    heappush(queue, (new_dist, tuple(new_positions), new_collected))
    
    return float('inf')

def solve_part2(filename):
    """Solve part 2 of the puzzle."""
    maze = read_input(filename)
    start, _ = find_start_and_keys(maze)
    maze = modify_maze_for_part2(maze, start)
    return find_shortest_path_part2(maze)


filename = "2019/Day18/input.txt"
print(f"Part 1: {solve_part1(filename)}")
print(f"Part 2: {solve_part2(filename)}")