def read_input(file_path):
    with open(file_path) as f:
        return [(line[0], int(line[1:])) for line in f]

def rotate(x, y, degrees):
    # Rotate point (x,y) around origin
    for _ in range((degrees % 360) // 90):
        x, y = -y, x
    return x, y

def navigate_part1(instructions):
    x, y = 0, 0
    dx, dy = 1, 0  # Facing east
    
    for action, value in instructions:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            dx, dy = rotate(dx, dy, value)
        elif action == 'R':
            dx, dy = rotate(dx, dy, -value)
        elif action == 'F':
            x += dx * value
            y += dy * value
            
    return abs(x) + abs(y)

def navigate_part2(instructions):
    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1  # Waypoint starts 10 east, 1 north
    
    for action, value in instructions:
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, value)
        elif action == 'R':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, -value)
        elif action == 'F':
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value
            
    return abs(ship_x) + abs(ship_y)

def main():
    instructions = read_input("2020/Day12/input.txt")
    print(f"Part 1: {navigate_part1(instructions)}")
    print(f"Part 2: {navigate_part2(instructions)}")

if __name__ == "__main__":
    main()