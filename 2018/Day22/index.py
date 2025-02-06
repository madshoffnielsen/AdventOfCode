import heapq

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    depth = int(lines[0].strip().split()[1])
    target = tuple(map(int, lines[1].strip().split()[1].split(',')))
    return depth, target

def geologic_index(x, y, depth, target, erosion_levels):
    if (x, y) in erosion_levels:
        return erosion_levels[(x, y)]
    if (x, y) == (0, 0) or (x, y) == target:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return erosion_level(x-1, y, depth, target, erosion_levels) * erosion_level(x, y-1, depth, target, erosion_levels)

def erosion_level(x, y, depth, target, erosion_levels):
    if (x, y) not in erosion_levels:
        geo_index = geologic_index(x, y, depth, target, erosion_levels)
        erosion = (geo_index + depth) % 20183
        erosion_levels[(x, y)] = erosion
    return erosion_levels[(x, y)]

def region_type(x, y, depth, target, erosion_levels):
    erosion = erosion_level(x, y, depth, target, erosion_levels)
    return erosion % 3

def part1(depth, target):
    erosion_levels = {}
    risk_level = 0
    for y in range(target[1] + 1):
        for x in range(target[0] + 1):
            risk_level += region_type(x, y, depth, target, erosion_levels)
    return risk_level

def neighbors(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0:
            yield nx, ny

def part2(depth, target):
    erosion_levels = {}
    target_x, target_y = target
    pq = [(0, 0, 0, 1)]  # (time, x, y, tool)
    visited = set()
    while pq:
        time, x, y, tool = heapq.heappop(pq)
        if (x, y, tool) in visited:
            continue
        visited.add((x, y, tool))
        if (x, y) == target and tool == 1:
            return time
        current_region = region_type(x, y, depth, target, erosion_levels)
        for nx, ny in neighbors(x, y):
            next_region = region_type(nx, ny, depth, target, erosion_levels)
            for next_tool in range(3):
                if next_tool != current_region and next_tool != next_region:
                    heapq.heappush(pq, (time + 1 + (next_tool != tool) * 7, nx, ny, next_tool))

if __name__ == "__main__":
    input_file = "2018/Day22/input.txt"
    depth, target = read_input(input_file)
    
    result_part1 = part1(depth, target)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(depth, target)
    print(f"Part 2: {result_part2}")