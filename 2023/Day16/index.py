def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def move_beam(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def get_new_directions(tile, direction):
    if tile == '/':
        return [(-direction[1], -direction[0])]
    elif tile == '\\':
        return [(direction[1], direction[0])]
    elif tile == '|' and direction[1] != 0:
        return [(1, 0), (-1, 0)]
    elif tile == '-' and direction[0] != 0:
        return [(0, 1), (0, -1)]
    return [direction]

def trace_beam(grid, start_pos=(0,0), start_dir=(0,1)):
    height, width = len(grid), len(grid[0])
    beams = [(start_pos, start_dir)]
    energized = set()
    seen = set()
    
    while beams:
        pos, direction = beams.pop()
        
        if not (0 <= pos[0] < height and 0 <= pos[1] < width):
            continue
        
        if (pos, direction) in seen:
            continue
            
        seen.add((pos, direction))
        energized.add(pos)
        
        tile = grid[pos[0]][pos[1]]
        for new_dir in get_new_directions(tile, direction):
            new_pos = move_beam(pos, new_dir)
            beams.append((new_pos, new_dir))
            
    return len(energized)

def part1(grid):
    return trace_beam(grid)

def part2(grid):
    height, width = len(grid), len(grid[0])
    max_energy = 0
    
    # Try all possible starting positions
    for row in range(height):
        max_energy = max(max_energy, trace_beam(grid, (row, 0), (0, 1)))
        max_energy = max(max_energy, trace_beam(grid, (row, width-1), (0, -1)))
    
    for col in range(width):
        max_energy = max(max_energy, trace_beam(grid, (0, col), (1, 0)))
        max_energy = max(max_energy, trace_beam(grid, (height-1, col), (-1, 0)))
    
    return max_energy

def main():
    grid = read_input("2023/Day16/input.txt")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

if __name__ == "__main__":
    main()