from typing import List, Set

def read_input(file_path: str) -> List[List[Set[str]]]:
    """Read and parse input file into groups of answers."""
    with open(file_path) as f:
        groups = []
        current_group = []
        
        for line in f:
            line = line.strip()
            if not line:
                if current_group:
                    groups.append(current_group)
                    current_group = []
            else:
                current_group.append(set(line))
                
        if current_group:
            groups.append(current_group)
            
        return groups

def part1(groups: List[List[Set[str]]]) -> int:
    """Calculate sum of unique answers in each group."""
    return sum(len(set.union(*group)) for group in groups)

def part2(groups: List[List[Set[str]]]) -> int:
    """Calculate sum of common answers in each group."""
    return sum(len(set.intersection(*group)) for group in groups)

def main():
    """Main program."""
    # Print header
    print("\n--- Day 6: Custom Customs ---")
    
    # Read input
    groups = read_input("2020/input/day06.txt")
    
    # Part 1
    result1 = part1(groups)
    print(f"Part 1: {result1}")
    
    # Part 2
    result2 = part2(groups)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()