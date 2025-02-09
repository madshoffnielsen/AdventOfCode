def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def move(position, direction, keypad):
    x, y = position
    if direction == 'U' and y > 0 and keypad[y-1][x] != ' ':
        y -= 1
    elif direction == 'D' and y < len(keypad) - 1 and keypad[y+1][x] != ' ':
        y += 1
    elif direction == 'L' and x > 0 and keypad[y][x-1] != ' ':
        x -= 1
    elif direction == 'R' and x < len(keypad[0]) - 1 and keypad[y][x+1] != ' ':
        x += 1
    return (x, y)

def part1(instructions):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    position = (1, 1)  # Start at '5'
    code = []

    for instruction in instructions:
        for direction in instruction:
            position = move(position, direction, keypad)
        code.append(keypad[position[1]][position[0]])

    return ''.join(code)

def part2(instructions):
    keypad = [
        [' ', ' ', '1', ' ', ' '],
        [' ', '2', '3', '4', ' '],
        ['5', '6', '7', '8', '9'],
        [' ', 'A', 'B', 'C', ' '],
        [' ', ' ', 'D', ' ', ' ']
    ]
    position = (0, 2)  # Start at '5'
    code = []

    for instruction in instructions:
        for direction in instruction:
            position = move(position, direction, keypad)
        code.append(keypad[position[1]][position[0]])

    return ''.join(code)

if __name__ == "__main__":
    instructions = parse_input("2016/Day02/input.txt")
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))