def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def count_trees(grid, right, down):
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

def part1(grid):
    return count_trees(grid, 3, 1)

def part2(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    
    for right, down in slopes:
        result *= count_trees(grid, right, down)
    
    return result

def main():
    grid = read_input("2020/Day03/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()