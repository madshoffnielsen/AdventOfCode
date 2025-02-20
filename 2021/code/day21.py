import re
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return input_data

def parse_input(input_data):
    matches = re.findall(r"Player (\d+) starting position: (\d+)", input_data)
    players = {int(match[0]): {"start": int(match[1]), "score": 0, "pos": int(match[1])} for match in matches}
    return players

def play_deterministic_dice(players):
    dice = 0
    turn = 1
    rolled = 0
    while True:
        roll = sum((dice := dice + 1) % 100 or 100 for _ in range(3))
        rolled += 3
        space = (players[turn]["pos"] + roll) % 10 or 10
        players[turn]["pos"] = space
        players[turn]["score"] += space
        if players[turn]["score"] >= 1000:
            break
        turn = 2 if turn == 1 else 1
    loser = 2 if turn == 1 else 1
    return players[loser]["score"] * rolled

def dirac(players, turn, universes, goes, states, wins):
    initial_score = players[turn]["score"]
    initial_pos = players[turn]["pos"]
    for rolls, times in states.items():
        space = (initial_pos + rolls) % 10 or 10
        players[turn]["pos"] = space
        players[turn]["score"] = initial_score + space
        if players[turn]["score"] >= 21:
            wins[turn] += universes * times
        else:
            next_turn = 2 if turn == 1 else 1
            dirac(players, next_turn, universes * times, goes + 1, states, wins)
        players[turn]["score"] = initial_score
        players[turn]["pos"] = initial_pos

def play_quantum_dice(players):
    states = defaultdict(int)
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                states[a + b + c] += 1
    wins = {1: 0, 2: 0}
    dirac(players, 1, 1, 0, states, wins)
    return max(wins.values())

def main():
    print("\n--- Day 21: Dirac Dice ---")
    input_file = '2021/input/day21.txt'
    input_data = read_input(input_file)
    players = parse_input(input_data)

    # Part 1
    result = play_deterministic_dice(players)
    print(f"Part 1: {result}")

    # Reset players for Part 2
    players = parse_input(input_data)

    # Part 2
    result = play_quantum_dice(players)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()