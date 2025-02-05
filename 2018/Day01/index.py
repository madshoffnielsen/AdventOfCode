def read_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def part1(frequencies):
    return sum(frequencies)

def part2(frequencies):
    seen = set()
    current_frequency = 0
    index = 0
    while current_frequency not in seen:
        seen.add(current_frequency)
        current_frequency += frequencies[index]
        index = (index + 1) % len(frequencies)
    return current_frequency

if __name__ == "__main__":
    input_file = "2018/Day01/input.txt"
    frequencies = read_input(input_file)
    
    result_part1 = part1(frequencies)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(frequencies)
    print(f"Part 2: {result_part2}")