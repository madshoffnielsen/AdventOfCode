def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def part1(strings):
    code_length = 0
    memory_length = 0
    
    for s in strings:
        code_length += len(s)
        memory_length += len(eval(s))  # Use eval to get the actual string in memory
    
    return code_length - memory_length

def part2(strings):
    code_length = 0
    encoded_length = 0
    
    for s in strings:
        code_length += len(s)
        encoded_length += len(s.replace('\\', '\\\\').replace('"', '\\"')) + 2  # Encode the string
    
    return encoded_length - code_length

def main():
    strings = read_input("2015/Day08/input.txt")
    print(f"Part 1: {part1(strings)}")
    print(f"Part 2: {part2(strings)}")

if __name__ == "__main__":
    main()