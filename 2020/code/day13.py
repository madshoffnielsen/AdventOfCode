from typing import List, Tuple

Schedule = List[Tuple[int, int]]

def read_input(file_path: str) -> Tuple[int, Schedule]:
    """Read bus schedule from input file."""
    with open(file_path) as f:
        lines = f.readlines()
        timestamp = int(lines[0])
        buses = [(i, int(x)) for i, x in enumerate(lines[1].strip().split(',')) 
                if x != 'x']
        return timestamp, buses

def find_earliest_bus(timestamp: int, buses: Schedule) -> int:
    """Find earliest bus multiplied by wait time."""
    earliest = float('inf')
    best_bus = None
    
    for _, bus in buses:
        wait = bus - (timestamp % bus)
        if wait < earliest:
            earliest = wait
            best_bus = bus
            
    return best_bus * earliest

def chinese_remainder(buses: Schedule) -> int:
    """Solve using Chinese Remainder Theorem."""
    N = 1
    for _, n in buses:
        N *= n
        
    total = 0
    for i, n in buses:
        a = -i  # We want bus to depart i minutes after timestamp
        y = N // n
        z = pow(y, -1, n)  # Modular multiplicative inverse
        total += a * y * z
        
    return total % N

def part1(timestamp: int, buses: Schedule) -> int:
    """Find earliest bus times minutes waited."""
    return find_earliest_bus(timestamp, buses)

def part2(buses: Schedule) -> int:
    """Find earliest timestamp satisfying schedule."""
    return chinese_remainder(buses)

def main():
    """Main program."""
    print("\n--- Day 13: Shuttle Search ---")
    
    timestamp, buses = read_input("2020/input/day13.txt")
    
    result1 = part1(timestamp, buses)
    print(f"Part 1: {result1}")
    
    result2 = part2(buses)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()