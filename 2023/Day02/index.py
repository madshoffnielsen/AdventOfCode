import re
from math import prod

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def parse_game(line):
    game_id = int(re.match(r"Game (\d+):", line).group(1))
    sets = line.split(": ")[1].split("; ")
    
    game_sets = []
    for set_info in sets:
        cubes = {"red": 0, "green": 0, "blue": 0}
        for cube in set_info.split(", "):
            count, color = cube.split()
            cubes[color] = int(count)
        game_sets.append(cubes)
    
    return game_id, game_sets

def is_game_possible(game_sets, limits):
    return all(
        all(set_info[color] <= limits[color] for color in limits)
        for set_info in game_sets
    )

def find_minimum_cubes(game_sets):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for set_info in game_sets:
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], set_info[color])
    return min_cubes

def part1(lines):
    limits = {"red": 12, "green": 13, "blue": 14}
    total = 0
    
    for line in lines:
        game_id, game_sets = parse_game(line)
        if is_game_possible(game_sets, limits):
            total += game_id
            
    return total

def part2(lines):
    total = 0
    
    for line in lines:
        _, game_sets = parse_game(line)
        min_cubes = find_minimum_cubes(game_sets)
        total += prod(min_cubes.values())
        
    return total

def main():
    lines = read_input("2023/Day02/input.txt")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()