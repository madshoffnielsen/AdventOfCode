import re
from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def process_instructions(instructions):
    bots = defaultdict(list)
    outputs = defaultdict(list)
    bot_instructions = {}
    value_pattern = re.compile(r'value (\d+) goes to bot (\d+)')
    bot_pattern = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')

    for instruction in instructions:
        if instruction.startswith('value'):
            value, bot = map(int, value_pattern.match(instruction).groups())
            bots[bot].append(value)
        else:
            bot, low_type, low_id, high_type, high_id = bot_pattern.match(instruction).groups()
            bot_instructions[int(bot)] = (low_type, int(low_id), high_type, int(high_id))

    return bots, outputs, bot_instructions

def execute_instructions(bots, outputs, bot_instructions):
    queue = deque(bot for bot, values in bots.items() if len(values) == 2)
    responsible_bot = None

    while queue:
        bot = queue.popleft()
        low, high = sorted(bots[bot])
        if low == 17 and high == 61:
            responsible_bot = bot

        low_type, low_id, high_type, high_id = bot_instructions[bot]
        if low_type == 'bot':
            bots[low_id].append(low)
            if len(bots[low_id]) == 2:
                queue.append(low_id)
        else:
            outputs[low_id].append(low)

        if high_type == 'bot':
            bots[high_id].append(high)
            if len(bots[high_id]) == 2:
                queue.append(high_id)
        else:
            outputs[high_id].append(high)

        bots[bot] = []

    return responsible_bot, outputs

def part1(instructions):
    bots, outputs, bot_instructions = process_instructions(instructions)
    responsible_bot, _ = execute_instructions(bots, outputs, bot_instructions)
    return responsible_bot

def part2(instructions):
    bots, outputs, bot_instructions = process_instructions(instructions)
    _, outputs = execute_instructions(bots, outputs, bot_instructions)
    return outputs[0][0] * outputs[1][0] * outputs[2][0]

if __name__ == "__main__":
    instructions = parse_input("2016/Day10/input.txt")
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))