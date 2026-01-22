from typing import List

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.rstrip() for line in f if line.strip()]

def part1(lines: List[str]) -> int:
    fields = [line.split() for line in lines]
    num_problems = len(fields[0])
    total = 0
    for i in range(num_problems):
        op = fields[-1][i]
        nums = []
        for j in range(len(fields) - 1):
            field = fields[j][i]
            if field.strip():
                nums.append(int(field))
        if op == '+':
            result = sum(nums)
        elif op == '*':
            result = 1
            for n in nums:
                result *= n
        total += result
    return total

def part2(lines: List[str]) -> int:
    rows = len(lines)
    cols = max(len(line) for line in lines)
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(len(lines[i])):
            grid[i][j] = lines[i][j]
    # Find problems
    problems = []
    current = []
    for j in range(cols):
        is_sep = all(grid[i][j] == ' ' for i in range(rows))
        if not is_sep:
            current.append(j)
        else:
            if current:
                problems.append(current)
                current = []
    if current:
        problems.append(current)
    total = 0
    for problem in problems:
        start_col = problem[0]
        op = grid[rows - 1][start_col]
        nums = []
        for col in problem:
            num_str = ''
            for r in range(rows - 1):
                if grid[r][col] != ' ':
                    num_str += grid[r][col]
            if num_str:
                nums.append(int(num_str))
        if op == '+':
            result = sum(nums)
        elif op == '*':
            result = 1
            for n in nums:
                result *= n
        total += result
    return total

def main() -> None:
    lines = read_input("2025/Day06/input.txt")
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

if __name__ == "__main__":
    main()