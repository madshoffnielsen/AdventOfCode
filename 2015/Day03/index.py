def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip()

def move(position, direction):
    x, y = position
    if direction == '^':
        return (x, y + 1)
    elif direction == 'v':
        return (x, y - 1)
    elif direction == '>':
        return (x + 1, y)
    elif direction == '<':
        return (x - 1, y)

def part1(directions):
    position = (0, 0)
    visited = {position}
    
    for direction in directions:
        position = move(position, direction)
        visited.add(position)
    
    return len(visited)

def part2(directions):
    santa_position = (0, 0)
    robo_position = (0, 0)
    visited = {santa_position}
    
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            santa_position = move(santa_position, direction)
            visited.add(santa_position)
        else:
            robo_position = move(robo_position, direction)
            visited.add(robo_position)
    
    return len(visited)

def main():
    directions = read_input("2015/Day03/input.txt")
    print(f"Part 1: {part1(directions)}")
    print(f"Part 2: {part2(directions)}")

if __name__ == "__main__":
    main()