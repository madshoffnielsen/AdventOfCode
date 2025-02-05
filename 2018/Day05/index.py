def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def react(polymer):
    stack = []
    for unit in polymer:
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)

def part1(polymer):
    return react(polymer)

def part2(polymer):
    units = set(polymer.lower())
    shortest_length = min(react(polymer.replace(unit, '').replace(unit.upper(), '')) for unit in units)
    return shortest_length

if __name__ == "__main__":
    input_file = "2018/Day05/input.txt"
    polymer = read_input(input_file)
    
    result_part1 = part1(polymer)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(polymer)
    print(f"Part 2: {result_part2}")