def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        return (int(lines[0].split()[-1]), 
                int(lines[1].split()[-1]))

def generator(start, factor, multiple=1):
    value = start
    while True:
        value = (value * factor) % 2147483647
        if value % multiple == 0:
            yield value & 0xFFFF

def count_matches(gen_a, gen_b, pairs):
    return sum(1 for _ in range(pairs) 
              if next(gen_a) == next(gen_b))

def part1(start_a, start_b):
    gen_a = generator(start_a, 16807)
    gen_b = generator(start_b, 48271)
    return count_matches(gen_a, gen_b, 40_000_000)

def part2(start_a, start_b):
    gen_a = generator(start_a, 16807, 4)
    gen_b = generator(start_b, 48271, 8)
    return count_matches(gen_a, gen_b, 5_000_000)

def main():
    start_a, start_b = read_input("2017/Day15/input.txt")
    print(f"Part 1: {part1(start_a, start_b)}")
    print(f"Part 2: {part2(start_a, start_b)}")

if __name__ == "__main__":
    main()