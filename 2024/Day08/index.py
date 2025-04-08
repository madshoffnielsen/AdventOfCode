from collections import defaultdict
from math import gcd
from itertools import combinations

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def parse_grid(grid):
    antennas = defaultdict(list)
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch != '.':
                antennas[ch].append((x, y))
    return antennas, len(grid[0]), len(grid)

def normalize_vector(dx, dy):
    if not dx and not dy:
        return (0, 0)
    g = abs(gcd(dx, dy))
    dx, dy = dx // g, dy // g
    return (-dx, -dy) if dx < 0 or (dx == 0 and dy < 0) else (dx, dy)

def get_line_id(x, y, dx, dy):
    return (*normalize_vector(dx, dy), y * dx - x * dy)

def generate_line_points(anchors, dx, dy, width, height):
    points = set()
    x_min, x_max = 0, width - 1
    y_min, y_max = 0, height - 1
    
    def add_points(start, step):
        x, y = start
        while x_min <= x <= x_max and y_min <= y <= y_max:
            points.add((x, y))
            x += dx * step
            y += dy * step
    
    for ax, ay in anchors:
        add_points((ax, ay), 1)
        add_points((ax - dx, ay - dy), -1)
    
    return points

def compute_antinodes(antennas, width, height, use_harmonics=False):
    if not use_harmonics:
        antinodes = set()
        for positions in antennas.values():
            for (x1, y1), (x2, y2) in combinations(positions, 2):
                for ax, ay in [(2*x1 - x2, 2*y1 - y2), (2*x2 - x1, 2*y2 - y1)]:
                    if 0 <= ax < width and 0 <= ay < height:
                        antinodes.add((ax, ay))
        return antinodes
    
    antinodes = set()
    for positions in antennas.values():
        if len(positions) < 2:
            continue
        
        lines = defaultdict(set)
        for p1, p2 in combinations(positions, 2):
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            line_id = get_line_id(p1[0], p1[1], dx, dy)
            lines[line_id].update({p1, p2})
        
        for (dx, dy, _), anchors in lines.items():
            if len(anchors) >= 2:
                antinodes.update(generate_line_points(anchors, dx, dy, width, height))
    
    return antinodes

def count_antinodes(grid, part2=False):
    antennas, width, height = parse_grid(grid)
    return len(compute_antinodes(antennas, width, height, part2))

def main():
    grid = read_input("2024/Day08/input.txt")
    print(f"Part 1: {count_antinodes(grid)}")
    print(f"Part 2: {count_antinodes(grid, True)}")

if __name__ == "__main__":
    main()