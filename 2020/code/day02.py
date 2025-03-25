from typing import List, Tuple

def read_input(file_path: str) -> List[Tuple[int, int, str, str]]:
    """Read and parse input file into list of password entries.
    
    Each entry contains: (min_count, max_count, letter, password)
    """
    passwords = []
    with open(file_path) as f:
        for line in f:
            policy, letter, password = line.strip().split()
            min_count, max_count = map(int, policy.split('-'))
            letter = letter[0]  # Remove colon
            passwords.append((min_count, max_count, letter, password))
    return passwords

def is_valid_part1(min_count: int, max_count: int, letter: str, password: str) -> bool:
    """Check if password is valid according to part 1 rules."""
    count = password.count(letter)
    return min_count <= count <= max_count

def is_valid_part2(pos1: int, pos2: int, letter: str, password: str) -> bool:
    """Check if password is valid according to part 2 rules."""
    return (password[pos1-1] == letter) != (password[pos2-1] == letter)

def part1(passwords: List[Tuple[int, int, str, str]]) -> int:
    """Solve part 1: Count passwords valid under first policy."""
    return sum(1 for p in passwords if is_valid_part1(*p))

def part2(passwords: List[Tuple[int, int, str, str]]) -> int:
    """Solve part 2: Count passwords valid under second policy."""
    return sum(1 for p in passwords if is_valid_part2(*p))

def main():
    """Main program."""
    # Print header
    print("\n--- Day 2: Password Philosophy ---")
    
    # Read input
    passwords = read_input("2020/input/day02.txt")
    
    # Part 1
    result1 = part1(passwords)
    print(f"Part 1: {result1}")
    
    # Part 2
    result2 = part2(passwords)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()