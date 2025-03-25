from typing import List, Tuple

def read_input(file_path: str) -> List[str]:
    """Read and parse input file into a grid of characters."""
    with open(file_path) as f:
        return [line.strip() for line in f]

def count_trees(grid: List[str], right: int, down: int) -> int:
    """Count trees encountered while sledding down the slope."""
    width = len(grid[0])
    height = len(grid)
    x, y = 0, 0
    trees = 0
    
    while y < height:
        if grid[y][x % width] == '#':
            trees += 1
        x += right
        y += down
    
    return trees

def part1(grid: List[str]) -> int:
    """Solve part 1: Count trees encountered on slope (3, 1)."""
    return count_trees(grid, 3, 1)

def part2(grid: List[str]) -> int:
    """Solve part 2: Multiply tree counts for different slopes."""
    slopes: List[Tuple[int, int]] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    
    for right, down in slopes:
        result *= count_trees(grid, right, down)
    
    return result

def main():
    """Main program."""
    # Print header
    print("\n--- Day 3: Toboggan Trajectory ---")
    
    # Read input
    grid = read_input("2020/input/day03.txt")
    
    # Part 1
    result1 = part1(grid)
    print(f"Part 1: {result1}")
    
    # Part 2
    result2 = part2(grid)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()