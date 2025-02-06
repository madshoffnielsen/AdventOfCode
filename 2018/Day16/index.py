import re
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        content = f.read().strip().split('\n\n\n\n')
        samples = content[0].strip().split('\n\n')
        test_program = content[1].strip().split('\n')
        
        parsed_samples = []
        for sample in samples:
            before, instruction, after = sample.split('\n')
            before = list(map(int, re.findall(r'\d+', before)))
            instruction = list(map(int, re.findall(r'\d+', instruction)))
            after = list(map(int, re.findall(r'\d+', after)))
            parsed_samples.append((before, instruction, after))
        
        parsed_test_program = [list(map(int, re.findall(r'\d+', line))) for line in test_program]
        
        return parsed_samples, parsed_test_program

def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]

def addi(registers, a, b, c):
    registers[c] = registers[a] + b

def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]

def muli(registers, a, b, c):
    registers[c] = registers[a] * b

def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]

def bani(registers, a, b, c):
    registers[c] = registers[a] & b

def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]

def bori(registers, a, b, c):
    registers[c] = registers[a] | b

def setr(registers, a, b, c):
    registers[c] = registers[a]

def seti(registers, a, b, c):
    registers[c] = a

def gtir(registers, a, b, c):
    registers[c] = 1 if a > registers[b] else 0

def gtri(registers, a, b, c):
    registers[c] = 1 if registers[a] > b else 0

def gtrr(registers, a, b, c):
    registers[c] = 1 if registers[a] > registers[b] else 0

def eqir(registers, a, b, c):
    registers[c] = 1 if a == registers[b] else 0

def eqri(registers, a, b, c):
    registers[c] = 1 if registers[a] == b else 0

def eqrr(registers, a, b, c):
    registers[c] = 1 if registers[a] == registers[b] else 0

operations = {
    'addr': addr, 'addi': addi, 'mulr': mulr, 'muli': muli,
    'banr': banr, 'bani': bani, 'borr': borr, 'bori': bori,
    'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri,
    'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr
}

def behaves_like(before, instruction, after):
    opcode, a, b, c = instruction
    count = 0
    for op_name, op_func in operations.items():
        registers = before[:]
        op_func(registers, a, b, c)
        if registers == after:
            count += 1
    return count

def part1(samples):
    count = 0
    for before, instruction, after in samples:
        if behaves_like(before, instruction, after) >= 3:
            count += 1
    return count

def determine_opcode_mapping(samples):
    possible_mappings = defaultdict(set)
    for before, instruction, after in samples:
        opcode, a, b, c = instruction
        for op_name, op_func in operations.items():
            registers = before[:]
            op_func(registers, a, b, c)
            if registers == after:
                possible_mappings[opcode].add(op_name)
    
    opcode_mapping = {}
    while possible_mappings:
        for opcode, ops in list(possible_mappings.items()):
            if len(ops) == 1:
                op_name = ops.pop()
                opcode_mapping[opcode] = op_name
                del possible_mappings[opcode]
                for other_ops in possible_mappings.values():
                    other_ops.discard(op_name)
    
    return opcode_mapping

def part2(samples, test_program):
    opcode_mapping = determine_opcode_mapping(samples)
    registers = [0, 0, 0, 0]
    for instruction in test_program:
        opcode, a, b, c = instruction
        op_name = opcode_mapping[opcode]
        operations[op_name](registers, a, b, c)
    return registers[0]

if __name__ == "__main__":
    input_file = "2018/Day16/input.txt"
    samples, test_program = read_input(input_file)
    
    result_part1 = part1(samples)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(samples, test_program)
    print(f"Part 2: {result_part2}")