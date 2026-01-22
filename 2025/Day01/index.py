from typing import List

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def part1(rotations: List[str], start: int = 50) -> int:
    pos = start
    zeros = 0
    for r in rotations:
        d = r[0].upper()
        n = int(r[1:])
        if d == 'L':
            pos = (pos - n) % 100
        else:
            pos = (pos + n) % 100
        if pos == 0:
            zeros += 1
    return zeros

def part2(rotations: List[str], start: int = 50) -> int:
    pos = start
    zeros = 0
    for r in rotations:
        d = r[0].upper()
        n = int(r[1:])
        step = -1 if d == 'L' else 1
        for _ in range(n):
            pos = (pos + step) % 100
            if pos == 0:
                zeros += 1
    return zeros

def main() -> None:
    rotations = read_input("2025/Day01/input.txt")
    print("Part 1:", part1(rotations))
    print("Part 2:", part2(rotations))

if __name__ == "__main__":
    main()