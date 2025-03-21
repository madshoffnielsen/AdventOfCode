def read_input(file_path):
    """Reads and parses the input file."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split(','))) for line in file.readlines()]

def calculate_surface_area(cubes):
    """Calculates the surface area of the cubes (Part 1)."""
    cube_set = set()
    max_coords = [0, 0, 0]
    min_coords = [20, 20, 20]

    def cube_dist(c1, c2):
        return sum(abs(c1[i] - c2[i]) for i in range(3))

    surface_area = 0
    for c1 in cubes:
        cube_set.add(tuple(c1))
        max_coords = [max(max_coords[i], c1[i] + 1) for i in range(3)]
        min_coords = [min(min_coords[i], c1[i] - 1) for i in range(3)]
        surface_area += 6 - sum(1 for c2 in cubes if cube_dist(c1, c2) == 1)

    return surface_area, cube_set, min_coords, max_coords

def spread_water(min_coords, max_coords, cube_set):
    """Spreads water cubes (Part 2) using an iterative approach."""
    dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    processed = set()
    water = []

    def in_range(cube):
        return all(min_coords[i] <= cube[i] <= max_coords[i] for i in range(3))

    def add_cube(c1, c2):
        return [c1[i] + c2[i] for i in range(3)]

    # Use a stack to simulate recursion
    stack = [min_coords]
    while stack:
        cube = stack.pop()
        if tuple(cube) in processed:
            continue
        processed.add(tuple(cube))
        water.append(cube)
        for d in dirs:
            target_cube = add_cube(cube, d)
            if in_range(target_cube) and tuple(target_cube) not in cube_set and tuple(target_cube) not in processed:
                stack.append(target_cube)

    return water

def calculate_water_surface(water, cubes):
    """Calculates the surface area of water cubes touching normal cubes."""
    def cube_dist(c1, c2):
        return sum(abs(c1[i] - c2[i]) for i in range(3))

    return sum(sum(1 for c2 in cubes if cube_dist(c1, c2) == 1) for c1 in water)

def main():
    print("\n--- Day 18: Boiling Boulders ---")
    cubes = read_input("2022/input/day18.txt")

    # Part 1
    surface_area, cube_set, min_coords, max_coords = calculate_surface_area(cubes)
    print(f"Part 1: {surface_area}")

    # Part 2
    water = spread_water(min_coords, max_coords, cube_set)
    water_surface_area = calculate_water_surface(water, cubes)
    print(f"Part 2: {water_surface_area}")

if __name__ == "__main__":
    main()