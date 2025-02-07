def read_input(file_path):
    with open(file_path) as f:
        return [int(d) for d in f.read().strip()]

def part1(digits):
    total = 0
    for i in range(len(digits)):
        if digits[i] == digits[(i + 1) % len(digits)]:
            total += digits[i]
    return total

def part2(digits):
    total = 0
    half = len(digits) // 2
    for i in range(len(digits)):
        if digits[i] == digits[(i + half) % len(digits)]:
            total += digits[i]
    return total

def main():
    digits = read_input("2017/Day01/input.txt")
    print(f"Part 1: {part1(digits)}")
    print(f"Part 2: {part2(digits)}")

if __name__ == "__main__":
    main()