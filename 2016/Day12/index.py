from collections import defaultdict

def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

def solve(instructions, initial_state=None):
    registers = defaultdict(int)
    if initial_state:
        registers.update(initial_state)
    
    ip = 0
    while 0 <= ip < len(instructions):
        instr = instructions[ip]
        op = instr[0]
        
        if op == 'cpy':
            x, y = instr[1], instr[2]
            try:
                registers[y] = int(x)
            except ValueError:
                registers[y] = registers[x]
        elif op == 'inc':
            x = instr[1]
            registers[x] += 1
        elif op == 'dec':
            x = instr[1]
            registers[x] -= 1
        elif op == 'jnz':
            x, y = instr[1], instr[2]
            val = registers[x] if x.isalpha() else int(x)
            if val != 0:
                ip += int(y)
                continue
        ip += 1
    return registers['a']

def part1(instructions):
    return solve(instructions)

def part2(instructions):
    return solve(instructions, {'c': 1})

if __name__ == "__main__":
    instructions = parse_input("2016/Day12/input.txt")
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))