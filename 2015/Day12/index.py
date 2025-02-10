import json

def read_input(file_path):
    with open(file_path) as f:
        return json.load(f)

def sum_numbers(data, ignore_red=False):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item, ignore_red) for item in data)
    elif isinstance(data, dict):
        if ignore_red and "red" in data.values():
            return 0
        return sum(sum_numbers(value, ignore_red) for value in data.values())
    return 0

def part1(data):
    return sum_numbers(data)

def part2(data):
    return sum_numbers(data, ignore_red=True)

def main():
    data = read_input("2015/Day12/input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

if __name__ == "__main__":
    main()