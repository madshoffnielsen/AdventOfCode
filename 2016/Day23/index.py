def read_instructions(filename):
    with open(filename) as f:
        return [line.strip().split() for line in f]

def get_value(x, registers):
    try:
        return int(x)
    except ValueError:
        return registers[x]

def execute_instructions(instructions, initial_registers):
    registers = initial_registers.copy()
    pc = 0  # Program counter

    while pc < len(instructions):
        instr = instructions[pc]

        # Optimization: Recognizing multiplication pattern
        if pc == 4 and instructions[pc:pc+6] == [
            ['cpy', 'b', 'c'],
            ['inc', 'a'],
            ['dec', 'c'],
            ['jnz', 'c', '-2'],
            ['dec', 'd'],
            ['jnz', 'd', '-5']
        ]:
            # The loop effectively does: a += b * d
            registers['a'] += registers['b'] * registers['d']
            registers['c'] = 0
            registers['d'] = 0
            pc += 6  # Skip the loop
            continue

        if instr[0] == 'cpy':
            x, y = instr[1], instr[2]
            if y in registers:
                registers[y] = get_value(x, registers)
            pc += 1

        elif instr[0] == 'inc':
            x = instr[1]
            if x in registers:
                registers[x] += 1
            pc += 1

        elif instr[0] == 'dec':
            x = instr[1]
            if x in registers:
                registers[x] -= 1
            pc += 1

        elif instr[0] == 'jnz':
            x, y = instr[1], instr[2]
            if get_value(x, registers) != 0:
                pc += get_value(y, registers)
            else:
                pc += 1

        elif instr[0] == 'tgl':
            x = instr[1]
            target = pc + get_value(x, registers)
            if 0 <= target < len(instructions):
                target_instr = instructions[target]
                if len(target_instr) == 2:
                    if target_instr[0] == 'inc':
                        instructions[target][0] = 'dec'
                    else:
                        instructions[target][0] = 'inc'
                elif len(target_instr) == 3:
                    if target_instr[0] == 'jnz':
                        instructions[target][0] = 'cpy'
                    else:
                        instructions[target][0] = 'jnz'
            pc += 1

        else:
            raise ValueError(f"Unknown instruction: {instr[0]}")

    return registers

if __name__ == "__main__":
    instructions = read_instructions("2016/Day23/input.txt")

    # Part 1
    initial_registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    result = execute_instructions(instructions, initial_registers)
    print(f"Part 1: Register 'a' = {result['a']}")

    # Part 2 (Runs very fast now!)
    instructions = read_instructions("2016/Day23/input.txt")
    initial_registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    result = execute_instructions(instructions, initial_registers)
    print(f"Part 2: Register 'a' = {result['a']}")
