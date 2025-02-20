import re
from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    template = lines[0]
    rules = {}
    
    for line in lines[1:]:
        pair, insert = line.split(" -> ")
        rules[pair] = insert
    
    return template, rules

def simulate_polymerization(template, rules, steps):
    pair_counts = defaultdict(int)
    element_counts = defaultdict(int)
    
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        pair_counts[pair] += 1
    
    for char in template:
        element_counts[char] += 1
    
    for _ in range(steps):
        new_pair_counts = defaultdict(int)
        
        for pair, count in pair_counts.items():
            if pair in rules:
                insert = rules[pair]
                new_pair_counts[pair[0] + insert] += count
                new_pair_counts[insert + pair[1]] += count
                element_counts[insert] += count
        
        pair_counts = new_pair_counts
    
    return max(element_counts.values()) - min(element_counts.values())

def main():
    input_file = '2021/input/day14.txt'
    template, rules = parse_input(input_file)
    result = simulate_polymerization(template, rules, 10)
    print(f"Part 1: {result}")

    result = simulate_polymerization(template, rules, 40)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
