def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip()

def generate_next_row(row):
    next_row = []
    for i in range(len(row)):
        left = row[i - 1] if i > 0 else '.'
        center = row[i]
        right = row[i + 1] if i < len(row) - 1 else '.'
        if (left == '^' and center == '^' and right == '.') or \
           (left == '.' and center == '^' and right == '^') or \
           (left == '^' and center == '.' and right == '.') or \
           (left == '.' and center == '.' and right == '^'):
            next_row.append('^')
        else:
            next_row.append('.')
    return ''.join(next_row)

def count_safe_tiles(initial_row, num_rows):
    row = initial_row
    safe_tiles = row.count('.')
    for _ in range(num_rows - 1):
        row = generate_next_row(row)
        safe_tiles += row.count('.')
    return safe_tiles

def part1(initial_row):
    return count_safe_tiles(initial_row, 40)

def part2(initial_row):
    return count_safe_tiles(initial_row, 400000)

if __name__ == "__main__":
    initial_row = parse_input("2016/Day18/input.txt")
    print("Part 1:", part1(initial_row))
    print("Part 2:", part2(initial_row))