def get_value(program, parameter, mode, relative_base):
    if mode == 0:
        return program.get(parameter, 0)
    elif mode == 1:
        return parameter
    elif mode == 2:
        return program.get(relative_base + parameter, 0)
    else:
        raise ValueError(f"Unknown parameter mode: {mode}")

def set_value(program, parameter, mode, relative_base, value):
    if mode == 0:
        program[parameter] = value
    elif mode == 2:
        program[relative_base + parameter] = value
    else:
        raise ValueError(f"Unknown parameter mode: {mode}")

def run_intcode_program(program, inputs):
    pc = 0  # Program counter
    relative_base = 0
    input_index = 0
    output = []
    program = {i: program[i] for i in range(len(program))}  # Convert to dict for sparse memory

    while program[pc] != 99:
        instruction = str(program[pc]).zfill(5)
        opcode = int(instruction[-2:])
        mode1 = int(instruction[-3])
        mode2 = int(instruction[-4])
        mode3 = int(instruction[-5])

        if opcode in (1, 2, 7, 8):
            param1 = program.get(pc + 1, 0)
            param2 = program.get(pc + 2, 0)
            param3 = program.get(pc + 3, 0)
            value1 = get_value(program, param1, mode1, relative_base)
            value2 = get_value(program, param2, mode2, relative_base)
            if opcode == 1:
                set_value(program, param3, mode3, relative_base, value1 + value2)
            elif opcode == 2:
                set_value(program, param3, mode3, relative_base, value1 * value2)
            elif opcode == 7:
                set_value(program, param3, mode3, relative_base, 1 if value1 < value2 else 0)
            elif opcode == 8:
                set_value(program, param3, mode3, relative_base, 1 if value1 == value2 else 0)
            pc += 4
        elif opcode in (5, 6):
            param1 = program.get(pc + 1, 0)
            param2 = program.get(pc + 2, 0)
            value1 = get_value(program, param1, mode1, relative_base)
            value2 = get_value(program, param2, mode2, relative_base)
            if opcode == 5 and value1 != 0:
                pc = value2
            elif opcode == 6 and value1 == 0:
                pc = value2
            else:
                pc += 3
        elif opcode == 3:
            param1 = program.get(pc + 1, 0)
            set_value(program, param1, mode1, relative_base, inputs[input_index])
            input_index += 1
            pc += 2
        elif opcode == 4:
            param1 = program.get(pc + 1, 0)
            output.append(get_value(program, param1, mode1, relative_base))
            pc += 2
        elif opcode == 9:
            param1 = program.get(pc + 1, 0)
            relative_base += get_value(program, param1, mode1, relative_base)
            pc += 2
        else:
            raise ValueError(f"Unknown opcode {opcode} at position {pc}")
    return output

# Read input from input.txt
with open('2019/Day09/input.txt', 'r') as file:
    input_data = file.read().strip()

# Convert input data to a list of integers
program = list(map(int, input_data.split(',')))

# Part 1: Run the program with input value 1
output_part1 = run_intcode_program(program[:], [1])
print("Output for Part 1:", output_part1)

# Part 2: Run the program with input value 2
output_part2 = run_intcode_program(program[:], [2])
print("Output for Part 2:", output_part2)