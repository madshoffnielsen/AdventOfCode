def calculate_risk_levels(filename):
    with open(filename, 'r') as file:
        heightmap = [list(map(int, line.strip())) for line in file if line.strip()]
    
    rows, cols = len(heightmap), len(heightmap[0])
    total_risk_level = 0
    
    for i in range(rows):
        for j in range(cols):
            current = heightmap[i][j]
            is_low_point = True
            
            if i > 0 and heightmap[i - 1][j] <= current:
                is_low_point = False
            if i < rows - 1 and heightmap[i + 1][j] <= current:
                is_low_point = False
            if j > 0 and heightmap[i][j - 1] <= current:
                is_low_point = False
            if j < cols - 1 and heightmap[i][j + 1] <= current:
                is_low_point = False
            
            if is_low_point:
                total_risk_level += current + 1
    
    return total_risk_level

def flood_fill(i, j, heightmap, visited, rows, cols):
    stack = [(i, j)]
    size = 0
    
    while stack:
        x, y = stack.pop()
        if visited[x][y] or heightmap[x][y] == 9:
            continue
        
        visited[x][y] = True
        size += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and heightmap[new_x][new_y] != 9:
                stack.append((new_x, new_y))
    
    return size

def find_basins(filename):
    with open(filename, 'r') as file:
        heightmap = [list(map(int, line.strip())) for line in file if line.strip()]
    
    rows, cols = len(heightmap), len(heightmap[0])
    basins = []
    visited = [[False] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            current = heightmap[i][j]
            is_low_point = True
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if heightmap[new_x][new_y] <= current:
                        is_low_point = False
                        break
            
            if is_low_point:
                basin_size = flood_fill(i, j, heightmap, visited, rows, cols)
                basins.append(basin_size)
    
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]

def main():
    print("\n--- Day 9: Smoke Basin ---")
    input_file = '2021/input/day09.txt'
    risk_level = calculate_risk_levels(input_file)
    print(f"Part 1: {risk_level}")

    basin_product = find_basins(input_file)
    print(f"Part 2: {basin_product}")

if __name__ == "__main__":
    main() 