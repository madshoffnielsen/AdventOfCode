from collections import deque

def parse_input(filename):
    with open(filename) as f:
        p1, p2 = f.read().strip().split('\n\n')
    return (
        deque(int(x) for x in p1.splitlines()[1:]),
        deque(int(x) for x in p2.splitlines()[1:])
    )

def play_combat(p1, p2):
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return p1 if p1 else p2

def play_recursive_combat(p1, p2):
    seen = set()
    
    while p1 and p2:
        # Check for repeated game state
        state = (tuple(p1), tuple(p2))
        if state in seen:
            return 1, p1
        seen.add(state)
        
        c1, c2 = p1.popleft(), p2.popleft()
        
        # Determine round winner
        if len(p1) >= c1 and len(p2) >= c2:
            # Recursive combat
            winner, _ = play_recursive_combat(
                deque(list(p1)[:c1]),
                deque(list(p2)[:c2])
            )
            if winner == 1:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])
        else:
            # Normal combat
            if c1 > c2:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])
    
    return (1, p1) if p1 else (2, p2)

def calculate_score(deck):
    return sum(i * card for i, card in enumerate(reversed(deck), 1))

def part1(p1, p2):
    winner = play_combat(p1.copy(), p2.copy())
    return calculate_score(winner)

def part2(p1, p2):
    _, winning_deck = play_recursive_combat(p1.copy(), p2.copy())
    return calculate_score(winning_deck)

def main():
    p1, p2 = parse_input("2020/Day22/input.txt")
    print(f"Part 1: {part1(p1, p2)}")
    print(f"Part 2: {part2(p1, p2)}")

if __name__ == "__main__":
    main()