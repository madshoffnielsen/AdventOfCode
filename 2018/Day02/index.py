from collections import Counter

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def part1(box_ids):
    twos = threes = 0
    for box_id in box_ids:
        counts = Counter(box_id).values()
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
    return twos * threes

def part2(box_ids):
    for i in range(len(box_ids)):
        for j in range(i + 1, len(box_ids)):
            common_chars = [char1 for char1, char2 in zip(box_ids[i], box_ids[j]) if char1 == char2]
            if len(common_chars) == len(box_ids[i]) - 1:
                return ''.join(common_chars)
    return None

if __name__ == "__main__":
    input_file = "2018/Day02/input.txt"
    box_ids = read_input(input_file)
    
    result_part1 = part1(box_ids)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(box_ids)
    print(f"Part 2: {result_part2}")