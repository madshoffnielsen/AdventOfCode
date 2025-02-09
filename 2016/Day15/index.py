import re

def parse_input(file_path):
    discs = []
    with open(file_path) as f:
        for line in f:
            match = re.match(r'Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).', line)
            if match:
                positions, start = map(int, match.groups())
                discs.append((positions, start))
    return discs

def find_time(discs):
    time = 0
    while True:
        if all((start + time + i + 1) % positions == 0 for i, (positions, start) in enumerate(discs)):
            return time
        time += 1

def part1(discs):
    return find_time(discs)

def part2(discs):
    discs.append((11, 0))  # Add the new disc with 11 positions and starting at position 0
    return find_time(discs)

if __name__ == "__main__":
    discs = parse_input("2016/Day15/input.txt")
    print("Part 1:", part1(discs))
    print("Part 2:", part2(discs))