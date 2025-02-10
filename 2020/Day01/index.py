def read_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def find_two_numbers(numbers):
    seen = set()
    for num in numbers:
        if 2020 - num in seen:
            return num * (2020 - num)
        seen.add(num)
    return None

def find_three_numbers(numbers):
    numbers.sort()
    for i, num in enumerate(numbers):
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            current_sum = num + numbers[left] + numbers[right]
            if current_sum == 2020:
                return num * numbers[left] * numbers[right]
            elif current_sum < 2020:
                left += 1
            else:
                right -= 1
    return None

def main():
    numbers = read_input("2020/Day01/input.txt")
    print(f"Part 1: {find_two_numbers(numbers)}")
    print(f"Part 2: {find_three_numbers(numbers)}")

if __name__ == "__main__":
    main()