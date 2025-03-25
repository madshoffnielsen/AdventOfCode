import re
from itertools import product
from typing import List, Dict, Iterator

def read_input(file_path: str) -> List[str]:
    """Read program instructions from file."""
    with open(file_path) as f:
        return f.readlines()

def apply_mask_to_value(mask: str, value: int) -> int:
    """Apply bitmask to value."""
    binary_value = list(f"{value:036b}")
    for i, bit in enumerate(mask):
        if bit != "X":
            binary_value[i] = bit
    return int("".join(binary_value), 2)

def apply_mask_to_address(mask: str, address: int) -> List[str]:
    """Apply bitmask to memory address."""
    binary_address = list(f"{address:036b}")
    for i, bit in enumerate(mask):
        if bit == "1":
            binary_address[i] = "1"
        elif bit == "X":
            binary_address[i] = "X"
    return binary_address

def get_all_addresses(floating_address: List[str]) -> Iterator[int]:
    """Generate all possible addresses from floating address."""
    floating_indices = [i for i, bit in enumerate(floating_address) if bit == "X"]
    combinations = product("01", repeat=len(floating_indices))
    for combo in combinations:
        address_copy = floating_address[:]
        for i, bit in zip(floating_indices, combo):
            address_copy[i] = bit
        yield int("".join(address_copy), 2)

def run_program(instructions: List[str], part: int = 1) -> int:
    """Execute initialization program."""
    memory: Dict[int, int] = {}
    mask = ""
    
    for line in instructions:
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

def part1(instructions: List[str]) -> int:
    """Calculate sum of values in memory after version 1 execution."""
    return run_program(instructions, part=1)

def part2(instructions: List[str]) -> int:
    """Calculate sum of values in memory after version 2 execution."""
    return run_program(instructions, part=2)

def main():
    """Main program."""
    print("\n--- Day 14: Docking Data ---")
    
    instructions = read_input("2020/input/day14.txt")
    
    result1 = part1(instructions)
    print(f"Part 1: {result1}")
    
    result2 = part2(instructions)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()