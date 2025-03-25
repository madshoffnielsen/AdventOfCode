from typing import List, Tuple, Set
from copy import deepcopy

Grid = List[List[str]]

def read_input(file_path: str) -> Grid:
    """Read seating layout from input file."""
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def count_adjacent(grid: Grid, row: int, col: int) -> int:
    """Count occupied seats adjacent to given position."""
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

def count_visible(grid: Grid, row: int, col: int) -> int:
    """Count visible occupied seats from given position."""
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

def simulate_step(grid: Grid, visible: bool = False, tolerance: int = 4) -> Tuple[Grid, bool]:
    """Simulate one step of seating changes."""
    new_grid = deepcopy(grid)
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

def count_occupied(grid: Grid) -> int:
    """Count total occupied seats in grid."""
    return sum(row.count('#') for row in grid)

def simulate_until_stable(grid: Grid, visible: bool = False, tolerance: int = 4) -> int:
    """Simulate until no more changes occur."""
    while True:
        grid, changed = simulate_step(grid, visible, tolerance)
        if not changed:
            return count_occupied(grid)

def part1(grid: Grid) -> int:
    """Calculate stable occupied seats using adjacent rule."""
    return simulate_until_stable(grid)

def part2(grid: Grid) -> int:
    """Calculate stable occupied seats using visibility rule."""
    return simulate_until_stable(grid, visible=True, tolerance=5)

def main():
    """Main program."""
    print("\n--- Day 11: Seating System ---")
    
    grid = read_input("2020/input/day11.txt")
    
    result1 = part1(deepcopy(grid))
    print(f"Part 1: {result1}")
    
    result2 = part2(deepcopy(grid))
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()