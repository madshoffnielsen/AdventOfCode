from typing import List, Optional

def read_input(file_path: str) -> List[int]:
    """Read numbers from input file."""
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def is_valid(number: int, preamble: List[int]) -> bool:
    """Check if number is sum of any two different numbers in preamble."""
    for i in range(len(preamble)):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False

def find_invalid_number(numbers: List[int], preamble_size: int = 25) -> Optional[int]:
    """Find first number that is not sum of two numbers in preamble."""
    for i in range(preamble_size, len(numbers)):
        preamble = numbers[i - preamble_size:i]
        if not is_valid(numbers[i], preamble):
            return numbers[i]
    return None

def find_contiguous_set(numbers: List[int], target: int) -> Optional[int]:
    """Find contiguous set that sums to target and return sum of min and max."""
    for i in range(len(numbers)):
        sum_so_far = 0
        for j in range(i, len(numbers)):
            sum_so_far += numbers[j]
            if sum_so_far == target:
                contiguous_set = numbers[i:j + 1]
                return min(contiguous_set) + max(contiguous_set)
            if sum_so_far > target:
                break
    return None

def part1(numbers: List[int]) -> Optional[int]:
    """Find first invalid number in sequence."""
    return find_invalid_number(numbers)

def part2(numbers: List[int]) -> Optional[int]:
    """Find encryption weakness in XMAS data."""
    invalid_number = find_invalid_number(numbers)
    if invalid_number:
        return find_contiguous_set(numbers, invalid_number)
    return None

def main():
    """Main program."""
    print("\n--- Day 9: Encoding Error ---")
    
    numbers = read_input("2020/input/day09.txt")
    
    result1 = part1(numbers)
    print(f"Part 1: {result1}")
    
    result2 = part2(numbers)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()