from typing import List, Tuple
from collections import deque

def read_matrix(file_path: str) -> List[List[int]]:
    matrix = []
    with open(file_path, 'r') as f:
        for line in f:
            row = [int(x) for x in line.strip()]
            matrix.append(row)
    return matrix

def find_zeros(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    zeros = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zeros.append((row, col))
    return zeros

def find_hiking_trails(matrix: List[List[int]], zero_positions: List[Tuple[int, int]]) -> dict:
    """Find all valid hiking trails from each trailhead (zero position) to height 9."""
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    trailhead_scores = {}

    def is_valid(x: int, y: int) -> bool:
        """Check if position is within matrix bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def find_trails(start: Tuple[int, int]) -> int:
        """Find number of reachable height-9 positions from start position."""
        queue = deque([(start[0], start[1], {start})])
        reachable_nines = set()

        while queue:
            x, y, path = queue.popleft()
            current_height = matrix[x][y]

            if current_height == 9:
                reachable_nines.add((x, y))
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (is_valid(nx, ny) and 
                    (nx, ny) not in path and 
                    matrix[nx][ny] == current_height + 1):
                    queue.append((nx, ny, path | {(nx, ny)}))

        return len(reachable_nines)

    # Process each trailhead
    for start_pos in zero_positions:
        if matrix[start_pos[0]][start_pos[1]] == 0:  # Verify it's a trailhead
            score = find_trails(start_pos)
            trailhead_scores[start_pos] = score

    return trailhead_scores

def find_hiking_trail_ratings(matrix: List[List[int]], zero_positions: List[Tuple[int, int]]) -> dict:
    """Find number of distinct hiking trails from each trailhead."""
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    trailhead_ratings = {}

    def is_valid(x: int, y: int) -> bool:
        """Check if position is within matrix bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def count_trails(start: Tuple[int, int]) -> int:
        """Count distinct trails reaching height 9 from start position."""
        distinct_trails = set()
        queue = deque([(start[0], start[1], tuple())])  # Path stored as tuple for hashability

        while queue:
            x, y, path = queue.popleft()
            current_height = matrix[x][y]
            path = path + ((x, y),)  # Add current position to path

            if current_height == 9:
                distinct_trails.add(path)
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (is_valid(nx, ny) and 
                    (nx, ny) not in path and 
                    matrix[nx][ny] == current_height + 1):
                    queue.append((nx, ny, path))

        return len(distinct_trails)

    # Process each trailhead
    for start_pos in zero_positions:
        if matrix[start_pos[0]][start_pos[1]] == 0:
            rating = count_trails(start_pos)
            trailhead_ratings[start_pos] = rating

    return trailhead_ratings

def main():
    matrix = read_matrix("2024/Day10/input.txt")
    zero_positions = find_zeros(matrix)
    
    trail_scores = find_hiking_trails(matrix, zero_positions)
    print(f"Part 1: {sum(trail_scores.values())}")
    
    trail_ratings = find_hiking_trail_ratings(matrix, zero_positions)
    print(f"Part 2: {sum(trail_ratings.values())}")

if __name__ == "__main__":
    main()