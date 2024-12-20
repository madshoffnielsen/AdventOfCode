from itertools import product

def parse_input(filename):
    """Parse the initial state from the input file."""
    with open(filename) as f:
        lines = f.read().strip().split("\n")
    return {
        (x, y, 0, 0)  # Add z and w dimensions
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "#"
    }


def get_neighbors(coord, dimensions):
    """Generate all neighbors of a given coordinate in n dimensions."""
    deltas = product([-1, 0, 1], repeat=dimensions)
    return {
        tuple(c + d for c, d in zip(coord, delta))
        for delta in deltas
        if any(delta)  # Exclude the coordinate itself
    }


def simulate(initial_state, dimensions, cycles=6):
    """Simulate the Conway Cubes for a given number of cycles."""
    active = {tuple(c[:dimensions]) for c in initial_state}

    for _ in range(cycles):
        new_active = set()
        candidates = active | {n for cube in active for n in get_neighbors(cube, dimensions)}

        for cube in candidates:
            neighbors = get_neighbors(cube, dimensions)
            active_neighbors = len(neighbors & active)

            if cube in active and active_neighbors in [2, 3]:
                new_active.add(cube)
            elif cube not in active and active_neighbors == 3:
                new_active.add(cube)

        active = new_active

    return len(active)


def solve(filename):
    initial_state = parse_input(filename)

    # Part 1: 3D simulation
    part1_result = simulate(initial_state, dimensions=3)

    # Part 2: 4D simulation
    part2_result = simulate(initial_state, dimensions=4)

    return part1_result, part2_result


# Run the solution
filename = "2020/Day17/input.txt"
part1, part2 = solve(filename)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
