def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def find_digits_part1(line):
    digits = [c for c in line if c.isdigit()]
    return int(digits[0] + digits[-1])

def find_digits_part2(line):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        else:
            for word, digit in number_map.items():
                if line[i:].startswith(word):
                    digits.append(digit)
                    
    return int(digits[0] + digits[-1])

def part1(lines):
    return sum(find_digits_part1(line) for line in lines)

def part2(lines):
    return sum(find_digits_part2(line) for line in lines)

def main():
    lines = read_input("2023/Day01/input.txt")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()