def read_input(file_path):
    with open(file_path) as f:
        return [pattern.split('\n') for pattern in f.read().strip().split('\n\n')]

def find_reflection(pattern, smudges=0):
    for i in range(1, len(pattern)):
        differences = 0
        for j in range(min(i, len(pattern) - i)):
            differences += sum(a != b for a, b in zip(pattern[i-j-1], pattern[i+j]))
            if differences > smudges:
                break
        if differences == smudges:
            return i
    return 0

def get_columns(pattern):
    return [''.join(col) for col in zip(*pattern)]

def solve_pattern(pattern, smudges=0):
    # Check horizontal reflection
    horizontal = find_reflection(pattern, smudges)
    if horizontal:
        return horizontal * 100
    
    # Check vertical reflection
    vertical = find_reflection(get_columns(pattern), smudges)
    return vertical

def part1(patterns):
    return sum(solve_pattern(pattern) for pattern in patterns)

def part2(patterns):
    return sum(solve_pattern(pattern, 1) for pattern in patterns)

def main():
    patterns = read_input("2023/Day13/input.txt")
    print(f"Part 1: {part1(patterns)}")
    print(f"Part 2: {part2(patterns)}")

if __name__ == "__main__":
    main()