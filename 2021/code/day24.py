def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return input_data

def parse_input(input_data):
    lines = input_data.split('\n')
    return lines

def process_instructions(lines):
    var = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    inp = [9] * 14
    pointer = 1

    x = 0
    y = 0
    dump = []
    lets = []

    for i in range(14):
        l = chr(65 + i)
        stuff = []
        stuff.append(int(lines[(i * 18) + 4].split()[2]))
        stuff.append(int(lines[(i * 18) + 5].split()[2]))
        stuff.append(int(lines[(i * 18) + 15].split()[2]))
        if stuff[0] == 1:
            dump.append([l, stuff[2]])
        else:
            d = dump.pop()
            lets.append([l, d[0], d[1] + stuff[1]])

    return lets

def calculate_min_max(lets):
    min_vals = [0] * 14
    max_vals = [0] * 14

    for l in lets:
        a = ord(l[0]) - 65
        b = ord(l[1]) - 65
        if l[2] > 0:
            max_vals[a] = 9
            max_vals[b] = 9 - l[2]
            min_vals[b] = 1
            min_vals[a] = 1 + l[2]
        else:
            max_vals[b] = 9
            max_vals[a] = 9 + l[2]
            min_vals[a] = 1
            min_vals[b] = 1 - l[2]

    return max_vals, min_vals

def main():
    print("\n--- Day 24: Arithmetic Logic Unit ---")
    input_file = '2021/input/day24.txt'
    input_data = read_input(input_file)
    lines = parse_input(input_data)
    lets = process_instructions(lines)
    max_vals, min_vals = calculate_min_max(lets)

    print(f"Part 1: {"".join(map(str, max_vals))}")
    print(f"Part 2: {"".join(map(str, min_vals))}")

if __name__ == "__main__":
    main()