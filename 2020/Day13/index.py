def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        timestamp = int(lines[0])
        buses = [(i, int(x)) for i, x in enumerate(lines[1].strip().split(',')) if x != 'x']
        return timestamp, buses

def part1(timestamp, buses):
    earliest = float('inf')
    best_bus = None
    
    for _, bus in buses:
        wait = bus - (timestamp % bus)
        if wait < earliest:
            earliest = wait
            best_bus = bus
            
    return best_bus * earliest

def chinese_remainder(buses):
    N = 1
    for _, n in buses:
        N *= n
        
    total = 0
    for i, n in buses:
        a = -i  # We want bus to depart i minutes after timestamp
        y = N // n
        z = pow(y, -1, n)  # Modular multiplicative inverse
        total += a * y * z
        
    return total % N

def part2(buses):
    return chinese_remainder(buses)

def main():
    timestamp, buses = read_input("2020/Day13/input.txt")
    print(f"Part 1: {part1(timestamp, buses)}")
    print(f"Part 2: {part2(buses)}")

if __name__ == "__main__":
    main()