def read_input(file_path):
    with open(file_path) as f:
        return [int(line) for line in f]

def part1(jumps):
    jumps = jumps.copy()
    pos = 0
    steps = 0
    while 0 <= pos < len(jumps):
        jump = jumps[pos]
        jumps[pos] += 1
        pos += jump
        steps += 1
    return steps

def part2(jumps):
    jumps = jumps.copy()
    pos = 0
    steps = 0
    while 0 <= pos < len(jumps):
        jump = jumps[pos]
        jumps[pos] += 1 if jump < 3 else -1
        pos += jump
        steps += 1
    return steps

def main():
    jumps = read_input("2017/Day05/input.txt")
    print(f"Part 1: {part1(jumps)}")
    print(f"Part 2: {part2(jumps)}")

if __name__ == "__main__":
    main()