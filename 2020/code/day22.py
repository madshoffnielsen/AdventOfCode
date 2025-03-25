from collections import deque
from typing import Tuple, Deque, Set

Deck = Deque[int]
GameState = Tuple[Tuple[int, ...], Tuple[int, ...]]

def read_input(file_path: str) -> Tuple[Deck, Deck]:
    """Read player decks from file."""
    with open(file_path) as f:
        p1, p2 = f.read().strip().split('\n\n')
    return (
        deque(int(x) for x in p1.splitlines()[1:]),
        deque(int(x) for x in p2.splitlines()[1:])
    )

def play_combat(p1: Deck, p2: Deck) -> Deck:
    """Play regular combat game."""
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return p1 if p1 else p2

def play_recursive_combat(p1: Deck, p2: Deck) -> Tuple[int, Deck]:
    """Play recursive combat game."""
    seen: Set[GameState] = set()
    
    while p1 and p2:
        state = (tuple(p1), tuple(p2))
        if state in seen:
            return 1, p1
        seen.add(state)
        
        c1, c2 = p1.popleft(), p2.popleft()
        
        if len(p1) >= c1 and len(p2) >= c2:
            winner, _ = play_recursive_combat(
                deque(list(p1)[:c1]),
                deque(list(p2)[:c2])
            )
            if winner == 1:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])
        else:
            if c1 > c2:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])
    
    return (1, p1) if p1 else (2, p2)

def calculate_score(deck: Deck) -> int:
    """Calculate final score of a deck."""
    return sum(i * card for i, card in enumerate(reversed(deck), 1))

def part1(p1: Deck, p2: Deck) -> int:
    """Play regular combat and get winner's score."""
    winner = play_combat(p1.copy(), p2.copy())
    return calculate_score(winner)

def part2(p1: Deck, p2: Deck) -> int:
    """Play recursive combat and get winner's score."""
    _, winning_deck = play_recursive_combat(p1.copy(), p2.copy())
    return calculate_score(winning_deck)

def main():
    """Main program."""
    print("\n--- Day 22: Crab Combat ---")
    
    p1, p2 = read_input("2020/input/day22.txt")
    
    result1 = part1(p1, p2)
    print(f"Part 1: {result1}")
    
    result2 = part2(p1, p2)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()