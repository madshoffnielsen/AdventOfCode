from collections import Counter
from enum import IntEnum
from functools import total_ordering

class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

@total_ordering
class Hand:
    def __init__(self, cards, bid, use_jokers=False):
        self.cards = cards
        self.bid = bid
        self.use_jokers = use_jokers
        self.type = self._calculate_type()
        
    def _calculate_type(self):
        if self.use_jokers:
            counts = Counter(c for c in self.cards if c != 'J')
            jokers = self.cards.count('J')
            if jokers == 5:
                return HandType.FIVE_KIND
            most_common = counts.most_common(1)[0][1] + jokers
        else:
            counts = Counter(self.cards)
            most_common = counts.most_common(1)[0][1]
            
        if most_common == 5:
            return HandType.FIVE_KIND
        if most_common == 4:
            return HandType.FOUR_KIND
        if most_common == 3:
            if len(counts) == 2:
                return HandType.FULL_HOUSE
            return HandType.THREE_KIND
        if most_common == 2:
            if len(counts) == 3:
                return HandType.TWO_PAIR
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD
    
    def _card_strength(self, card):
        if self.use_jokers:
            return "J23456789TQKA".index(card)
        return "23456789TJQKA".index(card)
    
    def __eq__(self, other):
        return self.cards == other.cards
    
    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for s, o in zip(self.cards, other.cards):
            if s != o:
                return self._card_strength(s) < self._card_strength(o)
        return False

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

def calculate_winnings(hands):
    return sum(i * hand.bid for i, hand in enumerate(sorted(hands), 1))

def part1(lines):
    hands = [Hand(cards, int(bid)) for cards, bid in lines]
    return calculate_winnings(hands)

def part2(lines):
    hands = [Hand(cards, int(bid), True) for cards, bid in lines]
    return calculate_winnings(hands)

def main():
    lines = read_input("2023/Day07/input.txt")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()