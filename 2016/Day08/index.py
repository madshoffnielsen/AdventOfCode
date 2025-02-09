def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def initialize_screen(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def rect(screen, width, height):
    for y in range(height):
        for x in range(width):
            screen[y][x] = '#'

def rotate_row(screen, row, shift):
    screen[row] = screen[row][-shift:] + screen[row][:-shift]

def rotate_column(screen, col, shift):
    column = [screen[y][col] for y in range(len(screen))]
    column = column[-shift:] + column[:-shift]
    for y in range(len(screen)):
        screen[y][col] = column[y]

def execute_instruction(screen, instruction):
    if instruction.startswith("rect"):
        _, size = instruction.split()
        width, height = map(int, size.split('x'))
        rect(screen, width, height)
    elif instruction.startswith("rotate row"):
        parts = instruction.split()
        row = int(parts[2].split('=')[1])
        shift = int(parts[4])
        rotate_row(screen, row, shift)
    elif instruction.startswith("rotate column"):
        parts = instruction.split()
        col = int(parts[2].split('=')[1])
        shift = int(parts[4])
        rotate_column(screen, col, shift)

def count_lit_pixels(screen):
    return sum(row.count('#') for row in screen)

def display_screen(screen):
    for row in screen:
        print(''.join(row))

def part1_and_part2(instructions):
    screen = initialize_screen(50, 6)
    for instruction in instructions:
        execute_instruction(screen, instruction)
    display_screen(screen)
    return count_lit_pixels(screen)

if __name__ == "__main__":
    instructions = parse_input("2016/Day08/input.txt")
    print("Part 1 and Part 2:")
    print("Lit pixels:", part1_and_part2(instructions))