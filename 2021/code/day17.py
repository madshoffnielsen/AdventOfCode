import re

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    
    match = re.search(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', file_content)
    
    if match:
        x_min = int(match.group(1))
        x_max = int(match.group(2))
        y_min = int(match.group(3))
        y_max = int(match.group(4))
        
        return x_min, x_max, y_min, y_max
    else:
        raise ValueError("Invalid input format.")

def simulate_trajectory(vx, vy, x_min, x_max, y_min, y_max):
    x, y = 0, 0
    max_y = 0
    
    while x <= x_max and y >= y_min:
        x += vx
        y += vy
        
        max_y = max(max_y, y)
        
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return max_y
        
        if vx > 0:
            vx -= 1
        vy -= 1
    
    return None

def find_highest_y_position(x_min, x_max, y_min, y_max):
    max_height = 0
    valid_velocities = 0
    
    for vx in range(x_max + 1):
        for vy in range(y_min, abs(y_min) + 1):
            max_y = simulate_trajectory(vx, vy, x_min, x_max, y_min, y_max)
            if max_y is not None:
                valid_velocities += 1
                max_height = max(max_height, max_y)
    
    return max_height

def simulate_trajectory2(vx, vy, x_min, x_max, y_min, y_max):
    x, y = 0, 0
    
    while x <= x_max and y >= y_min:
        x += vx
        y += vy
        
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        
        if vx > 0:
            vx -= 1
        vy -= 1
    
    return False

def find_valid_velocities(x_min, x_max, y_min, y_max):
    valid_velocities = 0
    
    for vx in range(x_max + 1):
        for vy in range(y_min, abs(y_min) + 1):
            if simulate_trajectory2(vx, vy, x_min, x_max, y_min, y_max):
                valid_velocities += 1
    
    return valid_velocities

def main():
    print("\n--- Day 17: Trick Shot ---")
    input_file = '2021/input/day17.txt'
    x_min, x_max, y_min, y_max = read_input_from_file(input_file)
    highest_y = find_highest_y_position(x_min, x_max, y_min, y_max)
    print(f"Part 1: {highest_y}")
    
    valid_velocities = find_valid_velocities(x_min, x_max, y_min, y_max)
    print(f"Part 2: {valid_velocities}")

if __name__ == "__main__":
    main()