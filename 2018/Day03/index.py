import re
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def parse_claim(claim):
    claim_id, x, y, width, height = map(int, re.findall(r'\d+', claim))
    return claim_id, x, y, width, height

def part1(claims):
    fabric = defaultdict(int)
    for claim in claims:
        _, x, y, width, height = parse_claim(claim)
        for i in range(x, x + width):
            for j in range(y, y + height):
                fabric[(i, j)] += 1
    return sum(1 for square in fabric.values() if square > 1)

def part2(claims):
    fabric = defaultdict(int)
    claim_dict = {}
    for claim in claims:
        claim_id, x, y, width, height = parse_claim(claim)
        claim_dict[claim_id] = (x, y, width, height)
        for i in range(x, x + width):
            for j in range(y, y + height):
                fabric[(i, j)] += 1

    for claim_id, (x, y, width, height) in claim_dict.items():
        if all(fabric[(i, j)] == 1 for i in range(x, x + width) for j in range(y, y + height)):
            return claim_id
    return None

if __name__ == "__main__":
    input_file = "2018/Day03/input.txt"
    claims = read_input(input_file)
    
    result_part1 = part1(claims)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(claims)
    print(f"Part 2: {result_part2}")