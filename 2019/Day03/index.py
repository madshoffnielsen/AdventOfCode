def parse_wire_path(wire_path):
    directions = wire_path.split(',')
    path = []
    x, y = 0, 0
    for direction in directions:
        d = direction[0]
        length = int(direction[1:])
        for _ in range(length):
            if d == 'U':
                y += 1
            elif d == 'D':
                y -= 1
            elif d == 'L':
                x -= 1
            elif d == 'R':
                x += 1
            path.append((x, y))
    return path

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

def find_intersections(path1, path2):
    return set(path1) & set(path2)

def fewest_combined_steps(path1, path2, intersections):
    steps = []
    for intersection in intersections:
        steps.append(path1.index(intersection) + path2.index(intersection) + 2)  # +2 for 1-based index
    return min(steps)

# Read input from input.txt
with open('2019/Day03/input.txt', 'r') as file:
    input_data = file.readlines()

# Parse the wire paths
wire1_path = parse_wire_path(input_data[0].strip())
wire2_path = parse_wire_path(input_data[1].strip())

# Find intersections
intersections = find_intersections(wire1_path, wire2_path)

# Part 1: Find the closest intersection by Manhattan distance
closest_intersection = min(intersections, key=manhattan_distance)
distance_part1 = manhattan_distance(closest_intersection)
print("Closest intersection distance (Part 1):", distance_part1)

# Part 2: Find the intersection with the fewest combined steps
steps_part2 = fewest_combined_steps(wire1_path, wire2_path, intersections)
print("Fewest combined steps to an intersection (Part 2):", steps_part2)