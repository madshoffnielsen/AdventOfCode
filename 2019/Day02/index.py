def run_intcode_program(program):
    pc = 0  # Program counter
    while program[pc] != 99:
        opcode = program[pc]
        param1 = program[pc + 1]
        param2 = program[pc + 2]
        param3 = program[pc + 3]
        
        if opcode == 1:
            program[param3] = program[param1] + program[param2]
        elif opcode == 2:
            program[param3] = program[param1] * program[param2]
        else:
            raise ValueError(f"Unknown opcode {opcode} at position {pc}")
        
        pc += 4
    return program

def find_noun_and_verb(original_program, target_output):
    for noun in range(100):
        for verb in range(100):
            program = original_program[:]
            program[1] = noun
            program[2] = verb
            output = run_intcode_program(program)[0]
            if output == target_output:
                return 100 * noun + verb
    raise ValueError("No valid noun and verb found")

# Read input from input.txt
with open('2019/Day02/input.txt', 'r') as file:
    input_data = file.read().strip()

# Convert input data to a list of integers
original_program = list(map(int, input_data.split(',')))

# Part 1: Run the program with the initial state
program_part1 = original_program[:]
program_part1[1] = 12
program_part1[2] = 2
output_part1 = run_intcode_program(program_part1)[0]
print("Output for Part 1:", output_part1)

# Part 2: Find the noun and verb that produce the target output
target_output = 19690720
result_part2 = find_noun_and_verb(original_program, target_output)
print("Result for Part 2:", result_part2)