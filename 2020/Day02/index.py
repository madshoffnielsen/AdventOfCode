def read_input(file_path):
    passwords = []
    with open(file_path) as f:
        for line in f:
            policy, letter, password = line.strip().split()
            min_count, max_count = map(int, policy.split('-'))
            letter = letter[0]  # Remove colon
            passwords.append((min_count, max_count, letter, password))
    return passwords

def is_valid_part1(min_count, max_count, letter, password):
    count = password.count(letter)
    return min_count <= count <= max_count

def is_valid_part2(pos1, pos2, letter, password):
    return (password[pos1-1] == letter) != (password[pos2-1] == letter)

def part1(passwords):
    return sum(1 for p in passwords if is_valid_part1(*p))

def part2(passwords):
    return sum(1 for p in passwords if is_valid_part2(*p))

def main():
    passwords = read_input("2020/Day02/input.txt")
    print(f"Part 1: {part1(passwords)}")
    print(f"Part 2: {part2(passwords)}")

if __name__ == "__main__":
    main()