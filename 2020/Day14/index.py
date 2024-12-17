import re
from itertools import product

def apply_mask_to_value(mask, value):
    """Apply mask to value (Part 1 logic)."""
    binary_value = list(f"{value:036b}")
    for i, bit in enumerate(mask):
        if bit != "X":
            binary_value[i] = bit
    return int("".join(binary_value), 2)

def apply_mask_to_address(mask, address):
    """Apply mask to address (Part 2 logic)."""
    binary_address = list(f"{address:036b}")
    for i, bit in enumerate(mask):
        if bit == "1":
            binary_address[i] = "1"
        elif bit == "X":
            binary_address[i] = "X"
    return binary_address

def get_all_addresses(floating_address):
    """Generate all possible addresses from a floating binary address."""
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
            mask = line.split(" = ")[1]
        else:
            match = re.match(r"mem\[(\d+)\] = (\d+)", line)
            address, value = int(match[1]), int(match[2])
            if part == 1:
                memory[address] = apply_mask_to_value(mask, value)
            elif part == 2:
                masked_address = apply_mask_to_address(mask, address)
                for final_address in get_all_addresses(masked_address):
                    memory[final_address] = value
    return sum(memory.values())

# Read input from input.txt
with open("2020/Day14/input.txt", "r") as f:
    input_lines = f.read().strip().split("\n")

# Part 1
result_part1 = execute_program(input_lines, part=1)
print(f"Part 1: {result_part1}")

# Part 2
result_part2 = execute_program(input_lines, part=2)
print(f"Part 2: {result_part2}")
