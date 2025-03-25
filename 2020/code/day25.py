from typing import List, Tuple

def read_input(file_path: str) -> Tuple[int, int]:
    """Read card and door public keys from file."""
    with open(file_path) as f:
        keys = [int(line.strip()) for line in f]
        return keys[0], keys[1]

def transform(subject_number: int, loop_size: int) -> int:
    """Transform subject number using loop size."""
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value

def find_loop_size(public_key: int) -> int:
    """Find loop size by brute force."""
    value = 1
    loop_size = 0
    while value != public_key:
        value = (value * 7) % 20201227
        loop_size += 1
    return loop_size

def part1(card_public_key: int, door_public_key: int) -> int:
    """Find encryption key using card and door public keys."""
    card_loop_size = find_loop_size(card_public_key)
    encryption_key = transform(door_public_key, card_loop_size)
    return encryption_key

def main():
    """Main program."""
    print("\n--- Day 25: Combo Breaker ---")
    
    card_public_key, door_public_key = read_input("2020/input/day25.txt")
    
    result1 = part1(card_public_key, door_public_key)
    print(f"Part 1: {result1}")
    
if __name__ == "__main__":
    main()