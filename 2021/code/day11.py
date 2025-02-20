def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [[int(char) for char in line.strip()] for line in file if line.strip()]

def get_neighbors(x, y, grid):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors

def simulate_step(grid):
    flashes = 0
    to_flash = []
    flashed = set()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1
            if grid[x][y] > 9:
                to_flash.append((x, y))

    while to_flash:
        x, y = to_flash.pop()
        if (x, y) in flashed:
            continue
        flashed.add((x, y))
        flashes += 1

        for nx, ny in get_neighbors(x, y, grid):
            grid[nx][ny] += 1
            if grid[nx][ny] > 9 and (nx, ny) not in flashed:
                to_flash.append((nx, ny))

    for x, y in flashed:
        grid[x][y] = 0

    return flashes

def simulate_octopuses(grid, steps):
    total_flashes = 0
    for _ in range(steps):
        total_flashes += simulate_step(grid)
    return total_flashes

def find_synchronization_step(grid):
    step = 0
    total_octopuses = len(grid) * len(grid[0])

    while True:
        step += 1
        if simulate_step(grid) == total_octopuses:
            return step

def main():
    print("\n--- Day 11: Dumbo Octopus ---")
    input_file = '2021/input/day11.txt'
    grid = parse_input(input_file)
    print(f"Part 1: {simulate_octopuses(grid, 100)}")

    grid = parse_input(input_file)
    print(f"Part 2: {find_synchronization_step(grid)}")

if __name__ == "__main__": 
    main()