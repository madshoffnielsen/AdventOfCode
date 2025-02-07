def read_input(file_path):
    with open(file_path) as f:
        return [[int(n) for n in line.strip().split()] for line in f]

def part1(spreadsheet):
    total = 0
    for row in spreadsheet:
        total += max(row) - min(row)
    return total

def part2(spreadsheet):
    total = 0
    for row in spreadsheet:
        for i, n1 in enumerate(row):
            for n2 in row[i+1:]:
                if n1 % n2 == 0:
                    total += n1 // n2
                elif n2 % n1 == 0:
                    total += n2 // n1
    return total

def main():
    spreadsheet = read_input("2017/Day02/input.txt")
    print(f"Part 1: {part1(spreadsheet)}")
    print(f"Part 2: {part2(spreadsheet)}")

if __name__ == "__main__":
    main()