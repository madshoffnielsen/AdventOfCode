def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def calculate_max_calories(elves):
    return max(elves)

def calculate_top_three_calories(elves):
    top3 = sorted(elves, reverse=True)[:3]
    return sum(top3)

def main():
    print("\n--- Day 1: Calorie Counting ---")
    elves = []
    id = 0

    file = read_input('2022/input/day01.txt')
    if file:
        for line in file:
            line = line.strip()
            if line == "":
                id += 1
            else:
                if len(elves) <= id:
                    elves.append(0)
                elves[id] += int(line)

    max_calories = calculate_max_calories(elves)
    print(f"Part 1: {max_calories}")

    top_three_calories = calculate_top_three_calories(elves)
    print(f"Part 2: {top_three_calories}")

if __name__ == "__main__":
    main()