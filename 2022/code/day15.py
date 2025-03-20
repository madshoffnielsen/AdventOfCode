import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def parse_input(lines):
    sensors = []
    beacons = []
    for line in lines:
        matches = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        if matches:
            sensors.append({'x': int(matches[1]), 'y': int(matches[2]), 'dist': float('inf')})
            beacons.append({'x': int(matches[3]), 'y': int(matches[4])})
    return sensors, beacons

def calculate_distances(sensors, beacons):
    for sensor in sensors:
        xs, ys = sensor['x'], sensor['y']
        for beacon in beacons:
            xb, yb = beacon['x'], beacon['y']
            dist = abs(xb - xs) + abs(yb - ys)
            sensor['dist'] = min(sensor['dist'], dist)

def part1(sensors, beacons, y_searched):
    row = set()
    beacons_in_row = {beacon['x'] for beacon in beacons if beacon['y'] == y_searched}

    for sensor in sensors:
        xs, ys, dist = sensor['x'], sensor['y'], sensor['dist']
        if abs(ys - y_searched) <= dist:
            d = dist - abs(ys - y_searched)
            row.update(range(xs - d, xs + d + 1))

    # Exclude positions where beacons are already present
    return len(row - beacons_in_row)

def part2(sensors, max_length):
    for y_searched in range(max_length + 1):
        intervals = []

        for sensor in sensors:
            xs, ys, dist = sensor['x'], sensor['y'], sensor['dist']
            if abs(ys - y_searched) <= dist:
                d = dist - abs(ys - y_searched)
                intervals.append((max(0, xs - d), min(max_length, xs + d)))

        # Merge intervals and find gaps
        intervals.sort()
        cursor = 0
        for start, end in intervals:
            if start > cursor:
                return cursor * 4000000 + y_searched
            cursor = max(cursor, end + 1)

    return None

def main():
    print("\n--- Day 15: Beacon Exclusion Zone ---")
    lines = read_input('2022/input/day15.txt')
    sensors, beacons = parse_input(lines)

    # Precompute distances for sensors
    calculate_distances(sensors, beacons)

    # Part 1
    y_searched = 2000000
    part1_result = part1(sensors, beacons, y_searched)
    print(f"Part 1: {part1_result}")

    # Part 2
    max_length = 4000000
    part2_result = part2(sensors, max_length)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()