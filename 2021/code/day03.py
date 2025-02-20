def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def calculate_power_consumption(binary_numbers):
    bit_length = len(binary_numbers[0])
    bit_counts = [0] * bit_length

    # Count the number of 1s in each bit position
    for number in binary_numbers:
        for i in range(bit_length):
            if number[i] == '1':
                bit_counts[i] += 1

    gamma_rate = ''
    epsilon_rate = ''
    total_numbers = len(binary_numbers)

    # Calculate gamma and epsilon rates
    for count in bit_counts:
        if count > total_numbers / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_rate_decimal = int(gamma_rate, 2)
    epsilon_rate_decimal = int(epsilon_rate, 2)

    # Calculate and return the power consumption
    return gamma_rate_decimal * epsilon_rate_decimal

def find_rating(numbers, criteria):
    bit_length = len(numbers[0])

    for i in range(bit_length):
        count0 = count1 = 0
        for number in numbers:
            if number[i] == '0':
                count0 += 1
            else:
                count1 += 1

        if criteria == 'oxygen':
            keep_bit = '1' if count1 >= count0 else '0'
        else:
            keep_bit = '0' if count0 <= count1 else '1'

        numbers = [number for number in numbers if number[i] == keep_bit]

        if len(numbers) == 1:
            break

    return numbers[0]

def calculate_life_support_rating(binary_numbers):
    oxygen_rating_binary = find_rating(binary_numbers, 'oxygen')
    oxygen_rating_decimal = int(oxygen_rating_binary, 2)

    co2_rating_binary = find_rating(binary_numbers, 'co2')
    co2_rating_decimal = int(co2_rating_binary, 2)

    return oxygen_rating_decimal * co2_rating_decimal

def main():
    print("\n--- Day 3: Binary Diagnostic ---")
    binary_numbers = read_input('2021/input/day03.txt')

    power_consumption = calculate_power_consumption(binary_numbers)
    print(f"Part 1: {power_consumption}")

    life_support_rating = calculate_life_support_rating(binary_numbers)
    print(f"Part 2: {life_support_rating}")

if __name__ == "__main__":
    main()