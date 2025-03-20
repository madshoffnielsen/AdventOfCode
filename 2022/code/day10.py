def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def process_instructions(lines):
    cycles_check = [20, 60, 100, 140, 180, 220]
    total_score = 0

    crt = []
    cycle = 0
    crt_count = 0
    x = 1

    for line in lines:
        args = line.split()

        # Update CRT based on the current position
        if x - 1 == crt_count or x == crt_count or x + 1 == crt_count:
            crt.append('#')
        else:
            crt.append(' ')

        cycle += 1
        crt_count += 1

        # Reset CRT count after 40 cycles
        if crt_count == 40:
            crt_count = 0

        # Handle "noop" and other instructions
        if args[0] == 'noop':
            if cycle in cycles_check:
                total_score += (x * cycle)
        else:
            if cycle in cycles_check:
                total_score += (x * cycle)

            # Update CRT for the second cycle of the instruction
            if x - 1 == crt_count or x == crt_count or x + 1 == crt_count:
                crt.append('#')
            else:
                crt.append(' ')

            cycle += 1
            crt_count += 1

            # Reset CRT count after 40 cycles
            if crt_count == 40:
                crt_count = 0

            if cycle in cycles_check:
                total_score += (x * cycle)

            # Update the value of x
            x += int(args[1])

    return total_score, crt

def main():
    print("\n--- Day 10: Cathode-Ray Tube ---")
    lines = read_input('2022/input/day10.txt')
    total_score, crt = process_instructions(lines)

    print(f"Part 1: {total_score}")

    # Print CRT output in chunks of 40 characters
    for i in range(0, len(crt), 40):
        print(''.join(crt[i:i+40]))

if __name__ == "__main__":
    main()