from collections import defaultdict
import heapq
from typing import Dict, List, Set, Tuple, DefaultDict

# Type aliases for better readability
Position = Tuple[int, int]
Direction = Tuple[int, int]
Blizzard = Tuple[Position, Direction]
State = Tuple[List[Blizzard], int, int, Position, Position]
BlizzardCache = Dict[int, DefaultDict[Position, List[Blizzard]]]

def read_input(file_path: str) -> Tuple[Position, Position, List[Blizzard], int, int]:
    DIRECTIONS = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    
    with open(file_path, "r") as f:
        lines = f.read().splitlines()
        
    board_height = len(lines) - 2
    board_width = len(lines[1]) - 2
    elf_start = (lines[0].index(".") - 1, -1)
    elf_end = (lines[-1].index(".") - 1, board_height)
    
    blizzards = [
        ((x-1, y-1), DIRECTIONS[char])
        for y, line in enumerate(lines[1:-1], 1)
        for x, char in enumerate(line[1:-1], 1)
        if char in DIRECTIONS
    ]
    
    return elf_start, elf_end, blizzards, board_width, board_height

def simulate_blizzards(state: State, time: int, blizzard_cache: BlizzardCache) -> DefaultDict[Position, List[Blizzard]]:
    if time in blizzard_cache:
        return blizzard_cache[time]
    
    blizzards, board_width, board_height = state[:3]
    positions: DefaultDict[Position, List[Blizzard]] = defaultdict(list)
    
    for blizzard in blizzards:
        pos, direction = blizzard
        x = (pos[0] + direction[0] * time) % board_width
        y = (pos[1] + direction[1] * time) % board_height
        positions[(x, y)].append(blizzard)
    
    blizzard_cache[time] = positions
    return positions

def get_valid_moves(pos: Position, state: State, time: int, blizzard_cache: BlizzardCache) -> List[Position]:
    DIRECTIONS = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    _, board_width, board_height, elf_start, elf_end = state
    
    blizzard_positions = simulate_blizzards(state, time + 1, blizzard_cache)
    
    return [
        (pos[0] + dx, pos[1] + dy)
        for dx, dy in DIRECTIONS
        if (new_pos := (pos[0] + dx, pos[1] + dy)) not in blizzard_positions
        and (new_pos == elf_end or new_pos == elf_start or 
             (0 <= new_pos[0] < board_width and 0 <= new_pos[1] < board_height))
    ]

def find_shortest_path(state: State, start_pos: Position, end_pos: Position, 
                      start_time: int, blizzard_cache: BlizzardCache) -> int:
    heap = [(0, start_pos, start_time)]
    visited: Set[Tuple[Position, int]] = set()

    while heap:
        _, pos, time = heapq.heappop(heap)
        if pos == end_pos:
            return time
        
        if (pos, time) not in visited:
            visited.add((pos, time))
            time_plus_one = time + 1
            for move in get_valid_moves(pos, state, time, blizzard_cache):
                manhattan_dist = abs(move[0] - end_pos[0]) + abs(move[1] - end_pos[1])
                heapq.heappush(heap, (manhattan_dist + time, move, time_plus_one))
    
    return float('inf')

def part2(state: State, blizzard_cache: BlizzardCache, time1) -> int:
    elf_start, elf_end = state[3:5]
    time2 = find_shortest_path(state, elf_end, elf_start, time1, blizzard_cache)
    return find_shortest_path(state, elf_start, elf_end, time2, blizzard_cache)

def main():
    print("\n--- Day 24: Blizzard Basin ---")
    file_path = "2022/input/day24.txt"
    
    # Parse input and create initial state
    elf_start, elf_end, blizzards, board_width, board_height = read_input(file_path)
    state = (blizzards, board_width, board_height, elf_start, elf_end)
    blizzard_cache: BlizzardCache = {}

    # Part 1
    result1 = find_shortest_path(state, state[3], state[4], 0, blizzard_cache)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(state, blizzard_cache, result1)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()