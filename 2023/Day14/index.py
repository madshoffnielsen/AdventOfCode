def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def tilt_north(grid):
    height, width = len(grid), len(grid[0])
    for col in range(width):
        stop = 0
        for row in range(height):
            if grid[row][col] == '#':
                stop = row + 1
            elif grid[row][col] == 'O':
                grid[row][col] = '.'
                grid[stop][col] = 'O'
                stop += 1
    return grid

def rotate_grid(grid):
    return list(map(list, zip(*grid[::-1])))

def cycle(grid):
    # North, West, South, East
    for _ in range(4):
        grid = tilt_north(grid)
        grid = rotate_grid(grid)
    return grid

def calculate_load(grid):
    height = len(grid)
    return sum((height - r) * row.count('O') for r, row in enumerate(grid))

def grid_to_string(grid):
    return '\n'.join(''.join(row) for row in grid)

def part1(grid):
    return calculate_load(tilt_north([row[:] for row in grid]))

def part2(grid):
    seen = {}
    grid = [row[:] for row in grid]
    target = 1000000000
    
    for i in range(target):
        grid_str = grid_to_string(grid)
        if grid_str in seen:
            cycle_length = i - seen[grid_str]
            remaining = (target - i) % cycle_length
            for _ in range(remaining):
                grid = cycle(grid)
            break
        
        seen[grid_str] = i
        grid = cycle(grid)
    
    return calculate_load(grid)

def main():
    grid = read_input("2023/Day14/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()