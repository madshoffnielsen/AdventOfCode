def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def find_numbers_with_positions(grid):
    numbers = []
    height, width = len(grid), len(grid[0])
    
    for row in range(height):
        current_num = ''
        start_col = None
        
        for col in range(width + 1):
            if col < width and grid[row][col].isdigit():
                if start_col is None:
                    start_col = col
                current_num += grid[row][col]
            elif current_num:
                numbers.append((int(current_num), row, start_col, col-1))
                current_num = ''
                start_col = None
                
    return numbers

def is_symbol(char):
    return not (char.isdigit() or char == '.')

def is_adjacent_to_symbol(grid, row, start_col, end_col):
    height, width = len(grid), len(grid[0])
    
    for r in range(max(0, row-1), min(height, row+2)):
        for c in range(max(0, start_col-1), min(width, end_col+2)):
            if is_symbol(grid[r][c]):
                return True
    return False

def find_gear_ratios(grid, numbers):
    height, width = len(grid), len(grid[0])
    gears = {}
    
    for num, row, start_col, end_col in numbers:
        for r in range(max(0, row-1), min(height, row+2)):
            for c in range(max(0, start_col-1), min(width, end_col+2)):
                if grid[r][c] == '*':
                    gear_pos = (r, c)
                    if gear_pos not in gears:
                        gears[gear_pos] = []
                    gears[gear_pos].append(num)
    
    return sum(nums[0] * nums[1] 
              for nums in gears.values() 
              if len(nums) == 2)

def part1(grid):
    numbers = find_numbers_with_positions(grid)
    return sum(num for num, row, start, end in numbers 
              if is_adjacent_to_symbol(grid, row, start, end))

def part2(grid):
    numbers = find_numbers_with_positions(grid)
    return find_gear_ratios(grid, numbers)

def main():
    grid = read_input("2023/Day03/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()