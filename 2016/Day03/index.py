def parse_input(file_path):
    with open(file_path) as f:
        return [list(map(int, line.split())) for line in f]

def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

def part1(triangles):
    valid_count = 0
    for sides in triangles:
        if is_valid_triangle(sides):
            valid_count += 1
    return valid_count

def part2(triangles):
    valid_count = 0
    for i in range(0, len(triangles), 3):
        for j in range(3):
            sides = [triangles[i][j], triangles[i+1][j], triangles[i+2][j]]
            if is_valid_triangle(sides):
                valid_count += 1
    return valid_count

if __name__ == "__main__":
    triangles = parse_input("2016/Day03/input.txt")
    print("Part 1:", part1(triangles))
    print("Part 2:", part2(triangles))