def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def calculate_positions(commands):
    horizontal = 0
    depth = 0
    aim = 0
    depth_with_aim = 0

    for command in commands:
        action, value = command.split()
        value = int(value)

        if action == 'forward':
            horizontal += value
            depth_with_aim += aim * value
        elif action == 'down':
            aim += value
            depth += value
        elif action == 'up':
            aim -= value
            depth -= value

    return horizontal * depth, horizontal * depth_with_aim

def main():
    print("\n--- Day 2: Dive! ---")
    commands = read_input('2021/input/day02.txt')

    result, result_with_aim = calculate_positions(commands)
    print(f"Part 1: {result}")
    print(f"Part 2: {result_with_aim}")

if __name__ == "__main__":
    main()