from typing import List

def read_input(path: str) -> str:
    with open(path, 'r') as f:
        return f.read().strip()

def is_invalid_part1(id: int) -> bool:
    s = str(id)
    n = len(s)
    if n % 2 == 0:
        half = n // 2
        return s[:half] == s[half:]
    return False

def is_invalid_part2(id: int) -> bool:
    s = str(id)
    n = len(s)
    for k in range(2, n + 1):
        if n % k == 0:
            base_len = n // k
            base = s[:base_len]
            if s == base * k:
                return True
    return False

def part1(ranges_str: str) -> int:
    total = 0
    for r in ranges_str.split(','):
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            if is_invalid_part1(i):
                total += i
    return total

def part2(ranges_str: str) -> int:
    total = 0
    for r in ranges_str.split(','):
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            if is_invalid_part2(i):
                total += i
    return total

def main() -> None:
    ranges_str = read_input("2025/Day02/input.txt")
    print("Part 1:", part1(ranges_str))
    print("Part 2:", part2(ranges_str))

if __name__ == "__main__":
    main()