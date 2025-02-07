def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip().split(',')

def get_direction(step):
    # Using cube coordinates (x, y, z)
    directions = {
        'n':  (0, 1, -1),
        'ne': (1, 0, -1),
        'se': (1, -1, 0),
        's':  (0, -1, 1),
        'sw': (-1, 0, 1),
        'nw': (-1, 1, 0)
    }
    return directions[step]

def hex_distance(x, y, z):
    return max(abs(x), abs(y), abs(z))

def follow_path(steps):
    x = y = z = 0
    max_dist = 0
    
    for step in steps:
        dx, dy, dz = get_direction(step)
        x += dx
        y += dy
        z += dz
        max_dist = max(max_dist, hex_distance(x, y, z))
    
    return hex_distance(x, y, z), max_dist

def main():
    steps = read_input("2017/Day11/input.txt")
    final_dist, max_dist = follow_path(steps)
    print(f"Part 1: {final_dist}")
    print(f"Part 2: {max_dist}")

if __name__ == "__main__":
    main()