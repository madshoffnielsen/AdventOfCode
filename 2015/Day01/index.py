def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip()

def part1(directions):
    floor = 0
    for char in directions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

def part2(directions):
    floor = 0
    for i, char in enumerate(directions):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return i + 1

def main():
    directions = read_input("2015/Day01/input.txt")
    print(f"Part 1: {part1(directions)}")
    print(f"Part 2: {part2(directions)}")

if __name__ == "__main__":
    main()