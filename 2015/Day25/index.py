def read_input(file_path):
    with open(file_path) as f:
        line = f.readline().strip()
    parts = line.split()
    row = int(parts[-3].strip(','))
    col = int(parts[-1].strip('.'))
    return row, col

def calculate_code(row, col):
    code = 20151125
    multiplier = 252533
    divisor = 33554393
    
    # Calculate the position in the sequence
    n = (row + col - 2) * (row + col - 1) // 2 + col - 1
    
    for _ in range(n):
        code = (code * multiplier) % divisor
    
    return code

def main():
    row, col = read_input("2015/Day25/input.txt")
    print(f"Part 1: {calculate_code(row, col)}")

if __name__ == "__main__":
    main()