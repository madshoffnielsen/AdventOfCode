def part1(steps):
    buffer = [0]
    pos = 0
    
    for i in range(1, 2018):
        pos = ((pos + steps) % len(buffer)) + 1
        buffer.insert(pos, i)
    
    return buffer[(pos + 1) % len(buffer)]

def part2(steps):
    pos = 0
    value_after_zero = None
    
    for i in range(1, 50_000_000):
        pos = ((pos + steps) % i) + 1
        if pos == 1:
            value_after_zero = i
    
    return value_after_zero

def main():
    steps = 324
    print(f"Part 1: {part1(steps)}")
    print(f"Part 2: {part2(steps)}")

if __name__ == "__main__":
    main()