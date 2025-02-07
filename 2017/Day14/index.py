def knot_hash_round(numbers, lengths, pos=0, skip=0):
    n = len(numbers)
    for length in lengths:
        start = pos
        sublist = []
        for i in range(length):
            sublist.append(numbers[(start + i) % n])
        sublist.reverse()
        for i in range(length):
            numbers[(start + i) % n] = sublist[i]
        pos = (pos + length + skip) % n
        skip += 1
    return pos, skip

def knot_hash(input_str):
    lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    pos = skip = 0
    
    for _ in range(64):
        pos, skip = knot_hash_round(numbers, lengths, pos, skip)
    
    dense = []
    for i in range(0, 256, 16):
        result = numbers[i]
        for j in range(1, 16):
            result ^= numbers[i + j]
        dense.append(result)
    
    return ''.join(f'{x:02x}' for x in dense)

def create_grid(key):
    grid = []
    for i in range(128):
        row_input = f"{key}-{i}"
        hash_result = knot_hash(row_input)
        binary = ''.join(bin(int(c, 16))[2:].zfill(4) for c in hash_result)
        grid.append([int(b) for b in binary])
    return grid

def find_region(grid, x, y, visited):
    if (x < 0 or x >= 128 or y < 0 or y >= 128 or 
        not grid[x][y] or (x, y) in visited):
        return
    
    visited.add((x, y))
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        find_region(grid, x + dx, y + dy, visited)

def count_regions(grid):
    visited = set()
    regions = 0
    
    for i in range(128):
        for j in range(128):
            if grid[i][j] and (i, j) not in visited:
                find_region(grid, i, j, visited)
                regions += 1
    
    return regions

def main():
    key = "hwlqcszp"
    grid = create_grid(key)
    
    used = sum(sum(row) for row in grid)
    regions = count_regions(grid)
    
    print(f"Part 1: {used}")
    print(f"Part 2: {regions}")

if __name__ == "__main__":
    main()