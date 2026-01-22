from typing import List

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def count_accessible(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                neighbors = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                            neighbors += 1
                if neighbors < 4:
                    count += 1
    return count

def part1(grid: List[str]) -> int:
    return count_accessible(grid)

def part2(grid: List[str]) -> int:
    g = [list(row) for row in grid]
    total_removed = 0
    while True:
        to_remove = []
        rows = len(g)
        cols = len(g[0])
        for i in range(rows):
            for j in range(cols):
                if g[i][j] == '@':
                    neighbors = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < rows and 0 <= nj < cols and g[ni][nj] == '@':
                                neighbors += 1
                    if neighbors < 4:
                        to_remove.append((i, j))
        if not to_remove:
            break
        for i, j in to_remove:
            g[i][j] = '.'
        total_removed += len(to_remove)
    return total_removed

def main() -> None:
    grid = read_input("2025/Day04/input.txt")
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

if __name__ == "__main__":
    main()