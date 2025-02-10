import re
from collections import defaultdict

def read_input(file_path):
    with open(file_path) as f:
        return f.readlines()

def parse_rules(lines):
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

def find_containers(bag, contained_by):
    seen = set()
    stack = [bag]
    
    while stack:
        current = stack.pop()
        for container in contained_by[current]:
            if container not in seen:
                seen.add(container)
                stack.append(container)
    
    return len(seen)

def count_bags(bag, contains, cache=None):
    if cache is None:
        cache = {}
    
    if bag in cache:
        return cache[bag]
    
    total = 1  # Current bag
    for inner_bag, count in contains[bag]:
        total += count * count_bags(inner_bag, contains, cache)
    
    cache[bag] = total
    return total

def part1(rules):
    _, contained_by = rules
    return find_containers('shiny gold', contained_by)

def part2(rules):
    contains, _ = rules
    return count_bags('shiny gold', contains) - 1  # Subtract 1 to exclude the shiny gold bag itself

def main():
    lines = read_input("2020/Day07/input.txt")
    rules = parse_rules(lines)
    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2(rules)}")

if __name__ == "__main__":
    main()