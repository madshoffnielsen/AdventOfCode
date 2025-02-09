def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip().split(', ')

def move(position, direction, steps):
    x, y = position
    if direction == 'N':
        return (x, y + steps)
    elif direction == 'E':
        return (x + steps, y)
    elif direction == 'S':
        return (x, y - steps)
    elif direction == 'W':
        return (x - steps, y)

def turn(current_direction, turn_direction):
    directions = ['N', 'E', 'S', 'W']
    idx = directions.index(current_direction)
    if turn_direction == 'L':
        return directions[(idx - 1) % 4]
    else:
        return directions[(idx + 1) % 4]

def part1(instructions):
    position = (0, 0)
    direction = 'N'
    
    for instruction in instructions:
        turn_direction = instruction[0]
        steps = int(instruction[1:])
        direction = turn(direction, turn_direction)
        position = move(position, direction, steps)
    
    return abs(position[0]) + abs(position[1])

def part2(instructions):
    position = (0, 0)
    direction = 'N'
    visited = set()
    visited.add(position)
    
    for instruction in instructions:
        turn_direction = instruction[0]
        steps = int(instruction[1:])
        direction = turn(direction, turn_direction)
        
        for _ in range(steps):
            position = move(position, direction, 1)
            if position in visited:
                return abs(position[0]) + abs(position[1])
            visited.add(position)
    
    return None

if __name__ == "__main__":
    instructions = parse_input("2016/Day01/input.txt")
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))