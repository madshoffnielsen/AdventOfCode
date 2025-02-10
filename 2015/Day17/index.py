from itertools import combinations

def read_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def find_combinations(containers, target):
    valid_combinations = []
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                valid_combinations.append(combo)
    return valid_combinations

def part1(containers, target):
    valid_combinations = find_combinations(containers, target)
    return len(valid_combinations)

def part2(containers, target):
    valid_combinations = find_combinations(containers, target)
    min_containers = min(len(combo) for combo in valid_combinations)
    return sum(1 for combo in valid_combinations if len(combo) == min_containers)

def main():
    containers = read_input("2015/Day17/input.txt")
    target = 150
    print(f"Part 1: {part1(containers, target)}")
    print(f"Part 2: {part2(containers, target)}")

if __name__ == "__main__":
    main()