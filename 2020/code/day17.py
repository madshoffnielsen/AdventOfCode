from itertools import product
from typing import Set, Tuple

Coord = Tuple[int, ...]
State = Set[Coord]

def read_input(file_path: str) -> State:
    """Read initial cube state from file."""
    with open(file_path) as f:
        lines = f.read().strip().split("\n")
    return {
        (x, y, 0, 0)  # Add z and w dimensions
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "#"
    }

def get_neighbors(coord: Coord, dimensions: int) -> State:
    """Generate all neighbors of a coordinate."""
    deltas = product([-1, 0, 1], repeat=dimensions)
    return {
        tuple(c + d for c, d in zip(coord, delta))
        for delta in deltas
        if any(delta)  # Exclude the coordinate itself
    }

def simulate(initial_state: State, dimensions: int, cycles: int = 6) -> int:
    """Simulate Conway Cubes."""
    active = {tuple(c[:dimensions]) for c in initial_state}

    for _ in range(cycles):
        new_active = set()
        candidates = active | {n for cube in active for n in get_neighbors(cube, dimensions)}

        for cube in candidates:
            neighbors = get_neighbors(cube, dimensions)
            active_neighbors = len(neighbors & active)

            if cube in active:
                if active_neighbors in [2, 3]:
                    new_active.add(cube)
            else:
                if active_neighbors == 3:
                    new_active.add(cube)

        active = new_active

    return len(active)

def part1(initial_state: State) -> int:
    """Simulate in 3D space."""
    return simulate(initial_state, dimensions=3)

def part2(initial_state: State) -> int:
    """Simulate in 4D space."""
    return simulate(initial_state, dimensions=4)

def main():
    """Main program."""
    print("\n--- Day 17: Conway Cubes ---")
    
    initial_state = read_input("2020/input/day17.txt")
    
    result1 = part1(initial_state)
    print(f"Part 1: {result1}")
    
    result2 = part2(initial_state)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()