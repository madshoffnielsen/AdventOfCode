def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def count_adjacent(grid, row, col):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == '#':
                    count += 1
    return count

def count_visible(grid, row, col):
    count = 0
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] != '.':
                if grid[r][c] == '#':
                    count += 1
                break
            r, c = r + dr, c + dc
    return count

def simulate_step(grid, visible=False, tolerance=4):
    new_grid = [row[:] for row in grid]
    changed = False
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                continue
                
            occupied = count_visible(grid, row, col) if visible else count_adjacent(grid, row, col)
            
            if grid[row][col] == 'L' and occupied == 0:
                new_grid[row][col] = '#'
                changed = True
            elif grid[row][col] == '#' and occupied >= tolerance:
                new_grid[row][col] = 'L'
                changed = True
                
    return new_grid, changed

def count_occupied(grid):
    return sum(row.count('#') for row in grid)

def simulate_until_stable(grid, visible=False, tolerance=4):
    while True:
        grid, changed = simulate_step(grid, visible, tolerance)
        if not changed:
            return count_occupied(grid)

def part1(grid):
    return simulate_until_stable(grid)

def part2(grid):
    return simulate_until_stable(grid, visible=True, tolerance=5)

def main():
    grid = read_input("2020/Day11/input.txt")
    print(f"Part 1: {part1([row[:] for row in grid])}")
    print(f"Part 2: {part2([row[:] for row in grid])}")

if __name__ == "__main__":
    main()