import re
from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        line = file.read().strip()
        players, last_marble = map(int, re.findall(r'\d+', line))
        return players, last_marble

def play_game(players, last_marble):
    scores = [0] * players
    circle = deque([0])
    
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    
    return max(scores)

def part1(players, last_marble):
    return play_game(players, last_marble)

def part2(players, last_marble):
    return play_game(players, last_marble * 100)

if __name__ == "__main__":
    input_file = "2018/Day09/input.txt"
    players, last_marble = read_input(input_file)
    
    result_part1 = part1(players, last_marble)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(players, last_marble)
    print(f"Part 2: {result_part2}")