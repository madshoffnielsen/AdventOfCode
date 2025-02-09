def parse_input(file_path):
    rules = {}
    with open(file_path) as f:
        for line in f:
            pattern, result = line.strip().split(" => ")
            rules[pattern] = result
    return rules

def rotate(pattern):
    return list(zip(*pattern[::-1]))

def flip(pattern):
    return [row[::-1] for row in pattern]

def get_variations(pattern):
    variations = set()
    for _ in range(4):
        pattern = rotate(pattern)
        variations.add(tuple(map(tuple, pattern)))
        variations.add(tuple(map(tuple, flip(pattern))))
    return variations

def enhance(rules, grid):
    size = len(grid)
    if size % 2 == 0:
        step = 2
    else:
        step = 3

    new_grid = []
    for i in range(0, size, step):
        new_rows = [[] for _ in range(step + 1)]
        for j in range(0, size, step):
            block = [row[j:j+step] for row in grid[i:i+step]]
            for variation in get_variations(block):
                pattern = "/".join("".join(row) for row in variation)
                if pattern in rules:
                    result = rules[pattern].split("/")
                    for k, row in enumerate(result):
                        new_rows[k].extend(row)
                    break
        new_grid.extend(new_rows)
    return new_grid

def count_on(grid):
    return sum(row.count('#') for row in grid)

def main(file_path, iterations):
    rules = parse_input(file_path)
    grid = [list(".#."), list("..#"), list("###")]

    for _ in range(iterations):
        grid = enhance(rules, grid)

    return count_on(grid)

if __name__ == "__main__":
    print("Part 1:", main("2017/Day21/input.txt", 5))
    print("Part 2:", main("2017/Day21/input.txt", 18))