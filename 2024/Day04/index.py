from typing import List, Set, Tuple

def read_input(file_path: str) -> List[List[str]]:
    """Read and return the word search grid."""
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            grid.append([x for x in line.strip()])
    return grid

def find_word(grid: List[List[str]], word: str) -> int:
    """Find all occurrences of word in grid (horizontal, vertical, diagonal)."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    word_rev = word[::-1]  # Reversed word for backward search
    
    # Row search
    for row in grid:
        for i in range(cols - len(word) + 1):
            current = ''.join(row[i:i+len(word)])
            count += (current == word or current == word_rev)
    
    # Column search
    for col in zip(*grid):
        for i in range(rows - len(word) + 1):
            current = ''.join(col[i:i+len(word)])
            count += (current == word or current == word_rev)
    
    # Diagonal search
    for row in range(rows - len(word) + 1):
        for col in range(cols - len(word) + 1):
            # Forward diagonal
            diag1 = ''.join(grid[row+i][col+i] for i in range(len(word)))
            count += (diag1 == word or diag1 == word_rev)
            
            # Backward diagonal
            if row + len(word) <= rows and col >= len(word) - 1:
                diag2 = ''.join(grid[row+i][col-i] for i in range(len(word)))
                count += (diag2 == word or diag2 == word_rev)
    
    return count

def find_xmas_pattern(grid: List[List[str]]) -> int:
    """Find X-MAS patterns in grid."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    valid_diagonals = {'MAS', 'SAM'}
    
    for row in range(rows - 2):
        for col in range(cols - 2):
            # Check center 'A'
            if grid[row+1][col+1] != 'A':
                continue
                
            # Check diagonals
            diag1 = ''.join([grid[row][col], 
                            grid[row+1][col+1], 
                            grid[row+2][col+2]])
            diag2 = ''.join([grid[row+2][col], 
                            grid[row+1][col+1], 
                            grid[row][col+2]])
            
            if diag1 in valid_diagonals and diag2 in valid_diagonals:
                count += 1
    
    return count

def main():
    """Main program."""
    print("\n--- Day 4: Ceres Search ---")
    
    grid = read_input("2024/Day04/input.txt")
    
    result1 = find_word(grid, "XMAS")
    print(f"Part 1: {result1}")
    
    result2 = find_xmas_pattern(grid)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()