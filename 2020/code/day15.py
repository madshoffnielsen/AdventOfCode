from typing import List, Dict

def read_input(file_path: str) -> List[int]:
    """Read starting numbers from file."""
    with open(file_path) as f:
        return [int(x) for x in f.read().strip().split(',')]

def play_memory_game(numbers: List[int], target: int) -> int:
    """Play memory game until target turn."""
    last_seen: Dict[int, int] = {}
    
    # Initialize the game state
    for turn, num in enumerate(numbers[:-1], 1):
        last_seen[num] = turn
    current = numbers[-1]
    
    # Play until target turn
    for turn in range(len(numbers), target):
        next_num = 0 if current not in last_seen else turn - last_seen[current]
        last_seen[current] = turn
        current = next_num
        
    return current

def part1(numbers: List[int]) -> int:
    """Solve puzzle part 1: Play until turn 2020."""
    return play_memory_game(numbers, 2020)

def part2(numbers: List[int]) -> int:
    """Solve puzzle part 2: Play until turn 30000000."""
    return play_memory_game(numbers, 30000000)

def main():
    """Main program."""
    print("\n--- Day 15: Rambunctious Recitation ---")
    
    numbers = [13, 0, 10, 12, 1, 5, 8]
    
    result1 = part1(numbers)
    print(f"Part 1: {result1}")
    
    result2 = part2(numbers)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()