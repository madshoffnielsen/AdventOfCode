def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def calculate_scores(lines):
    total_score = 0
    total_score_part2 = 0

    score = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    for line in lines:
        line = line.strip()
        play = line.split(' ')

        total_score += score[play[1]]

        # Win
        if line in ['C X', 'A Y', 'B Z']:
            total_score += 6

        # Draw
        if line in ['A X', 'B Y', 'C Z']:
            total_score += 3

        # Draw part 2
        if play[1] == 'Y':
            total_score_part2 += 3
            total_score_part2 += score[play[0]]

        # Lose part 2
        if line == 'A X':
            total_score_part2 += score['Z']
        if line == 'B X':
            total_score_part2 += score['X']
        if line == 'C X':
            total_score_part2 += score['Y']

        # Win part 2
        if play[1] == 'Z':
            total_score_part2 += 6
            if line == 'A Z':
                total_score_part2 += score['Y']
            if line == 'B Z':
                total_score_part2 += score['Z']
            if line == 'C Z':
                total_score_part2 += score['X']

    return total_score, total_score_part2

def main():
    print("\n--- Day 2: Rock Paper Scissors ---")
    lines = read_input('2022/input/day02.txt')
    total_score, total_score_part2 = calculate_scores(lines)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()