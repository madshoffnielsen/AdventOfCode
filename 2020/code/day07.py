import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

BagRules = Tuple[Dict[str, List[Tuple[str, int]]], Dict[str, List[str]]]

def read_input(file_path: str) -> List[str]:
    """Read and parse input file into list of rules."""
    with open(file_path) as f:
        return f.readlines()

def parse_rules(lines: List[str]) -> BagRules:
    """Parse rules into contains and contained_by relationships."""
    contains = defaultdict(list)
    contained_by = defaultdict(list)
    
    for line in lines:
        outer = re.match(r'(.*?) bags contain', line).group(1)
        inner_bags = re.findall(r'(\d+) (.*?) bag', line)
        
        for count, color in inner_bags:
            count = int(count)
            contains[outer].append((color, count))
            contained_by[color].append(outer)
    
    return contains, contained_by

def find_containers(bag: str, contained_by: Dict[str, List[str]]) -> int:
    """Find number of bags that can contain the target bag."""
    seen = set()
    stack = [bag]
    
    while stack:
        current = stack.pop()
        for container in contained_by[current]:
            if container not in seen:
                seen.add(container)
                stack.append(container)
    
    return len(seen)

def count_bags(bag: str, contains: Dict[str, List[Tuple[str, int]]], 
               cache: Dict[str, int] = None) -> int:
    """Count total number of bags inside the target bag."""
    if cache is None:
        cache = {}
    
    if bag in cache:
        return cache[bag]
    
    total = 1  # Current bag
    for inner_bag, count in contains[bag]:
        total += count * count_bags(inner_bag, contains, cache)
    
    cache[bag] = total
    return total

def part1(rules: BagRules) -> int:
    """Calculate number of bag colors that can contain a shiny gold bag."""
    _, contained_by = rules
    return find_containers('shiny gold', contained_by)

def part2(rules: BagRules) -> int:
    """Calculate total number of bags required inside a shiny gold bag."""
    contains, _ = rules
    return count_bags('shiny gold', contains) - 1  # Subtract 1 to exclude the shiny gold bag itself

def main():
    """Main program."""
    # Print header
    print("\n--- Day 7: Handy Haversacks ---")
    
    # Read and parse input
    lines = read_input("2020/input/day07.txt")
    rules = parse_rules(lines)
    
    # Part 1
    result1 = part1(rules)
    print(f"Part 1: {result1}")
    
    # Part 2
    result2 = part2(rules)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()