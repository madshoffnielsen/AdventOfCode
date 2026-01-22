from typing import List
import functools

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def part1(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    # Find S
    start_col = -1
    for j in range(cols):
        if grid[0][j] == 'S':
            start_col = j
            break
    if start_col == -1:
        return 0
    active = set([(1, start_col)])
    splits = 0
    while active:
        new_active = set()
        for r, c in list(active):
            if r >= rows or c < 0 or c >= cols:
                continue
            cell = grid[r][c]
            if cell == '^':
                splits += 1
                left_c = c - 1
                right_c = c + 1
                if left_c >= 0:
                    new_active.add((r + 1, left_c))
                if right_c < cols:
                    new_active.add((r + 1, right_c))
            elif cell == '.':
                new_active.add((r + 1, c))
        active = new_active
    return splits

def part2(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    start_col = -1
    for j in range(cols):
        if grid[0][j] == 'S':
            start_col = j
            break
    if start_col == -1:
        return 0
    @functools.lru_cache(maxsize=None)
    def count_timelines(r, c):
        if r >= rows:
            return 1
        if c < 0 or c >= cols:
            return 0
        cell = grid[r][c]
        if cell == '^':
            left = count_timelines(r + 1, c - 1) if c - 1 >= 0 else 0
            right = count_timelines(r + 1, c + 1) if c + 1 < cols else 0
            return left + right
        elif cell == '.':
            return count_timelines(r + 1, c)
        else:
            return 0
    return count_timelines(1, start_col)

def main() -> None:
    grid = read_input("2025/Day07/input.txt")
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

if __name__ == "__main__":
    main()