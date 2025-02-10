def read_input(file_path):
    with open(file_path) as f:
        return [(line.split()[0], int(line.split()[1])) for line in f]

def run_program(instructions):
    acc = 0
    pc = 0
    seen = set()
    
    while pc < len(instructions):
        if pc in seen:
            return acc, False
        seen.add(pc)
        
        op, arg = instructions[pc]
        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        else:  # nop
            pc += 1
            
    return acc, True

def part1(instructions):
    acc, _ = run_program(instructions)
    return acc

def part2(instructions):
    for i in range(len(instructions)):
        if instructions[i][0] == 'acc':
            continue
            
        # Create modified copy of instructions
        modified = instructions.copy()
        op = 'nop' if instructions[i][0] == 'jmp' else 'jmp'
        modified[i] = (op, instructions[i][1])
        
        acc, terminated = run_program(modified)
        if terminated:
            return acc
    
    return None

def main():
    instructions = read_input("2020/Day08/input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

if __name__ == "__main__":
    main()