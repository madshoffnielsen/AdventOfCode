def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def check_visibility(x, y, row, col):
    xl = max(row[:x])
    xr = max(row[x+1:])
    xt = max(col[:y])
    xb = max(col[y+1:])

    if xl < row[x] or xr < row[x] or xt < row[x] or xb < row[x]:
        return 1
    return 0

def check_scenic_score(x, y, row, col):
    current_tree = row[x]

    xl = xr = xt = xb = 0

    for i in range(x-1, -1, -1):
        xl += 1
        if row[i] >= current_tree:
            break

    for i in range(x+1, len(row)):
        xr += 1
        if row[i] >= current_tree:
            break

    for i in range(y-1, -1, -1):
        xt += 1
        if col[i] >= current_tree:
            break

    for i in range(y+1, len(col)):
        xb += 1
        if col[i] >= current_tree:
            break

    return xl * xr * xt * xb

def process_grid(lines):
    grid = [list(line) for line in lines]

    total_score = 0
    total_score_part2 = 0

    rows = len(grid)
    cols = len(grid[0])

    total_score += (2 * cols) + (2 * (rows - 2))

    for x in range(1, cols-1):
        col = [grid[y][x] for y in range(rows)]

        for y in range(1, rows-1):
            row = grid[y]
            total_score += check_visibility(x, y, row, col)

    for x in range(cols):
        col = [grid[y][x] for y in range(rows)]
        for y in range(rows):
            row = grid[y]
            score = check_scenic_score(x, y, row, col)
            if score > total_score_part2:
                total_score_part2 = score

    return total_score, total_score_part2

def main():
    print("\n--- Day 8: Treetop Tree House ---")
    lines = read_input('2022/input/day08.txt')
    total_score, total_score_part2 = process_grid(lines)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()