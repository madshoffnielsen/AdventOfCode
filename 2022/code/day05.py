def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def process_instructions(lines):
    ship = {i: [] for i in range(10)}
    ship_part2 = {i: [] for i in range(10)}

    for line in lines:
        input_data = [line[i:i+4].strip() for i in range(0, len(line), 4)]

        if input_data[0] != 'move' and not input_data[0].isdigit():
            for key, value in enumerate(input_data):
                if value:
                    value = value.replace('[', '').replace(']', '').strip()
                    ship[key + 1].append(value)
                    ship_part2[key + 1].append(value)

        if input_data[0] == 'move':
            move_cmd = line.strip().split(' ')
            amount = int(move_cmd[1])
            from_stack = int(move_cmd[3])
            to_stack = int(move_cmd[5])

            for _ in range(amount):
                val = ship[from_stack].pop(0)
                ship[to_stack].insert(0, val)

            crane = []

            for _ in range(amount):
                crane.append(ship_part2[from_stack].pop(0))
            for val in reversed(crane):
                ship_part2[to_stack].insert(0, val)

    return ship, ship_part2

def calculate_scores(ship, ship_part2):
    total_score = ''
    total_score_part2 = ''

    for key, value in ship.items():
        if value:
            total_score += value[0]

    for key, value in ship_part2.items():
        if value:
            total_score_part2 += value[0]

    return total_score, total_score_part2

def main():
    print("\n--- Day 5: Supply Stacks ---")
    lines = read_input('2022/input/day05.txt')
    ship, ship_part2 = process_instructions(lines)
    total_score, total_score_part2 = calculate_scores(ship, ship_part2)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()