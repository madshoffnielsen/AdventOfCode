def read_input(file_path):
    with open(file_path) as f:
        pairs = {}
        inputs = []
        for line in f:
            if "|" in line:
                pair = line.strip().split("|")
                key, value = int(pair[0]), int(pair[1])
                if key in pairs:
                    pairs[key].append(value)
                else:
                    pairs[key] = [value]
            elif "," in line:
                inputs.append(list(map(int, line.strip().split(","))))
        return pairs, inputs

def middle_page_number(pairs, inputs):
    count = 0
    for input in inputs:
        if check_order(pairs, input):
            count += input[len(input) // 2]
    return count

def fix_middle_page_number(pairs, inputs):
    count = 0
    for input in inputs:
        if not check_order(pairs, input):
            input = re_order(pairs, input)
            count += input[len(input) // 2]
    return count

def check_order(pairs, input):
    for idx, x in enumerate(input):
        for y in input[idx + 1:]:
            if x not in pairs or y not in pairs[x]:
                return False
    return True

def re_order(pairs, input):
    n = len(input)
    while True:
        swapped = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                if input[i] not in pairs or input[j] not in pairs[input[i]]:
                    input[i], input[j] = input[j], input[i]
                    swapped = True
        if not swapped:
            break
    return input

def main():
    pairs, inputs = read_input("2024/Day05/input.txt")
    print(f"Part 1: {middle_page_number(pairs, inputs)}")
    print(f"Part 2: {fix_middle_page_number(pairs, inputs)}")

if __name__ == "__main__":
    main()