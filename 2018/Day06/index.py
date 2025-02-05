import re
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [tuple(map(int, re.findall(r'\d+', line))) for line in file]

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def part1(coordinates):
    min_x = min(x for x, y in coordinates)
    max_x = max(x for x, y in coordinates)
    min_y = min(y for x, y in coordinates)
    max_y = max(y for x, y in coordinates)

    area = defaultdict(int)
    infinite = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = sorted((manhattan_distance(x, y, cx, cy), (cx, cy)) for cx, cy in coordinates)
            if distances[0][0] != distances[1][0]:
                closest = distances[0][1]
                area[closest] += 1
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    infinite.add(closest)

    return max(area[coord] for coord in area if coord not in infinite)

def part2(coordinates, max_distance=10000):
    min_x = min(x for x, y in coordinates)
    max_x = max(x for x, y in coordinates)
    min_y = min(y for x, y in coordinates)
    max_y = max(y for x, y in coordinates)

    region_size = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if sum(manhattan_distance(x, y, cx, cy) for cx, cy in coordinates) < max_distance:
                region_size += 1

    return region_size

if __name__ == "__main__":
    input_file = "2018/Day06/input.txt"
    coordinates = read_input(input_file)
    
    result_part1 = part1(coordinates)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(coordinates)
    print(f"Part 2: {result_part2}")