import numpy as np

def calculate_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    return ((power // 100) % 10) - 5

def build_summed_area_table(serial):
    # Create grid with 1-based indexing
    grid = np.zeros((301, 301), dtype=int)
    for y in range(1, 301):
        for x in range(1, 301):
            grid[y,x] = calculate_power(x, y, serial)
    
    # Build summed area table
    sat = np.zeros((301, 301), dtype=int)
    for y in range(1, 301):
        for x in range(1, 301):
            sat[y,x] = grid[y,x] + sat[y-1,x] + sat[y,x-1] - sat[y-1,x-1]
    return sat

def get_square_sum(sat, x, y, size):
    x1, y1 = x-1, y-1  # Convert to 0-based for array indexing
    return sat[y1+size,x1+size] - sat[y1,x1+size] - sat[y1+size,x1] + sat[y1,x1]

def part1(serial):
    sat = build_summed_area_table(serial)
    max_power = float('-inf')
    max_coord = None
    
    for y in range(1, 299):
        for x in range(1, 299):
            power = get_square_sum(sat, x, y, 3)
            if power > max_power:
                max_power = power
                max_coord = (x, y)
    return max_coord

def part2(serial):
    sat = build_summed_area_table(serial)
    max_power = float('-inf')
    result = None
    
    for size in range(1, 301):
        for y in range(1, 302-size):
            for x in range(1, 302-size):
                power = get_square_sum(sat, x, y, size)
                if power > max_power:
                    max_power = power
                    result = (x, y, size)
    return result

if __name__ == "__main__":
    serial = 6303
    
    x, y = part1(serial)
    print(f"Part 1: {x},{y}")
    
    x, y, size = part2(serial)
    print(f"Part 2: {x},{y},{size}")