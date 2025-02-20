import re
from math import floor, ceil

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split("\n")

def add(a, b):
    return f"[{a},{b}]"

def reduce(a):
    while True:
        new_a = explode(a)
        if new_a != a:
            a = new_a
            continue
        
        new_a = split(a)
        if new_a != a:
            a = new_a
            continue
        
        break
    return a

def explode(a):
    stack = re.findall(r"\[|\]|\d+|,", a)
    opened = 0
    for i in range(len(stack) - 2):
        v = stack[i]
        if v == '[':
            opened += 1
        elif v == ']':
            opened -= 1
        elif v.isdigit() and stack[i + 1] == ',' and stack[i + 2].isdigit() and opened > 4:
            left_val = int(stack[i])
            right_val = int(stack[i + 2])

            for j in range(i - 1, -1, -1):
                if stack[j].isdigit():
                    stack[j] = str(int(stack[j]) + left_val)
                    break
            
            for j in range(i + 3, len(stack)):
                if stack[j].isdigit():
                    stack[j] = str(int(stack[j]) + right_val)
                    break

            stack = stack[:i - 1] + ['0'] + stack[i + 4:]
            return ''.join(stack)
    
    return a

def split(a):
    stack = re.findall(r"\[|\]|\d+|,", a)
    for i in range(len(stack)):
        v = stack[i]
        if v.isdigit() and int(v) >= 10:
            left = floor(int(v) / 2)
            right = ceil(int(v) / 2)
            stack = stack[:i] + ['[', str(left), ',', str(right), ']'] + stack[i + 1:]
            return ''.join(stack)
    return a

def magnitude(a):
    while ',' in a:
        a = re.sub(r"\[(\d+),(\d+)\]", lambda m: str(int(m.group(1)) * 3 + int(m.group(2)) * 2), a)
    return int(a)

def part1(lines):
    sum_str = lines[0]
    for i in range(1, len(lines)):
        sum_str = reduce(add(sum_str, lines[i]))
    return magnitude(sum_str)

def part2(lines, sum_str):
    max_magnitude = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                sum_str = add(lines[i], lines[j])
                reduced_str = reduce(sum_str)
                mag = magnitude(reduced_str)
                max_magnitude = max(max_magnitude, mag)
    return max_magnitude

def main():
    print("\n--- Day 18: Snailfish ---")
    input_file = '2021/input/day18.txt'
    lines = parse_input(input_file)
    sum_str = part1(lines)
    print(f"Part 1: {sum_str}")

    max_magnitude = part2(lines, sum_str)
    print(f"Part 2: {max_magnitude}")
    
if __name__ == "__main__":
    main()