def read_input(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value

def find_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value = (value * 7) % 20201227
        loop_size += 1
    return loop_size

def part1(card_public_key, door_public_key):
    card_loop_size = find_loop_size(card_public_key)
    encryption_key = transform(door_public_key, card_loop_size)
    return encryption_key

def main():
    card_public_key, door_public_key = read_input("2020/Day25/input.txt")
    print(f"Part 1: {part1(card_public_key, door_public_key)}")
    print("Part 2: Completed all days!")

if __name__ == "__main__":
    main()