def get_value(program, parameter, mode):
    return parameter if mode == 1 else program[parameter]

def run_intcode_program(program, input_value):
    pc = 0  # Program counter
    output = []
    while program[pc] != 99:
        instruction = str(program[pc]).zfill(5)
        opcode = int(instruction[-2:])
        mode1 = int(instruction[-3])
        mode2 = int(instruction[-4])
        mode3 = int(instruction[-5])  # Not used, but included for completeness

        if opcode in (1, 2, 7, 8):
            param1 = program[pc + 1]
            param2 = program[pc + 2]
            param3 = program[pc + 3]
            value1 = get_value(program, param1, mode1)
            value2 = get_value(program, param2, mode2)
            if opcode == 1:
                program[param3] = value1 + value2
            elif opcode == 2:
                program[param3] = value1 * value2
            elif opcode == 7:
                program[param3] = 1 if value1 < value2 else 0
            elif opcode == 8:
                program[param3] = 1 if value1 == value2 else 0
            pc += 4
        elif opcode in (5, 6):
            param1 = program[pc + 1]
            param2 = program[pc + 2]
            value1 = get_value(program, param1, mode1)
            value2 = get_value(program, param2, mode2)
            if opcode == 5 and value1 != 0:
                pc = value2
            elif opcode == 6 and value1 == 0:
                pc = value2
            else:
                pc += 3
        elif opcode == 3:
            param1 = program[pc + 1]
            program[param1] = input_value
            pc += 2
        elif opcode == 4:
            param1 = program[pc + 1]
            output.append(get_value(program, param1, mode1))
            pc += 2
        else:
            raise ValueError(f"Unknown opcode {opcode} at position {pc}")
    return output

# Read input from input.txt
with open('2019/Day05/input.txt', 'r') as file:
    input_data = file.read().strip()

# Convert input data to a list of integers
program = list(map(int, input_data.split(',')))

# Part 1: Run the program with input value 1
output_part1 = run_intcode_program(program[:], input_value=1)
print("Output for Part 1:", output_part1)

# Part 2: Run the program with input value 5
output_part2 = run_intcode_program(program[:], input_value=5)
print("Output for Part 2:", output_part2)