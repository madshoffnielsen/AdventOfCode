from collections import defaultdict

def parse_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def biodiversity_rating(grid):
    rating = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                rating += 2 ** (y * len(grid[0]) + x)
    return rating

def evolve(grid):
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            neighbors = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if grid[ny][nx] == '#':
                        neighbors += 1
            if grid[y][x] == '#' and neighbors != 1:
                new_grid[y][x] = '.'
            elif grid[y][x] == '.' and neighbors in (1, 2):
                new_grid[y][x] = '#'
            else:
                new_grid[y][x] = grid[y][x]
    return new_grid

def find_repeating_biodiversity(grid):
    seen = set()
    while True:
        rating = biodiversity_rating(grid)
        if rating in seen:
            return rating
        seen.add(rating)
        grid = evolve(grid)

def evolve_recursive(grids):
    new_grids = defaultdict(lambda: [['.' for _ in range(5)] for _ in range(5)])
    min_level = min(grids.keys())
    max_level = max(grids.keys())
    
    for level in range(min_level - 1, max_level + 2):
        for y in range(5):
            for x in range(5):
                if (x, y) == (2, 2):
                    continue
                neighbors = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx == 2 and ny == 2:
                        if dx == -1:
                            neighbors += sum(1 for i in range(5) if grids[level + 1][i][4] == '#')
                        elif dx == 1:
                            neighbors += sum(1 for i in range(5) if grids[level + 1][i][0] == '#')
                        elif dy == -1:
                            neighbors += sum(1 for i in range(5) if grids[level + 1][4][i] == '#')
                        elif dy == 1:
                            neighbors += sum(1 for i in range(5) if grids[level + 1][0][i] == '#')
                    elif 0 <= nx < 5 and 0 <= ny < 5:
                        if grids[level][ny][nx] == '#':
                            neighbors += 1
                    else:
                        if grids[level - 1][2 + dy][2 + dx] == '#':
                            neighbors += 1
                if grids[level][y][x] == '#' and neighbors != 1:
                    new_grids[level][y][x] = '.'
                elif grids[level][y][x] == '.' and neighbors in (1, 2):
                    new_grids[level][y][x] = '#'
                else:
                    new_grids[level][y][x] = grids[level][y][x]
    return new_grids

def count_bugs(grids):
    return sum(row.count('#') for grid in grids.values() for row in grid)

# Read input
initial_grid = parse_input('2019/Day24/input.txt')

# Part 1: Find repeating biodiversity rating
result1 = find_repeating_biodiversity(initial_grid)
print(f"Part 1: {result1}")

# Part 2: Simulate recursive grids for 200 minutes
grids = defaultdict(lambda: [['.' for _ in range(5)] for _ in range(5)])
grids[0] = initial_grid

for _ in range(200):
    grids = evolve_recursive(grids)

result2 = count_bugs(grids)
print(f"Part 2: {result2}")