from collections import defaultdict

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def parse_card(line):
    card_part, numbers = line.split(': ')
    card_id = int(card_part.split()[1])
    winning, mine = numbers.split(' | ')
    winning_nums = set(int(x) for x in winning.split())
    my_nums = set(int(x) for x in mine.split())
    return card_id, winning_nums, my_nums

def count_matches(winning, mine):
    return len(winning & mine)

def calculate_points(matches):
    return 2 ** (matches - 1) if matches > 0 else 0

def part1(lines):
    total = 0
    for line in lines:
        _, winning, mine = parse_card(line)
        matches = count_matches(winning, mine)
        total += calculate_points(matches)
    return total

def part2(lines):
    card_counts = defaultdict(int)
    
    for line in lines:
        card_id, winning, mine = parse_card(line)
        card_counts[card_id] += 1
        matches = count_matches(winning, mine)
        
        for next_card in range(card_id + 1, card_id + matches + 1):
            card_counts[next_card] += card_counts[card_id]
    
    return sum(card_counts.values())

def main():
    lines = read_input("2023/Day04/input.txt")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()