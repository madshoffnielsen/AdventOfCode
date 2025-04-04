from itertools import product

def read_input(file_path):
    """Read and return the word search grid."""
    list = []
    with open(file_path, 'r') as f:
        for line in f:
            list.append(line.strip())
    return list

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_form_target(test_value, numbers):
    num_positions = len(numbers) - 1
    for ops in product(['+', '*'], repeat=num_positions):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def can_form_target_part_2(test_value, numbers):
    num_positions = len(numbers) - 1
    for ops in product(['+', '*', '||'], repeat=num_positions):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def sum_valid_expressions(equations, part2 = False):
    total_sum = 0
    for line in equations:
        parts = line.split(': ')
        test_value = int(parts[0])
        numbers = list(map(int, parts[1].split()))
        if part2:
            if can_form_target_part_2(test_value, numbers):
                total_sum += test_value
        elif can_form_target(test_value, numbers):
            total_sum += test_value
    return total_sum

def main():
    print("\n--- Day 7: Bridge Repair ---")
    
    list = read_input("2024/Day07/input.txt")
    
    result1 = sum_valid_expressions(list)
    print(f"Part 1: {result1}")

    result2 = sum_valid_expressions(list, True)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()