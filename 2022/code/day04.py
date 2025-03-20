def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def calculate_scores(lines):
    total_score = 0
    total_score_part2 = 0

    for line in lines:
        elf = line.strip().split(',')
        elf1 = list(map(int, elf[0].split('-')))
        elf2 = list(map(int, elf[1].split('-')))

        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
            total_score += 1

        if ((elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or
            (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]) or
            (elf1[0] >= elf2[0] and elf1[0] <= elf2[1]) or
            (elf1[1] >= elf2[0] and elf1[1] <= elf2[1]) or
            (elf2[0] >= elf1[0] and elf2[0] <= elf1[1]) or
            (elf2[1] >= elf1[0] and elf2[1] <= elf1[1])):
            total_score_part2 += 1

    return total_score, total_score_part2

def main():
    print("\n--- Day 4: Camp Cleanup ---")
    lines = read_input('2022/input/day04.txt')
    total_score, total_score_part2 = calculate_scores(lines)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()