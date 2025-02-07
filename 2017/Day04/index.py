def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

def is_valid_part1(passphrase):
    return len(passphrase) == len(set(passphrase))

def is_valid_part2(passphrase):
    sorted_words = [''.join(sorted(word)) for word in passphrase]
    return len(sorted_words) == len(set(sorted_words))

def part1(passphrases):
    return sum(1 for phrase in passphrases if is_valid_part1(phrase))

def part2(passphrases):
    return sum(1 for phrase in passphrases if is_valid_part2(phrase))

def main():
    passphrases = read_input("2017/Day04/input.txt")
    print(f"Part 1: {part1(passphrases)}")
    print(f"Part 2: {part2(passphrases)}")

if __name__ == "__main__":
    main()