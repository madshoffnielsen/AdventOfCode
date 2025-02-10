def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def execute_instructions(instructions, registers):
    pc = 0
    while pc < len(instructions):
        parts = instructions[pc].split()
        cmd = parts[0]
        
        if cmd == 'hlf':
            reg = parts[1]
            registers[reg] //= 2
            pc += 1
        elif cmd == 'tpl':
            reg = parts[1]
            registers[reg] *= 3
            pc += 1
        elif cmd == 'inc':
            reg = parts[1]
            registers[reg] += 1
            pc += 1
        elif cmd == 'jmp':
            offset = int(parts[1])
            pc += offset
        elif cmd == 'jie':
            reg = parts[1].rstrip(',')
            offset = int(parts[2])
            if registers[reg] % 2 == 0:
                pc += offset
            else:
                pc += 1
        elif cmd == 'jio':
            reg = parts[1].rstrip(',')
            offset = int(parts[2])
            if registers[reg] == 1:
                pc += offset
            else:
                pc += 1
    return registers

def part1(instructions):
    registers = {'a': 0, 'b': 0}
    registers = execute_instructions(instructions, registers)
    return registers['b']

def part2(instructions):
    registers = {'a': 1, 'b': 0}
    registers = execute_instructions(instructions, registers)
    return registers['b']

def main():
    instructions = read_input("2015/Day23/input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

if __name__ == "__main__":
    main()