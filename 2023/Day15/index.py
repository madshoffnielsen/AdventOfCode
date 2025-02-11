def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip().split(',')

def hash_algorithm(s):
    value = 0
    for c in s:
        value = ((value + ord(c)) * 17) % 256
    return value

def process_instruction(instruction, boxes):
    if '=' in instruction:
        label, focal = instruction.split('=')
        box = hash_algorithm(label)
        focal = int(focal)
        
        # Update or add lens
        for i, (existing_label, _) in enumerate(boxes[box]):
            if existing_label == label:
                boxes[box][i] = (label, focal)
                break
        else:
            boxes[box].append((label, focal))
    else:
        label = instruction[:-1]
        box = hash_algorithm(label)
        
        # Remove lens if it exists
        boxes[box] = [(l, f) for l, f in boxes[box] if l != label]

def calculate_power(boxes):
    total = 0
    for box_num, lenses in enumerate(boxes):
        for slot, (_, focal) in enumerate(lenses, 1):
            total += (box_num + 1) * slot * focal
    return total

def part1(steps):
    return sum(hash_algorithm(step) for step in steps)

def part2(steps):
    boxes = [[] for _ in range(256)]
    for step in steps:
        process_instruction(step, boxes)
    return calculate_power(boxes)

def main():
    steps = read_input("2023/Day15/input.txt")
    print(f"Part 1: {part1(steps)}")
    print(f"Part 2: {part2(steps)}")

if __name__ == "__main__":
    main()