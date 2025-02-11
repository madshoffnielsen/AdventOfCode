def read_input(file_path):
    with open(file_path) as f:
        return [[int(x) for x in line.split()] for line in f]

def get_differences(sequence):
    return [b - a for a, b in zip(sequence, sequence[1:])]

def build_pyramid(sequence):
    pyramid = [sequence]
    while any(x != 0 for x in pyramid[-1]):
        pyramid.append(get_differences(pyramid[-1]))
    return pyramid

def extrapolate_forward(pyramid):
    pyramid[-1].append(0)
    for i in range(len(pyramid) - 2, -1, -1):
        pyramid[i].append(pyramid[i][-1] + pyramid[i + 1][-1])
    return pyramid[0][-1]

def extrapolate_backward(pyramid):
    pyramid[-1].insert(0, 0)
    for i in range(len(pyramid) - 2, -1, -1):
        pyramid[i].insert(0, pyramid[i][0] - pyramid[i + 1][0])
    return pyramid[0][0]

def part1(sequences):
    return sum(extrapolate_forward(build_pyramid(seq)) for seq in sequences)

def part2(sequences):
    return sum(extrapolate_backward(build_pyramid(seq)) for seq in sequences)

def main():
    sequences = read_input("2023/Day09/input.txt")
    print(f"Part 1: {part1(sequences)}")
    print(f"Part 2: {part2(sequences)}")

if __name__ == "__main__":
    main()