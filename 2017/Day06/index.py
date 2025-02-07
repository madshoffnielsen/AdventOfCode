def read_input(file_path):
    with open(file_path) as f:
        return [int(x) for x in f.read().strip().split()]

def redistribute(banks):
    # Find bank with most blocks
    max_blocks = max(banks)
    bank_index = banks.index(max_blocks)
    
    # Empty the bank
    banks[bank_index] = 0
    
    # Redistribute blocks
    while max_blocks > 0:
        bank_index = (bank_index + 1) % len(banks)
        banks[bank_index] += 1
        max_blocks -= 1
    
    return banks

def solve(banks):
    seen = {}
    steps = 0
    banks = banks.copy()
    
    while tuple(banks) not in seen:
        seen[tuple(banks)] = steps
        banks = redistribute(banks.copy())
        steps += 1
    
    loop_size = steps - seen[tuple(banks)]
    return steps, loop_size

def main():
    banks = read_input("2017/Day06/input.txt")
    part1, part2 = solve(banks)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()