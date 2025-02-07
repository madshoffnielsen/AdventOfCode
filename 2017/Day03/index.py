def get_coordinates(n):
    if n == 1:
        return 0, 0
    
    # Find the ring number and side length
    ring = 1
    while (2*ring+1)**2 < n:
        ring += 1
    
    side = 2*ring + 1
    max_in_ring = side**2
    
    # Find position within the ring
    pos = max_in_ring - n
    side_length = side - 1
    
    # Calculate coordinates based on which side of the ring
    if pos < side_length:  # bottom side
        return ring - pos, -ring
    pos -= side_length
    if pos < side_length:  # left side
        return -ring, -ring + pos
    pos -= side_length
    if pos < side_length:  # top side
        return -ring + pos, ring
    pos -= side_length
    return ring, ring - pos  # right side

def part1(num):
    x, y = get_coordinates(num)
    return abs(x) + abs(y)

def part2(num):
    values = {(0,0): 1}
    x, y = 0, 0
    steps = 0
    direction = 0  # 0:right, 1:up, 2:left, 3:down
    step_size = 1
    
    while True:
        # Move in current direction
        if direction == 0: x += 1
        elif direction == 1: y += 1
        elif direction == 2: x -= 1
        else: y -= 1
        
        # Calculate sum of adjacent values
        value = 0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if (x+dx,y+dy) in values:
                    value += values[(x+dx,y+dy)]
        
        values[(x,y)] = value
        if value > num:
            return value
        
        # Update direction and step size
        steps += 1
        if steps == step_size:
            direction = (direction + 1) % 4
            steps = 0
            if direction in [0, 2]:
                step_size += 1

def main():
    input_value = 347991
    print(f"Part 1: {part1(input_value)}")
    print(f"Part 2: {part2(input_value)}")

if __name__ == "__main__":
    main()