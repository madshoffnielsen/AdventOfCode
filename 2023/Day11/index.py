def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def find_galaxies(grid):
    galaxies = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                galaxies.append((r, c))
    return galaxies

def find_empty_space(grid):
    empty_rows = [r for r in range(len(grid)) 
                 if all(cell == '.' for cell in grid[r])]
    empty_cols = [c for c in range(len(grid[0])) 
                 if all(row[c] == '.' for row in grid)]
    return empty_rows, empty_cols

def calculate_distances(galaxies, empty_rows, empty_cols, expansion_factor):
    total = 0
    expansion = expansion_factor - 1
    
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[i+1:]:
            min_r, max_r = min(r1, r2), max(r1, r2)
            min_c, max_c = min(c1, c2), max(c1, c2)
            
            # Count expanded rows and columns between galaxies
            expanded_rows = sum(1 for r in empty_rows if min_r < r < max_r)
            expanded_cols = sum(1 for c in empty_cols if min_c < c < max_c)
            
            # Calculate Manhattan distance with expansion
            distance = (max_r - min_r) + (max_c - min_c) + \
                      (expanded_rows + expanded_cols) * expansion
            total += distance
            
    return total

def solve(grid, expansion_factor):
    galaxies = find_galaxies(grid)
    empty_rows, empty_cols = find_empty_space(grid)
    return calculate_distances(galaxies, empty_rows, empty_cols, expansion_factor)

def main():
    grid = read_input("2023/Day11/input.txt")
    print(f"Part 1: {solve(grid, 2)}")
    print(f"Part 2: {solve(grid, 1000000)}")

if __name__ == "__main__":
    main()