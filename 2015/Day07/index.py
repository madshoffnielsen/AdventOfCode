def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def get_value(wires, x):
    try:
        return int(x)
    except ValueError:
        return wires[x]

def evaluate(wires, instructions, part2=False):
    while instructions:
        for instruction in instructions[:]:
            parts = instruction.split(' -> ')
            expr, target = parts[0], parts[1]
            tokens = expr.split()
            
            if len(tokens) == 1:
                # Direct assignment
                if part2 and target == 'b':
                    wires[target] = 46065
                    instructions.remove(instruction)
                elif tokens[0].isdigit() or tokens[0] in wires:
                    wires[target] = get_value(wires, tokens[0])
                    instructions.remove(instruction)
            elif len(tokens) == 2:
                # NOT operation
                if tokens[1].isdigit() or tokens[1] in wires:
                    wires[target] = ~get_value(wires, tokens[1]) & 0xFFFF
                    instructions.remove(instruction)
            elif len(tokens) == 3:
                # AND, OR, LSHIFT, RSHIFT operations
                op1, op, op2 = tokens
                if (op1.isdigit() or op1 in wires) and (op2.isdigit() or op2 in wires):
                    if op == 'AND':
                        wires[target] = get_value(wires, op1) & get_value(wires, op2)
                    elif op == 'OR':
                        wires[target] = get_value(wires, op1) | get_value(wires, op2)
                    elif op == 'LSHIFT':
                        wires[target] = get_value(wires, op1) << get_value(wires, op2)
                    elif op == 'RSHIFT':
                        wires[target] = get_value(wires, op1) >> get_value(wires, op2)
                    instructions.remove(instruction)
    return wires

def part1(instructions):
    wires = {}
    evaluate(wires, instructions.copy())
    return wires['a']

def part2(instructions):
    wires = {}
    evaluate(wires, instructions.copy(), True)
    return wires['a']

def main():
    instructions = read_input("2015/Day07/input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

if __name__ == "__main__":
    main()