from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def parse_input(lines):
    insp = defaultdict(int)
    insp_2 = defaultdict(int)
    items = defaultdict(list)
    items_2 = defaultdict(list)
    op = {}
    op_value = {}
    test = {}
    true = {}
    false = {}
    global_modulus = 1

    current_monkey = None

    for line in lines:
        args = line.split()

        if len(args) == 0:
            continue

        if args[0] == 'Monkey':
            current_monkey = int(args[1].replace(':', ''))
            insp[current_monkey] = 0
            insp_2[current_monkey] = 0
        elif args[0] == 'Starting':
            values = line.split(': ')[1]
            its = map(int, values.split(', '))
            items[current_monkey].extend(its)
            its = map(int, values.split(', '))
            items_2[current_monkey].extend(its)
        elif args[0] == 'Operation:':
            op[current_monkey] = args[4]
            op_value[current_monkey] = args[5]
        elif args[0] == 'Test:':
            test[current_monkey] = int(args[3])
            global_modulus *= test[current_monkey]
        elif args[1] == 'true:':
            true[current_monkey] = int(args[5])
        elif args[1] == 'false:':
            false[current_monkey] = int(args[5])

    return insp, insp_2, items, items_2, op, op_value, test, true, false, global_modulus

def process_rounds(insp, items, op, op_value, test, true, false, rounds, divide_by=3):
    for _ in range(rounds):
        for key in insp.keys():
            while items[key]:
                item = items[key].pop(0)
                insp[key] += 1

                worry_level = item

                if op_value[key] == 'old':
                    if op[key] == '*':
                        worry_level *= item
                    else:
                        worry_level += item
                else:
                    if op[key] == '*':
                        worry_level *= int(op_value[key])
                    else:
                        worry_level += int(op_value[key])

                worry_level //= divide_by

                if worry_level % test[key] == 0:
                    items[true[key]].append(worry_level)
                else:
                    items[false[key]].append(worry_level)

def process_part2(insp_2, items_2, op, op_value, test, true, false, rounds, global_modulus):
    for round_num in range(rounds):
        for key in insp_2.keys():
            while items_2[key]:
                item = items_2[key].pop(0)
                insp_2[key] += 1

                item %= global_modulus

                if op_value[key] == 'old':
                    if op[key] == '*':
                        item *= item
                    else:
                        item += item
                else:
                    if op[key] == '*':
                        item *= int(op_value[key])
                    else:
                        item += int(op_value[key])

                item %= global_modulus

                if item % test[key] == 0:
                    items_2[true[key]].append(item)
                else:
                    items_2[false[key]].append(item)

def main():
    print("\n--- Day 11: Monkey in the Middle ---")
    lines = read_input('2022/input/day11.txt')

    (insp, insp_2, items, items_2, op, op_value, test, true, false, global_modulus) = parse_input(lines)

    # Part 1
    process_rounds(insp, items, op, op_value, test, true, false, 20)
    part1 = insp.pop(max(insp, key=insp.get)) * insp.pop(max(insp, key=insp.get))
    print(f"Part 1: {part1}")
    
    # Part 2
    process_part2(insp_2, items_2, op, op_value, test, true, false, 10000, global_modulus)
    part2 = insp_2.pop(max(insp_2, key=insp_2.get)) * insp_2.pop(max(insp_2, key=insp_2.get))
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()