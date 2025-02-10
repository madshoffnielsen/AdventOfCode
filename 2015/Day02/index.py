def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def parse_dimensions(dimensions):
    return [tuple(map(int, dim.split('x'))) for dim in dimensions]

def calculate_wrapping_paper(dimensions):
    total_paper = 0
    for l, w, h in dimensions:
        sides = [l*w, w*h, h*l]
        total_paper += 2 * sum(sides) + min(sides)
    return total_paper

def calculate_ribbon(dimensions):
    total_ribbon = 0
    for l, w, h in dimensions:
        perimeters = [2*(l+w), 2*(w+h), 2*(h+l)]
        total_ribbon += min(perimeters) + l*w*h
    return total_ribbon

def main():
    dimensions = read_input("2015/Day02/input.txt")
    parsed_dimensions = parse_dimensions(dimensions)
    print(f"Part 1: {calculate_wrapping_paper(parsed_dimensions)}")
    print(f"Part 2: {calculate_ribbon(parsed_dimensions)}")

if __name__ == "__main__":
    main()