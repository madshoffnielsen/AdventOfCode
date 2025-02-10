def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def count_neighbors_on(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '#':
            count += 1
    return count

def simulate(grid, steps, part2=False):
    for _ in range(steps):
        new_grid = [['.'] * len(grid[0]) for _ in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                neighbors_on = count_neighbors_on(grid, x, y)
                if grid[x][y] == '#' and neighbors_on in [2, 3]:
                    new_grid[x][y] = '#'
                elif grid[x][y] == '.' and neighbors_on == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = '.'
        if part2:
            new_grid[0][0] = new_grid[0][-1] = new_grid[-1][0] = new_grid[-1][-1] = '#'
        grid = new_grid
    return grid

def count_lights_on(grid):
    return sum(row.count('#') for row in grid)

def part1(grid):
    final_grid = simulate(grid, 100)
    return count_lights_on(final_grid)

def part2(grid):
    grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = '#'
    final_grid = simulate(grid, 100, part2=True)
    return count_lights_on(final_grid)

def main():
    grid = read_input("2015/Day18/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()