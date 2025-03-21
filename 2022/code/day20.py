def read_input(file_path):
    """Reads and parses the input file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return [int(x.strip()) for x in f.readlines()]

def decrypt(arrangement, key=1, num_mix=1):
    """Decrypts the arrangement based on the given key and number of mixes."""
    zero_index = 0
    mixer = [(itx, a * key) for (itx, a) in enumerate(arrangement)]

    for _ in range(num_mix):
        for i in range(len(arrangement)):
            for j in range(len(arrangement)):
                if mixer[j][0] == i:
                    curr = mixer.pop(j)
                    new_index = (j + curr[1]) % len(mixer)
                    mixer.insert(new_index, (i, curr[1]))
                    break

    for (itx, (_, val)) in enumerate(mixer):
        if val == 0:
            zero_index = itx
            break

    return (
        mixer[(zero_index + 1000) % len(mixer)][1]
        + mixer[(zero_index + 2000) % len(mixer)][1]
        + mixer[(zero_index + 3000) % len(mixer)][1]
    )

def part1(arrangement):
    """Solves Part 1 of the problem."""
    return decrypt(arrangement)

def part2(arrangement):
    """Solves Part 2 of the problem."""
    return decrypt(arrangement, key=811589153, num_mix=10)

def main():
    print("\n--- Day 20: Grove Positioning System ---")
    file_path = "2022/input/day20.txt"
    arrangement = read_input(file_path)

    # Part 1
    result1 = part1(arrangement)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(arrangement)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()