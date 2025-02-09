def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def swap_position(password, x, y):
    password = list(password)
    password[x], password[y] = password[y], password[x]
    return ''.join(password)

def swap_letter(password, x, y):
    return ''.join(y if c == x else x if c == y else c for c in password)

def rotate_steps(password, direction, steps):
    steps = steps % len(password)
    if direction == 'right':
        return password[-steps:] + password[:-steps]
    return password[steps:] + password[:steps]

def rotate_position(password, letter):
    index = password.index(letter)
    steps = 1 + index + (1 if index >= 4 else 0)
    return rotate_steps(password, 'right', steps)

def reverse_positions(password, x, y):
    password = list(password)
    password[x:y+1] = password[x:y+1][::-1]
    return ''.join(password)

def move_position(password, x, y):
    password = list(password)
    char = password.pop(x)
    password.insert(y, char)
    return ''.join(password)

def scramble(password, instructions):
    for instruction in instructions:
        words = instruction.split()
        if words[0] == 'swap':
            if words[1] == 'position':
                password = swap_position(password, int(words[2]), int(words[5]))
            else:  # swap letter
                password = swap_letter(password, words[2], words[5])
        elif words[0] == 'rotate':
            if words[1] in ['left', 'right']:
                password = rotate_steps(password, words[1], int(words[2]))
            else:  # rotate based on position
                password = rotate_position(password, words[6])
        elif words[0] == 'reverse':
            password = reverse_positions(password, int(words[2]), int(words[4]))
        elif words[0] == 'move':
            password = move_position(password, int(words[2]), int(words[5]))
    return password

def unscramble(password, instructions):
    instructions = instructions[::-1]
    for instruction in instructions:
        words = instruction.split()
        if words[0] == 'swap':
            if words[1] == 'position':
                password = swap_position(password, int(words[2]), int(words[5]))
            else:  # swap letter
                password = swap_letter(password, words[2], words[5])
        elif words[0] == 'rotate':
            if words[1] in ['left', 'right']:
                # Reverse direction for unscrambling
                direction = 'left' if words[1] == 'right' else 'right'
                password = rotate_steps(password, direction, int(words[2]))
            else:  # rotate based on position
                # Try all possible rotations until we find one that works
                original = password
                for i in range(len(password)):
                    test = rotate_steps(password, 'left', i)
                    if rotate_position(test, words[6]) == original:
                        password = test
                        break
        elif words[0] == 'reverse':
            password = reverse_positions(password, int(words[2]), int(words[4]))
        elif words[0] == 'move':
            # Swap x and y for unscrambling
            password = move_position(password, int(words[5]), int(words[2]))
    return password

def part1(instructions):
    return scramble('abcdefgh', instructions)

def part2(instructions):
    return unscramble('fbgdceah', instructions)

if __name__ == "__main__":
    instructions = parse_input("2016/Day21/input.txt")
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))