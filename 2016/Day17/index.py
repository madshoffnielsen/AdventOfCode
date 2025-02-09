import hashlib
from collections import deque

def get_doors(passcode, path):
    hash_result = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
    return [c in 'bcdef' for c in hash_result]

def bfs_shortest_path(passcode):
    queue = deque([((0, 0), "")])
    directions = ['U', 'D', 'L', 'R']
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == (3, 3):
            return path
        
        doors = get_doors(passcode, path)
        
        for i, (dx, dy) in enumerate(moves):
            if doors[i]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    queue.append(((nx, ny), path + directions[i]))
    
    return None

def bfs_longest_path(passcode):
    queue = deque([((0, 0), "")])
    directions = ['U', 'D', 'L', 'R']
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    longest_path_length = 0
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == (3, 3):
            longest_path_length = max(longest_path_length, len(path))
            continue
        
        doors = get_doors(passcode, path)
        
        for i, (dx, dy) in enumerate(moves):
            if doors[i]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    queue.append(((nx, ny), path + directions[i]))
    
    return longest_path_length

def part1(passcode):
    return bfs_shortest_path(passcode)

def part2(passcode):
    return bfs_longest_path(passcode)

if __name__ == "__main__":
    passcode = "dmypynyp"
    print("Part 1:", part1(passcode))
    print("Part 2:", part2(passcode))