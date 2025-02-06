from collections import deque, defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def parse_regex(regex):
    stack = []
    positions = set()
    x, y = 0, 0
    positions.add((x, y))
    distances = defaultdict(lambda: float('inf'))
    distances[(x, y)] = 0

    for char in regex:
        if char == '(':
            stack.append((x, y))
        elif char == ')':
            x, y = stack.pop()
        elif char == '|':
            x, y = stack[-1]
        else:
            if char == 'N':
                y -= 1
            elif char == 'S':
                y += 1
            elif char == 'E':
                x += 1
            elif char == 'W':
                x -= 1
            positions.add((x, y))
            distances[(x, y)] = min(distances[(x, y)], distances[(x - (char == 'E') + (char == 'W'), y - (char == 'S') + (char == 'N'))] + 1)

    return distances

def part1(distances):
    return max(distances.values())

def part2(distances):
    return sum(1 for distance in distances.values() if distance >= 1000)

if __name__ == "__main__":
    input_file = "2018/Day20/input.txt"
    regex = read_input(input_file)
    distances = parse_regex(regex[1:-1])  # Remove the outer ^ and $
    
    result_part1 = part1(distances)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(distances)
    print(f"Part 2: {result_part2}")