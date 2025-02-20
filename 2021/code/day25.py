def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return input_data

def parse_input(input_data):
    lines = input_data.split('\n')
    return [list(line) for line in lines]

def move_sea_cucumbers(grid):
    rows, cols = len(grid), len(grid[0])
    steps = 0
    moved = True

    while moved:
        steps += 1
        moved = False
        new_grid = [row[:] for row in grid]

        # Move east-facing sea cucumbers
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '>' and grid[r][(c + 1) % cols] == '.':
                    new_grid[r][c] = '.'
                    new_grid[r][(c + 1) % cols] = '>'
                    moved = True

        grid = [row[:] for row in new_grid]

        # Move south-facing sea cucumbers
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'v' and grid[(r + 1) % rows][c] == '.':
                    new_grid[r][c] = '.'
                    new_grid[(r + 1) % rows][c] = 'v'
                    moved = True

        grid = new_grid

    return steps

def main():
    print("\n--- Day 25: Sea Cucumber ---")
    input_file = '2021/input/day25.txt'
    input_data = read_input(input_file)
    grid = parse_input(input_data)

    result = move_sea_cucumbers(grid)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    main()