from typing import List, Tuple

Instruction = Tuple[str, int]

def read_input(file_path: str) -> List[Instruction]:
    """Read navigation instructions from file."""
    with open(file_path) as f:
        return [(line[0], int(line[1:])) for line in f.read().splitlines()]

def rotate(x: int, y: int, degrees: int) -> Tuple[int, int]:
    """Rotate point (x,y) around origin by degrees."""
    for _ in range((degrees % 360) // 90):
        x, y = -y, x
    return x, y

def navigate_part1(instructions: List[Instruction]) -> int:
    """Navigate ship using initial instructions."""
    x, y = 0, 0
    dx, dy = 1, 0  # Facing east
    
    for action, value in instructions:
        match action:
            case 'N': y += value
            case 'S': y -= value
            case 'E': x += value
            case 'W': x -= value
            case 'L': dx, dy = rotate(dx, dy, value)
            case 'R': dx, dy = rotate(dx, dy, -value)
            case 'F':
                x += dx * value
                y += dy * value
            
    return abs(x) + abs(y)

def navigate_part2(instructions: List[Instruction]) -> int:
    """Navigate ship using waypoint instructions."""
    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1  # Waypoint starts 10 east, 1 north
    
    for action, value in instructions:
        match action:
            case 'N': waypoint_y += value
            case 'S': waypoint_y -= value
            case 'E': waypoint_x += value
            case 'W': waypoint_x -= value
            case 'L': waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, value)
            case 'R': waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, -value)
            case 'F':
                ship_x += waypoint_x * value
                ship_y += waypoint_y * value
            
    return abs(ship_x) + abs(ship_y)

def part1(instructions: List[Instruction]) -> int:
    """Calculate Manhattan distance after following first navigation rules."""
    return navigate_part1(instructions)

def part2(instructions: List[Instruction]) -> int:
    """Calculate Manhattan distance after following waypoint rules."""
    return navigate_part2(instructions)

def main():
    """Main program."""
    print("\n--- Day 12: Rain Risk ---")
    
    instructions = read_input("2020/input/day12.txt")
    
    result1 = part1(instructions)
    print(f"Part 1: {result1}")
    
    result2 = part2(instructions)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()