def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def calculate_scores(lines):
    total_score = 0
    total_score_part2 = 0

    score = [0] + list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    group = []
    group_index = 0

    for line in lines:
        line = line.strip()
        length = len(line) // 2
        string1 = set(line[:length])
        string2 = set(line[length:])

        for char1 in string1:
            if char1 in string2:
                total_score += score.index(char1)

        # Part 2
        group.append(set(line))
        group_index += 1

        if group_index == 3:
            group_index = 0
            for char1 in group[0]:
                if char1 in group[1] and char1 in group[2]:
                    total_score_part2 += score.index(char1)
            group = []

    return total_score, total_score_part2

def main():
    print("\n--- Day 3: Rucksack Reorganization ---")
    lines = read_input('2022/input/day03.txt')
    total_score, total_score_part2 = calculate_scores(lines)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()