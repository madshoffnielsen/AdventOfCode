def parse_input(filename):
    """Reads input file and returns a list of (direction, steps) tuples."""
    with open(filename, "r") as f:
        return [(line[0], int(line[2:])) for line in f.read().strip().split("\n")]

def move_knot(knot, target):
    """Moves a knot towards the target knot if they are not adjacent."""
    x, y = knot
    tx, ty = target

    if abs(x - tx) > 1 or abs(y - ty) > 1:
        x += (tx - x) // abs(tx - x) if tx != x else 0
        y += (ty - y) // abs(ty - y) if ty != y else 0

    return (x, y)

def simulate_rope(movements, knot_count):
    """Simulates the movement of the rope with given knots and returns unique tail positions."""
    rope = [(0, 0)] * knot_count  # Initialize all knots at (0,0)
    visited = set()
    
    direction_map = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    
    for direction, steps in movements:
        dx, dy = direction_map[direction]

        for _ in range(steps):
            rope[0] = (rope[0][0] + dx, rope[0][1] + dy)  # Move head
            
            for i in range(1, knot_count):
                rope[i] = move_knot(rope[i], rope[i - 1])  # Move each knot
            
            visited.add(rope[-1])  # Track tail position
    
    return len(visited)

def part1(movements):
    return simulate_rope(movements, knot_count=2)

def part2(movements):
    return simulate_rope(movements, knot_count=10)

# Main Execution
if __name__ == "__main__":
    print("\n--- Day 9: Rope Bridge ---")
    movements = parse_input("2022/input/day09.txt")
    
    print("Part 1:", part1(movements))
    print("Part 2:", part2(movements))
