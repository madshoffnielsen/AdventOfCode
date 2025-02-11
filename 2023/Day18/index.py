def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

def get_direction(d):
    return {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0),
        '0': (0, 1),   # Right
        '1': (1, 0),   # Down
        '2': (0, -1),  # Left
        '3': (-1, 0)   # Up
    }[d]

def calculate_area(vertices):
    # Shoelace formula + boundary points
    area = 0
    perimeter = 0
    
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        r1, c1 = vertices[i]
        r2, c2 = vertices[j]
        
        # Shoelace formula
        area += r1 * c2 - r2 * c1
        
        # Manhattan distance for perimeter
        perimeter += abs(r2 - r1) + abs(c2 - c1)
    
    # Area formula: internal points + perimeter/2 + 1
    return abs(area) // 2 + perimeter // 2 + 1

def process_instructions(instructions, use_hex=False):
    vertices = [(0, 0)]
    r, c = 0, 0
    
    for direction, steps, color in instructions:
        if use_hex:
            steps = int(color[2:-2], 16)
            direction = color[-2]
        else:
            steps = int(steps)
            
        dr, dc = get_direction(direction)
        r += dr * steps
        c += dc * steps
        vertices.append((r, c))
    
    return vertices

def part1(instructions):
    vertices = process_instructions(instructions)
    return calculate_area(vertices)

def part2(instructions):
    vertices = process_instructions(instructions, use_hex=True)
    return calculate_area(vertices)

def main():
    instructions = read_input("2023/Day18/input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

if __name__ == "__main__":
    main()