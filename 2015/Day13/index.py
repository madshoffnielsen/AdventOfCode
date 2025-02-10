from itertools import permutations

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    happiness = {}
    for line in lines:
        parts = line.strip().split()
        person1 = parts[0]
        person2 = parts[-1][:-1]
        change = int(parts[3]) if parts[2] == "gain" else -int(parts[3])
        if person1 not in happiness:
            happiness[person1] = {}
        happiness[person1][person2] = change
    return happiness

def calculate_happiness(arrangement, happiness):
    total_happiness = 0
    for i in range(len(arrangement)):
        person1 = arrangement[i]
        person2 = arrangement[(i + 1) % len(arrangement)]
        total_happiness += happiness[person1].get(person2, 0)
        total_happiness += happiness[person2].get(person1, 0)
    return total_happiness

def find_optimal_happiness(happiness):
    guests = list(happiness.keys())
    max_happiness = float('-inf')
    for arrangement in permutations(guests):
        max_happiness = max(max_happiness, calculate_happiness(arrangement, happiness))
    return max_happiness

def part1(happiness):
    return find_optimal_happiness(happiness)

def part2(happiness):
    # Add yourself to the happiness dictionary
    happiness["You"] = {}
    for guest in happiness:
        happiness[guest]["You"] = 0
        happiness["You"][guest] = 0
    return find_optimal_happiness(happiness)

def main():
    happiness = read_input("2015/Day13/input.txt")
    print(f"Part 1: {part1(happiness)}")
    print(f"Part 2: {part2(happiness)}")

if __name__ == "__main__":
    main()