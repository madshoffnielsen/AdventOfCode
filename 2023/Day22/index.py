import re
from collections import defaultdict

def parse_input(file_path):
    bricks = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)', line.strip())
            if match:
                x1, y1, z1, x2, y2, z2 = map(int, match.groups())
                bricks.append(((x1, y1, z1), (x2, y2, z2)))
    return bricks

def get_brick_positions(start, end):
    x1, y1, z1 = start
    x2, y2, z2 = end
    positions = []
    
    if x1 != x2:
        positions = [(x, y1, z1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif y1 != y2:
        positions = [(x1, y, z1) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif z1 != z2:
        positions = [(x1, y1, z) for z in range(min(z1, z2), max(z1, z2) + 1)]
    else:
        positions = [(x1, y1, z1)]
    
    return positions

def settle_bricks(bricks):
    brick_positions = {}  # Maps brick index to set of occupied positions
    occupied = {}  # Maps (x, y, z) to brick index
    
    sorted_bricks = sorted(enumerate(bricks), key=lambda b: min(b[1][0][2], b[1][1][2]))
    
    for i, (start, end) in sorted_bricks:
        positions = get_brick_positions(start, end)
        
        min_z = min(p[2] for p in positions)
        drop = min_z - 1
        
        while drop > 0 and all((p[0], p[1], p[2] - (min_z - drop)) not in occupied for p in positions):
            drop -= 1
        
        drop += 1  # Undo last failed check
        
        new_positions = [(p[0], p[1], p[2] - (min_z - drop)) for p in positions]
        
        brick_positions[i] = set(new_positions)
        for pos in new_positions:
            occupied[pos] = i
    
    return brick_positions, occupied

def find_safe_disintegrations(brick_positions, occupied):
    supports = defaultdict(set)
    supported_by = defaultdict(set)
    
    for i, positions in brick_positions.items():
        for x, y, z in positions:
            below = (x, y, z - 1)
            if below in occupied and occupied[below] != i:
                supports[occupied[below]].add(i)
                supported_by[i].add(occupied[below])
    
    safe_count = 0
    for i in brick_positions:
        if all(len(supported_by[above]) > 1 for above in supports[i]):
            safe_count += 1
    
    return safe_count

def count_falling_bricks(brick_positions, occupied):
    supports = defaultdict(set)
    supported_by = defaultdict(set)
    
    for i, positions in brick_positions.items():
        for x, y, z in positions:
            below = (x, y, z - 1)
            if below in occupied and occupied[below] != i:
                supports[occupied[below]].add(i)
                supported_by[i].add(occupied[below])
    
    total_falling = 0
    for i in brick_positions:
        to_check = {i}
        falling = set()
        while to_check:
            brick = to_check.pop()
            falling.add(brick)
            for above in supports[brick]:
                if supported_by[above] <= falling:
                    to_check.add(above)
        total_falling += len(falling) - 1  # Exclude the initial brick
    
    return total_falling

def main():
    file_path = "2023/Day22/input.txt"
    bricks = parse_input(file_path)
    brick_positions, occupied = settle_bricks(bricks)
    safe_count = find_safe_disintegrations(brick_positions, occupied)
    total_falling = count_falling_bricks(brick_positions, occupied)
    print("Part 1:", safe_count)
    print("Part 2:", total_falling)

if __name__ == "__main__":
    main()