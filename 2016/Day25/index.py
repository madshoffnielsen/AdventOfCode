def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

def get_value(registers, x):
    try:
        return int(x)
    except ValueError:
        return registers[x]

def execute_instructions(instructions, registers):
    pc = 0
    output = []
    
    while pc < len(instructions):
        inst = instructions[pc]
        cmd = inst[0]
        
        if cmd == 'cpy':
            x, y = inst[1], inst[2]
            if y in registers:
                registers[y] = get_value(registers, x)
        elif cmd == 'inc':
            x = inst[1]
            if x in registers:
                registers[x] += 1
        elif cmd == 'dec':
            x = inst[1]
            if x in registers:
                registers[x] -= 1
        elif cmd == 'jnz':
            x, y = inst[1], inst[2]
            if get_value(registers, x) != 0:
                pc += get_value(registers, y) - 1
        elif cmd == 'out':
            x = inst[1]
            output.append(get_value(registers, x))
            if len(output) > 20:  # Check first 20 outputs for pattern
                break
        
        pc += 1
    
    return output

def is_clock_signal(output):
    for i in range(len(output)):
        if output[i] != i % 2:
            return False
    return True

def find_initial_value(instructions):
    a = 0
    while True:
        registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
        output = execute_instructions(instructions, registers)
        if is_clock_signal(output):
            return a
        a += 1

def main():
    instructions = read_input("2016/Day25/input.txt")
    initial_value = find_initial_value(instructions)
    print(f"Part 1: {initial_value}")

if __name__ == "__main__":
    main()