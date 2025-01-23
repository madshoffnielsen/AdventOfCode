import math
from collections import defaultdict

def parse_asteroid_map(data):
    asteroids = set()
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.add((x, y))
    return asteroids

def get_angle_and_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dx, -dy) % (2 * math.pi)  # Convert to clockwise from top
    distance = math.hypot(dx, dy)
    return angle, distance

def count_visible_asteroids(asteroids, station):
    angles = set()
    for asteroid in asteroids:
        if asteroid != station:
            angle, _ = get_angle_and_distance(station[0], station[1], 
                                            asteroid[0], asteroid[1])
            angles.add(angle)
    return len(angles)

def find_best_location(asteroids):
    best_count = 0
    best_location = None
    for station in asteroids:
        count = count_visible_asteroids(asteroids, station)
        if count > best_count:
            best_count = count
            best_location = station
    return best_location, best_count

def get_vaporization_order(asteroids, station):
    asteroid_angles = defaultdict(list)
    for asteroid in asteroids:
        if asteroid != station:
            angle, distance = get_angle_and_distance(station[0], station[1],
                                                   asteroid[0], asteroid[1])
            asteroid_angles[angle].append((distance, asteroid))
    
    # Sort asteroids at each angle by distance
    for angle in asteroid_angles:
        asteroid_angles[angle].sort()
    
    # Get vaporization order
    vaporized = []
    while len(vaporized) < len(asteroids) - 1:
        for angle in sorted(asteroid_angles.keys()):
            if asteroid_angles[angle]:
                _, asteroid = asteroid_angles[angle].pop(0)
                vaporized.append(asteroid)
    
    return vaporized

# Read input
with open('2019/Day10/input.txt', 'r') as file:
    asteroid_map = file.read().strip()

# Parse asteroid map
asteroids = parse_asteroid_map(asteroid_map)

# Part 1: Find best monitoring station
station, visible_count = find_best_location(asteroids)
print(f"Part 1: Best location {station} can detect {visible_count} asteroids")

# Part 2: Find 200th asteroid to be vaporized
vaporized = get_vaporization_order(asteroids, station)
if len(vaporized) >= 200:
    x, y = vaporized[199]
    answer = x * 100 + y
    print(f"Part 2: 200th asteroid at {(x, y)}, answer is {answer}")