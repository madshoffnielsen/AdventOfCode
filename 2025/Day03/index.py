from typing import List

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def max_joltage(bank: str) -> int:
    max_val = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            val = 10 * int(bank[i]) + int(bank[j])
            if val > max_val:
                max_val = val
    return max_val

def largest_k_digits(s: str, k: int) -> str:
    if len(s) <= k:
        return s
    result = []
    start = 0
    for i in range(k):
        remaining_needed = k - i - 1
        end = len(s) - remaining_needed
        max_digit = '0'
        max_idx = start
        for j in range(start, end):
            if s[j] > max_digit:
                max_digit = s[j]
                max_idx = j
        result.append(max_digit)
        start = max_idx + 1
    return ''.join(result)

def part1(banks: List[str]) -> int:
    return sum(max_joltage(bank) for bank in banks)

def part2(banks: List[str]) -> int:
    return sum(int(largest_k_digits(bank, 12)) for bank in banks)

def main() -> None:
    banks = read_input("2025/Day03/input.txt")
    print("Part 1:", part1(banks))
    print("Part 2:", part2(banks))

if __name__ == "__main__":
    main()