from itertools import combinations
from functools import reduce
from operator import mul

def read_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def find_optimal_grouping(packages, group_count):
    target_weight = sum(packages) // group_count
    for group_size in range(len(packages)):
        valid_groups = [group for group in combinations(packages, group_size) if sum(group) == target_weight]
        if valid_groups:
            return min(valid_groups, key=lambda x: reduce(mul, x))

def calculate_quantum_entanglement(group):
    return reduce(mul, group)

def part1(packages):
    optimal_group = find_optimal_grouping(packages, 3)
    return calculate_quantum_entanglement(optimal_group)

def part2(packages):
    optimal_group = find_optimal_grouping(packages, 4)
    return calculate_quantum_entanglement(optimal_group)

def main():
    packages = read_input("2015/Day24/input.txt")
    print(f"Part 1: {part1(packages)}")
    print(f"Part 2: {part2(packages)}")

if __name__ == "__main__":
    main()