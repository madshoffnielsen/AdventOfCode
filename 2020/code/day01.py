def read_input(file_path):
    """Read and parse input file to list of integers."""
    with open(file_path, 'r') as f:
        return [int(line.strip()) for line in f]

def part1(numbers):
    """Find two numbers that sum to 2020 and return their product."""
    seen = set()
    for num in numbers:
        complement = 2020 - num
        if complement in seen:
            return num * complement
        seen.add(num)
    return None

def part2(numbers):
    """Find three numbers that sum to 2020 and return their product."""
    numbers.sort()
    for i, num in enumerate(numbers):
        target = 2020 - num
        left = i + 1
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return num * numbers[left] * numbers[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

def main():
    """Main program."""
    # Print header
    print("\n--- Day 1: Report Repair ---")
    
    # Read input
    numbers = read_input("2020/input/day01.txt")
    
    # Part 1
    result1 = part1(numbers)
    print(f"Part 1: {result1}")
    
    # Part 2
    result2 = part2(numbers)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()