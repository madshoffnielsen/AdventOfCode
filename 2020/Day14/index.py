import re
from itertools import product

def read_input(file_path):
    with open(file_path) as f:
        return f.readlines()

def apply_mask_to_value(mask, value):
    binary_value = list(f"{value:036b}")
    for i, bit in enumerate(mask):
        if bit != "X":
            binary_value[i] = bit
    return int("".join(binary_value), 2)

def apply_mask_to_address(mask, address):
    binary_address = list(f"{address:036b}")
    for i, bit in enumerate(mask):
        if bit == "1":
            binary_address[i] = "1"
        elif bit == "X":
            binary_address[i] = "X"
    return binary_address

def get_all_addresses(floating_address):
    floating_indices = [i for i, bit in enumerate(floating_address) if bit == "X"]
    combinations = product("01", repeat=len(floating_indices))
    for combo in combinations:
        address_copy = floating_address[:]
        for i, bit in zip(floating_indices, combo):
            address_copy[i] = bit
        yield int("".join(address_copy), 2)

def execute_program(input_lines, part=1):
    memory = {}
    mask = None
    for line in input_lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1].strip()
        else:
            match = re.match(r"mem\[(\d+)\] = (\d+)", line)
            address, value = map(int, match.groups())
            
            if part == 1:
                memory[address] = apply_mask_to_value(mask, value)
            else:
                floating_address = apply_mask_to_address(mask, address)
                for addr in get_all_addresses(floating_address):
                    memory[addr] = value
    
    return sum(memory.values())

def main():
    input_lines = read_input("2020/Day14/input.txt")
    print(f"Part 1: {execute_program(input_lines, part=1)}")
    print(f"Part 2: {execute_program(input_lines, part=2)}")

if __name__ == "__main__":
    main()