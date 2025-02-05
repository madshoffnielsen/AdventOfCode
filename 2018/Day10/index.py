import re
import numpy as np

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, re.findall(r'-?\d+', line))) for line in file]

def update_positions(points, seconds=1):
    for point in points:
        point[0] += point[2] * seconds
        point[1] += point[3] * seconds

def get_bounds(points):
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    return min_x, max_x, min_y, max_y

def display_message(points):
    min_x, max_x, min_y, max_y = get_bounds(points)
    grid = np.full((max_y - min_y + 1, max_x - min_x + 1), ' ')
    for x, y, _, _ in points:
        grid[y - min_y, x - min_x] = '#'
    for row in grid:
        print(''.join(row))

def part1_and_part2(points):
    seconds = 0
    while True:
        update_positions(points)
        seconds += 1
        min_x, max_x, min_y, max_y = get_bounds(points)
        if max_y - min_y < 10:  # Arbitrary threshold to detect message
            display_message(points)
            return seconds

if __name__ == "__main__":
    input_file = "2018/Day10/input.txt"
    points = read_input(input_file)
    
    seconds = part1_and_part2(points)
    print(f"Seconds: {seconds}")