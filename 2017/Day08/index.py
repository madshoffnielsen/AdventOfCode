from collections import defaultdict

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

def evaluate_condition(registers, reg, op, val):
    operations = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y
    }
    return operations[op](registers[reg], int(val))

def process_instructions(instructions):
    registers = defaultdict(int)
    highest_ever = 0
    
    for reg, cmd, val, _, cond_reg, cond_op, cond_val in instructions:
        if evaluate_condition(registers, cond_reg, cond_op, cond_val):
            if cmd == 'inc':
                registers[reg] += int(val)
            else:  # dec
                registers[reg] -= int(val)
            highest_ever = max(highest_ever, registers[reg])
    
    return max(registers.values()), highest_ever

def main():
    instructions = read_input("2017/Day08/input.txt")
    final_max, highest_ever = process_instructions(instructions)
    print(f"Part 1: {final_max}")
    print(f"Part 2: {highest_ever}")

if __name__ == "__main__":
    main()