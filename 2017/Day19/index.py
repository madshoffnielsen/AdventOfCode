def read_input(file_path):
    with open(file_path) as f:
        return [list(line.rstrip('\n')) for line in f]

def follow_path(grid):
    # Find starting position
    x = 0
    y = grid[0].index('|')
    dx, dy = 1, 0  # Moving down initially
    
    letters = []
    steps = 0
    
    while True:
        steps += 1
        x += dx
        y += dy
        
        # Check if we're out of bounds or hit a space
        if (x < 0 or x >= len(grid) or y < 0 or 
            y >= len(grid[x]) or grid[x][y] == ' '):
            break
        
        current = grid[x][y]
        
        if current.isalpha():
            letters.append(current)
        elif current == '+':
            # Change direction at intersection
            if dx != 0:  # Moving vertically
                dx = 0
                if y+1 < len(grid[x]) and grid[x][y+1] != ' ':
                    dy = 1  # Try right
                else:
                    dy = -1  # Must be left
            else:  # Moving horizontally
                dy = 0
                if x+1 < len(grid) and grid[x+1][y] != ' ':
                    dx = 1  # Try down
                else:
                    dx = -1  # Must be up
    
    return ''.join(letters), steps

def main():
    grid = read_input("2017/Day19/input.txt")
    letters, steps = follow_path(grid)
    print(f"Part 1: {letters}")
    print(f"Part 2: {steps}")

if __name__ == "__main__":
    main()