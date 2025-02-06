import re
import heapq

def read_input(file_path):
    nanobots = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z, r = map(int, re.findall(r'-?\d+', line))
            nanobots.append((x, y, z, r))
    return nanobots

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def in_range(nanobot, point):
    x, y, z, r = nanobot
    return manhattan_distance((x, y, z), point) <= r

def part1(nanobots):
    strongest = max(nanobots, key=lambda bot: bot[3])
    count = sum(1 for bot in nanobots if in_range(strongest, bot[:3]))
    return count

def part2(nanobots):
    queue = []
    for x, y, z, r in nanobots:
        d = abs(x) + abs(y) + abs(z)
        heapq.heappush(queue, (max(0, d - r), 1))
        heapq.heappush(queue, (d + r + 1, -1))
    
    count = 0
    max_count = 0
    result = 0
    while queue:
        dist, e = heapq.heappop(queue)
        count += e
        if count > max_count:
            max_count = count
            result = dist
    return result

if __name__ == "__main__":
    input_file = "2018/Day23/input.txt"
    nanobots = read_input(input_file)
    
    result_part1 = part1(nanobots)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(nanobots)
    print(f"Part 2: {result_part2}")