def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def get_adjacent_positions(x, y, max_x, max_y):
    positions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y:
                positions.append((nx, ny))
    return positions

def simulate(grid, minutes):
    max_y = len(grid)
    max_x = len(grid[0])
    
    for _ in range(minutes):
        new_grid = [row[:] for row in grid]
        
        for y in range(max_y):
            for x in range(max_x):
                adjacent = get_adjacent_positions(x, y, max_x, max_y)
                trees = sum(1 for nx, ny in adjacent if grid[ny][nx] == '|')
                lumberyards = sum(1 for nx, ny in adjacent if grid[ny][nx] == '#')
                
                if grid[y][x] == '.' and trees >= 3:
                    new_grid[y][x] = '|'
                elif grid[y][x] == '|' and lumberyards >= 3:
                    new_grid[y][x] = '#'
                elif grid[y][x] == '#' and (lumberyards == 0 or trees == 0):
                    new_grid[y][x] = '.'
        
        grid = new_grid
    
    return grid

def calculate_resource_value(grid):
    trees = sum(row.count('|') for row in grid)
    lumberyards = sum(row.count('#') for row in grid)
    return trees * lumberyards

def part1(grid):
    final_grid = simulate(grid, 10)
    return calculate_resource_value(final_grid)

def part2(grid):
    seen = {}
    max_y = len(grid)
    max_x = len(grid[0])
    minutes = 1000000000
    
    for minute in range(minutes):
        grid_tuple = tuple(tuple(row) for row in grid)
        if grid_tuple in seen:
            cycle_length = minute - seen[grid_tuple]
            remaining_minutes = (minutes - minute) % cycle_length
            for _ in range(remaining_minutes):
                grid = simulate(grid, 1)
            return calculate_resource_value(grid)
        
        seen[grid_tuple] = minute
        grid = simulate(grid, 1)
    
    return calculate_resource_value(grid)

if __name__ == "__main__":
    input_file = "2018/Day18/input.txt"
    grid = read_input(input_file)
    
    result_part1 = part1(grid)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(grid)
    print(f"Part 2: {result_part2}")