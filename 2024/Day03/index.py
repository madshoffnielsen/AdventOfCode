import re

def sum_multiplications(file_path: str, part: int) -> int:
    # Regular expressions
    pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    
    total = 0
    enabled = True  # Multiplications start enabled (Part 2 only)
    
    # Read input from file
    with open(file_path, 'r') as file:
        memory = file.read()
    
    # Process the memory in order
    index = 0
    while index < len(memory):
        do_match = do_pattern.match(memory, index)
        dont_match = dont_pattern.match(memory, index)
        mul_match = pattern.match(memory, index)
        
        if part == 2:
            if do_match:
                enabled = True
                index += len(do_match.group())
                continue
            elif dont_match:
                enabled = False
                index += len(dont_match.group())
                continue
        
        if mul_match:
            if part == 1 or (part == 2 and enabled):
                x, y = map(int, mul_match.groups())
                total += x * y
            index += len(mul_match.group())
        else:
            index += 1  # Move to the next character if no match found
    
    return total

# Example usage
input_file = "2024/Day03/input.txt"
print("Part 1:", sum_multiplications(input_file, part=1))
print("Part 2:", sum_multiplications(input_file, part=2))
