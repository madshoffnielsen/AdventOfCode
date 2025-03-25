from typing import List, Set, Tuple, Dict

Coord = Tuple[int, int]
Tile = Coord
Instructions = List[str]

def read_input(file_path: str) -> List[str]:
    """Read tile flip instructions from file."""
    with open(file_path) as f:
        return [line.strip() for line in f]

def parse_instruction(line: str) -> Instructions:
    """Parse line into list of directions."""
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

def get_coordinates(instructions: Instructions) -> Tile:
    """Convert instructions to axial coordinates."""
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

def get_neighbors(tile: Tile) -> List[Tile]:
    """Get all adjacent hexagonal tiles."""
    q, r = tile
    return [
        (q+1, r), (q-1, r),
        (q, r+1), (q, r-1),
        (q+1, r-1), (q-1, r+1)
    ]

def simulate_day(black_tiles: Set[Tile]) -> Set[Tile]:
    """Simulate one day of tile flipping."""
    counts: Dict[Tile, int] = {}
    
    for tile in black_tiles:
        for neighbor in get_neighbors(tile):
            counts[neighbor] = counts.get(neighbor, 0) + 1
    
    new_black_tiles = set()
    for tile, count in counts.items():
        if tile in black_tiles:
            if count == 1 or count == 2:
                new_black_tiles.add(tile)
        else:
            if count == 2:
                new_black_tiles.add(tile)
    
    return new_black_tiles

def get_initial_state(lines: List[str]) -> Set[Tile]:
    """Flip tiles according to initial instructions."""
    black_tiles: Set[Tile] = set()
    for line in lines:
        instructions = parse_instruction(line)
        coords = get_coordinates(instructions)
        if coords in black_tiles:
            black_tiles.remove(coords)
        else:
            black_tiles.add(coords)
    return black_tiles

def part1(lines: List[str]) -> int:
    """Count black tiles after initial flipping."""
    black_tiles = get_initial_state(lines)
    return len(black_tiles)

def part2(lines: List[str]) -> int:
    """Count black tiles after 100 days."""
    black_tiles = get_initial_state(lines)
    for _ in range(100):
        black_tiles = simulate_day(black_tiles)
    return len(black_tiles)

def main():
    """Main program."""
    print("\n--- Day 24: Lobby Layout ---")
    
    lines = read_input("2020/input/day24.txt")
    
    result1 = part1(lines)
    print(f"Part 1: {result1}")
    
    result2 = part2(lines)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()