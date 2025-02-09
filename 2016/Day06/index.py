from collections import Counter

def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def get_corrected_message(messages, most_common=True):
    columns = zip(*messages)
    corrected_message = []
    for column in columns:
        counter = Counter(column)
        if most_common:
            corrected_message.append(counter.most_common(1)[0][0])
        else:
            corrected_message.append(counter.most_common()[-1][0])
    return ''.join(corrected_message)

def part1(messages):
    return get_corrected_message(messages, most_common=True)

def part2(messages):
    return get_corrected_message(messages, most_common=False)

if __name__ == "__main__":
    messages = parse_input("2016/Day06/input.txt")
    print("Part 1:", part1(messages))
    print("Part 2:", part2(messages))