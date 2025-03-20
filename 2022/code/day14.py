def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def parse_input(lines):
    R = []
    y_max = float('-inf')

    for line in lines:
        segments = line.split(' -> ')
        path = []
        for segment in segments:
            x, y = map(int, segment.split(','))
            y_max = max(y_max, y)
            path.append((x, y))
        R.append(path)

    return R, y_max

def build_cave(R, y_max):
    w = 500
    dx = -(500 - w // 2)
    h = y_max + 2

    # Initialize the cave grid
    C = [['.'] * w for _ in range(h)]
    C[0][500 + dx] = '+'
    C.append(['#'] * w)

    # Fill the cave grid based on the input paths
    for path in R:
        x1, y1 = path.pop(0)
        while path:
            x2, y2 = path.pop(0)
            if x1 < x2:
                for x in range(x1, x2 + 1):
                    C[y1][x + dx] = '#'
            elif x2 < x1:
                for x in range(x2, x1 + 1):
                    C[y2][x + dx] = '#'
            elif y1 != y2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    C[y][x1 + dx] = '#'
            x1, y1 = x2, y2

    return C, dx

def simulate_sand(C, dx, y_max):
    part1 = part2 = sand = 0

    while True:
        px, py = 500 + dx, 0
        while True:
            if py > y_max and not part1:
                part1 = sand
            # Move sand
            if C[py + 1][px] == '.':
                py += 1
            elif C[py + 1][px - 1] == '.':
                py += 1
                px -= 1
            elif C[py + 1][px + 1] == '.':
                py += 1
                px += 1
            else:
                C[py][px] = 'o'
                sand += 1
                break
        if py == 0:
            part2 = sand
            break

    return part1, part2

def main():
    print("\n--- Day 14: Regolith Reservoir ---")
    lines = read_input('2022/input/day14.txt')
    R, y_max = parse_input(lines)
    C, dx = build_cave(R, y_max)
    part1, part2 = simulate_sand(C, dx, y_max)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()