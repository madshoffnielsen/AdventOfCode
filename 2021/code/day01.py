def read_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip()]

def count_increases(depths):
    return sum(1 for i in range(1, len(depths)) if depths[i] > depths[i - 1])

def count_sliding_window_increases(depths):
    increases = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            increases += 1
    return increases

def main():
    print("\n--- Day 1: Sonar Sweep ---")
    depths = read_input('2021/input/day01.txt')

    result = count_increases(depths)
    print(f"Part 1: {result}")

    result = count_sliding_window_increases(depths)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()