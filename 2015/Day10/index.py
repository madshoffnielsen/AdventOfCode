def look_and_say(sequence):
    result = []
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        result.append(f"{count}{sequence[i]}")
        i += 1
    return ''.join(result)

def part1(sequence):
    for _ in range(40):
        sequence = look_and_say(sequence)
    return len(sequence)

def part2(sequence):
    for _ in range(50):
        sequence = look_and_say(sequence)
    return len(sequence)

def main():
    input_sequence = "3113322113"
    print(f"Part 1: {part1(input_sequence)}")
    print(f"Part 2: {part2(input_sequence)}")

if __name__ == "__main__":
    main()