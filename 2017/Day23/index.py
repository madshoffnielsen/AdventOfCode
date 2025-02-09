from collections import defaultdict
import math

def execute_part_one(instructions):
    registers = defaultdict(int)
    mul_count = 0
    pointer = 0
    
    while 0 <= pointer < len(instructions):
        parts = instructions[pointer].split()
        instr, X, Y = parts[0], parts[1], parts[2] if len(parts) > 2 else None
        
        Y_val = int(Y) if Y and Y.lstrip('-').isdigit() else registers[Y]
        
        if instr == "set":
            registers[X] = Y_val
        elif instr == "sub":
            registers[X] -= Y_val
        elif instr == "mul":
            registers[X] *= Y_val
            mul_count += 1
        elif instr == "jnz":
            X_val = int(X) if X.lstrip('-').isdigit() else registers[X]
            if X_val != 0:
                pointer += Y_val - 1
        
        pointer += 1
    
    return mul_count

def execute_part_two():
    b = 109300
    c = 126300
    h = 0
    
    for num in range(b, c + 1, 17):
        if not is_prime(num):
            h += 1
    
    return h

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def read_instructions(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == "__main__":
    instructions = read_instructions("2017/Day23/input.txt")
    
    result_part_one = execute_part_one(instructions)
    print("Part 1:", result_part_one)
    
    result_part_two = execute_part_two()
    print("Part 2:", result_part_two)
