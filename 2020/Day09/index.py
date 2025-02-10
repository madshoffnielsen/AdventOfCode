def read_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def is_valid(number, preamble):
    for i in range(len(preamble)):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False

def find_invalid_number(numbers, preamble_size=25):
    for i in range(preamble_size, len(numbers)):
        preamble = numbers[i - preamble_size:i]
        if not is_valid(numbers[i], preamble):
            return numbers[i]
    return None

def find_contiguous_set(numbers, target):
    for i in range(len(numbers)):
        sum_so_far = 0
        for j in range(i, len(numbers)):
            sum_so_far += numbers[j]
            if sum_so_far == target:
                contiguous_set = numbers[i:j + 1]
                return min(contiguous_set) + max(contiguous_set)
            if sum_so_far > target:
                break
    return None

def part1(numbers):
    return find_invalid_number(numbers)

def part2(numbers):
    invalid_number = find_invalid_number(numbers)
    return find_contiguous_set(numbers, invalid_number)

def main():
    numbers = read_input("2020/Day09/input.txt")
    print(f"Part 1: {part1(numbers)}")
    print(f"Part 2: {part2(numbers)}")

if __name__ == "__main__":
    main()