from functools import cache
from typing import List

def read_input(file_path: str) -> List[int]:
    with open(file_path) as f:
        return [int(x) for x in f.read().strip().split()]

@cache
def transform_stone(value: int) -> List[int]:
    length = len(str(value))
    if value==0:
        return 1
    elif length%2==0:
        return [int(str(value)[:length//2]), int(str(value)[length//2:])]
    else:
        return value*2024

@cache
def blink_stones(number: int, iterations:int) -> int:
    overall=number
    splits=0
    for i in range(iterations):
        value=transform_stone(overall)
        if isinstance(value, int):
            overall=value
        if isinstance(value, list):
            splits+=1
            overall=value[0]
            splits+=blink_stones(value[1], iterations-i-1)
    return splits

def count_stones_after_blinks(stones: List[int], blinks: int) -> int:
    sum=0
    for i, number in enumerate(stones):
        sum+=blink_stones(number, blinks)
    
    return sum+len(stones)

def main():
    print("\n--- Day 11: Plutonian Pebbles ---")
    
    stones = read_input("2024/Day11/input.txt")
    
    result = count_stones_after_blinks(stones, 25)
    print(f"Part 1: {result}")

    result = count_stones_after_blinks(stones, 75)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
