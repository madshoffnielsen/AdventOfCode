def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def parse_instruction(instruction):
    parts = instruction.split()
    if parts[0] == "toggle":
        action = "toggle"
        start = tuple(map(int, parts[1].split(',')))
        end = tuple(map(int, parts[3].split(',')))
    else:
        action = "on" if parts[1] == "on" else "off"
        start = tuple(map(int, parts[2].split(',')))
        end = tuple(map(int, parts[4].split(',')))
    return action, start, end

def apply_instruction_part1(grid, instruction):
    action, start, end = parse_instruction(instruction)
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if action == "toggle":
                grid[x][y] = not grid[x][y]
            elif action == "on":
                grid[x][y] = True
            elif action == "off":
                grid[x][y] = False

def apply_instruction_part2(grid, instruction):
    action, start, end = parse_instruction(instruction)
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if action == "toggle":
                grid[x][y] += 2
            elif action == "on":
                grid[x][y] += 1
            elif action == "off":
                grid[x][y] = max(0, grid[x][y] - 1)

def part1(instructions):
    grid = [[False] * 1000 for _ in range(1000)]
    for instruction in instructions:
        apply_instruction_part1(grid, instruction)
    return sum(sum(row) for row in grid)

def part2(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    for instruction in instructions:
        apply_instruction_part2(grid, instruction)
    return sum(sum(row) for row in grid)

def main():
    instructions = read_input("2015/Day06/input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

if __name__ == "__main__":
    main()