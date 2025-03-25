from typing import Dict, List

def read_input(file_path: str) -> List[int]:
    """Read adapter joltages from input file."""
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def count_differences(adapters: List[int]) -> int:
    """Count joltage differences and multiply 1-jolt by 3-jolt counts."""
    # Add charging outlet (0) and device adapter (max + 3)
    adapters = [0] + sorted(adapters) + [max(adapters) + 3]
    differences = {1: 0, 2: 0, 3: 0}
    
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        differences[diff] += 1
    
    return differences[1] * differences[3]

def count_arrangements(adapters: List[int]) -> int:
    """Count possible adapter arrangements using dynamic programming."""
    # Add charging outlet and device adapter
    adapters = [0] + sorted(adapters) + [max(adapters) + 3]
    dp: Dict[int, int] = {adapters[-1]: 1}
    
    for i in range(len(adapters)-2, -1, -1):
        current = adapters[i]
        dp[current] = 0
        
        for j in range(i+1, len(adapters)):
            if adapters[j] - current <= 3:
                dp[current] += dp[adapters[j]]
            else:
                break
    
    return dp[0]

def part1(adapters: List[int]) -> int:
    """Calculate product of 1-jolt and 3-jolt differences."""
    return count_differences(adapters)

def part2(adapters: List[int]) -> int:
    """Calculate total number of possible adapter arrangements."""
    return count_arrangements(adapters)

def main():
    """Main program."""
    print("\n--- Day 10: Adapter Array ---")
    
    adapters = read_input("2020/input/day10.txt")
    
    result1 = part1(adapters)
    print(f"Part 1: {result1}")
    
    result2 = part2(adapters)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()