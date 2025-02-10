def parse_instruction(line):
    directions = []
    i = 0
    while i < len(line):
        if line[i] in 'ns':
            directions.append(line[i:i+2])
            i += 2
        else:
            directions.append(line[i])
            i += 1
    return directions

def get_coordinates(instructions):
    # Using axial coordinates (q,r) for hexagonal grid
    directions = {
        'e': (1, 0),
        'se': (0, 1),
        'sw': (-1, 1),
        'w': (-1, 0),
        'nw': (0, -1),
        'ne': (1, -1)
    }
    
    q, r = 0, 0
    for direction in instructions:
        dq, dr = directions[direction]
        q += dq
        r += dr
    return (q, r)

def get_neighbors(tile):
    q, r = tile
    return [
        (q+1, r), (q-1, r),
        (q, r+1), (q, r-1),
        (q+1, r-1), (q-1, r+1)
    ]

def simulate_day(black_tiles):
    counts = {}
    
    # Count black neighbors for each relevant tile
    for tile in black_tiles:
        for neighbor in get_neighbors(tile):
            counts[neighbor] = counts.get(neighbor, 0) + 1
    
    new_black_tiles = set()
    
    # Apply rules
    for tile, count in counts.items():
        if tile in black_tiles:
            if count == 1 or count == 2:
                new_black_tiles.add(tile)
        else:
            if count == 2:
                new_black_tiles.add(tile)
    
    return new_black_tiles

def solve(input_file):
    # Read and parse input
    with open(input_file) as f:
        lines = f.readlines()
    
    # Part 1: Initial tile flipping
    black_tiles = set()
    for line in lines:
        instructions = parse_instruction(line.strip())
        coords = get_coordinates(instructions)
        if coords in black_tiles:
            black_tiles.remove(coords)
        else:
            black_tiles.add(coords)
    
    part1 = len(black_tiles)
    
    # Part 2: Conway-like simulation
    for _ in range(100):
        black_tiles = simulate_day(black_tiles)
    
    part2 = len(black_tiles)
    
    return part1, part2

def main():
    part1, part2 = solve("2020/Day24/input.txt")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()