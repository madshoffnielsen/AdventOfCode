def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def find_first_marker(line, length):
    for i in range(length, len(line)):
        unique_chars = set(line[i-length+1:i+1])
        if len(unique_chars) == length:
            return i + 1
    return -1

def calculate_scores(lines):
    total_score = 0
    total_score_part2 = 0

    for line in lines:
        line = line.strip()
        total_score = find_first_marker(line, 4)
        total_score_part2 = find_first_marker(line, 14)

    return total_score, total_score_part2

def main():
    print("\n--- Day 6: Tuning Trouble ---")
    lines = read_input('2022/input/day06.txt')
    total_score, total_score_part2 = calculate_scores(lines)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()