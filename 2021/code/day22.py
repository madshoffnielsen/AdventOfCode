import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return input_data

def parse_input(input_data):
    lines = input_data.split('\n')
    instructions = []
    for line in lines:
        match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
        if match:
            state = 1 if match.group(1) == "on" else -1
            x1, x2 = int(match.group(2)), int(match.group(3))
            y1, y2 = int(match.group(4)), int(match.group(5))
            z1, z2 = int(match.group(6)), int(match.group(7))
            instructions.append((state, x1, x2, y1, y2, z1, z2))
    return instructions

def part_one(instructions):
    reactor = {}
    count = 0
    for state, x1, x2, y1, y2, z1, z2 in instructions:
        for x in range(max(-50, x1), min(50, x2) + 1):
            for y in range(max(-50, y1), min(50, y2) + 1):
                for z in range(max(-50, z1), min(50, z2) + 1):
                    if state == 1:
                        if (x, y, z) not in reactor:
                            reactor[(x, y, z)] = 1
                            count += 1
                    else:
                        if (x, y, z) in reactor:
                            del reactor[(x, y, z)]
                            count -= 1
    return count

def part_two(instructions):
    cubes = []
    for state, x1, x2, y1, y2, z1, z2 in instructions:
        new_cubes = []
        for cube in cubes:
            ax, bx = max(x1, cube[1]), min(x2, cube[2])
            ay, by = max(y1, cube[3]), min(y2, cube[4])
            az, bz = max(z1, cube[5]), min(z2, cube[6])
            if ax <= bx and ay <= by and az <= bz:
                overlap = (-cube[0], ax, bx, ay, by, az, bz)
                new_cubes.append(overlap)
        if state == 1:
            new_cubes.append((state, x1, x2, y1, y2, z1, z2))
        cubes.extend(new_cubes)
    
    volume = 0
    for state, x1, x2, y1, y2, z1, z2 in cubes:
        volume += state * (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    return volume

def main():
    print("\n--- Day 22: Reactor Reboot ---")
    input_file = '2021/input/day22.txt'
    input_data = read_input(input_file)
    instructions = parse_input(input_data)

    # Part 1
    result = part_one(instructions)
    print(f"Part 1: {result}")

    # Part 2
    result = part_two(instructions)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()