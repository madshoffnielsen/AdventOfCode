from typing import List, Tuple, Set

Instruction = Tuple[str, int]
Program = List[Instruction]

def read_input(file_path: str) -> Program:
    """Read and parse input file into list of instructions."""
    with open(file_path) as f:
        return [(line.split()[0], int(line.split()[1])) 
                for line in f.read().splitlines()]

def run_program(instructions: Program) -> Tuple[int, bool]:
    """Execute program and track accumulator value."""
    acc: int = 0
    pc: int = 0
    seen: Set[int] = set()
    
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

def part1(instructions: Program) -> int:
    """Find accumulator value before loop."""
    acc, _ = run_program(instructions)
    return acc

def part2(instructions: Program) -> int:
    """Find accumulator value after fixing the program."""
    for i in range(len(instructions)):
        if instructions[i][0] == 'acc':
            continue
            
        modified = instructions.copy()
        op = 'nop' if instructions[i][0] == 'jmp' else 'jmp'
        modified[i] = (op, instructions[i][1])
        
        acc, terminated = run_program(modified)
        if terminated:
            return acc
    
    return 0

def main():
    """Main program."""
    print("\n--- Day 8: Handheld Halting ---")
    
    instructions = read_input("2020/input/day08.txt")
    
    result1 = part1(instructions)
    print(f"Part 1: {result1}")
    
    result2 = part2(instructions)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()