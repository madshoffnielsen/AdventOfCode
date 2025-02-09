def dragon_curve(data):
    a = data
    b = ''.join('1' if x == '0' else '0' for x in reversed(a))
    return a + '0' + b

def generate_data(initial_state, length):
    data = initial_state
    while len(data) < length:
        data = dragon_curve(data)
    return data[:length]

def calculate_checksum(data):
    while len(data) % 2 == 0:
        data = ''.join('1' if data[i] == data[i + 1] else '0' for i in range(0, len(data), 2))
    return data

def solve(initial_state, length):
    data = generate_data(initial_state, length)
    return calculate_checksum(data)

def part1(initial_state):
    return solve(initial_state, 272)

def part2(initial_state):
    return solve(initial_state, 35651584)

if __name__ == "__main__":
    initial_state = "00111101111101000"
    print("Part 1:", part1(initial_state))
    print("Part 2:", part2(initial_state))