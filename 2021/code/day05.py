import re
from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    vents = []
    for line in lines:
        match = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line.strip())
        if match:
            x1, y1, x2, y2 = map(int, match.groups())
            vents.append((x1, y1, x2, y2))
    
    return vents

def count_overlaps(vents, include_diagonals=False):
    grid = defaultdict(int)
    
    for x1, y1, x2, y2 in vents:
        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] += 1
        elif y1 == y2:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] += 1
        elif include_diagonals:  # Diagonal line
            x_step = 1 if x2 > x1 else -1
            y_step = 1 if y2 > y1 else -1
            x, y = x1, y1
            while x != x2 + x_step and y != y2 + y_step:
                grid[(x, y)] += 1
                x += x_step
                y += y_step
    
    overlap_count = sum(1 for count in grid.values() if count >= 2)
    return overlap_count

def main():
    print("\n--- Day 5: Hydrothermal Venture ---")
    vents = parse_input('2021/input/day05.txt')

    # Part 1
    result = count_overlaps(vents)
    print(f"Part 1: {result}")

    # Part 2
    result_with_diagonals = count_overlaps(vents, include_diagonals=True)
    print(f"Part 2: {result_with_diagonals}")

if __name__ == "__main__":
    main()