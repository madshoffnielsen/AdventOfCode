from typing import List

def read_input(file_path: str) -> List[str]:
    """Read and parse input file into list of boarding passes."""
    with open(file_path) as f:
        return [line.strip() for line in f]

def get_seat_id(boarding_pass: str) -> int:
    """Calculate seat ID from boarding pass string."""
    # Convert F/B to binary for row
    row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
    # Convert L/R to binary for column
    col = int(boarding_pass[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

def part1(boarding_passes: List[str]) -> int:
    """Find highest seat ID."""
    return max(get_seat_id(bp) for bp in boarding_passes)

def part2(boarding_passes: List[str]) -> int:
    """Find missing seat ID between occupied seats."""
    seat_ids = sorted(get_seat_id(bp) for bp in boarding_passes)
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] - seat_ids[i] == 2:
            return seat_ids[i] + 1
    return None

def main():
    """Main program."""
    # Print header
    print("\n--- Day 5: Binary Boarding ---")
    
    # Read input
    boarding_passes = read_input("2020/input/day05.txt")
    
    # Part 1
    result1 = part1(boarding_passes)
    print(f"Part 1: {result1}")
    
    # Part 2
    result2 = part2(boarding_passes)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()