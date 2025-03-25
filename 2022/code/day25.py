def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()

def snafu_to_decimal(snafu):
    value = 0
    power = 1
    for ch in reversed(snafu):
        match ch:
            case '0' | '1' | '2':
                value += int(ch) * power
            case '-':
                value -= power
            case '=':
                value -= 2 * power
        power *= 5
    return value

def decimal_to_snafu(decimal):
    if decimal == 0:
        return "0"
    
    value = ""
    while decimal:
        decimal, remainder = divmod(decimal, 5)
        match remainder:
            case 0 | 1 | 2:
                value = str(remainder) + value
            case 3:
                decimal += 1
                value = "=" + value
            case 4:
                decimal += 1
                value = "-" + value
    return value

def main():
    print("\n--- Day 25: Full of Hot Air ---")
    file_path = "2022/input/day25.txt"
    snafu_numbers = read_input(file_path)

    # Part 1
    result1 = decimal_to_snafu(sum(map(snafu_to_decimal, snafu_numbers)))
    print(f"Part 1: {result1}")

if __name__ == "__main__":
    main()