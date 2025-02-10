def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    reindeer = []
    for line in lines:
        parts = line.strip().split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer.append((name, speed, fly_time, rest_time))
    return reindeer

def calculate_distance(speed, fly_time, rest_time, total_time):
    cycle_time = fly_time + rest_time
    full_cycles = total_time // cycle_time
    remaining_time = total_time % cycle_time
    distance = full_cycles * speed * fly_time
    distance += min(remaining_time, fly_time) * speed
    return distance

def part1(reindeer, total_time):
    max_distance = 0
    for name, speed, fly_time, rest_time in reindeer:
        distance = calculate_distance(speed, fly_time, rest_time, total_time)
        max_distance = max(max_distance, distance)
    return max_distance

def part2(reindeer, total_time):
    points = {name: 0 for name, _, _, _ in reindeer}
    distances = {name: 0 for name, _, _, _ in reindeer}
    
    for t in range(1, total_time + 1):
        for name, speed, fly_time, rest_time in reindeer:
            distances[name] = calculate_distance(speed, fly_time, rest_time, t)
        max_distance = max(distances.values())
        for name in distances:
            if distances[name] == max_distance:
                points[name] += 1
    
    return max(points.values())

def main():
    reindeer = read_input("2015/Day14/input.txt")
    total_time = 2503
    print(f"Part 1: {part1(reindeer, total_time)}")
    print(f"Part 2: {part2(reindeer, total_time)}")

if __name__ == "__main__":
    main()