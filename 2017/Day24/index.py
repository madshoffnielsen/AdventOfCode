def parse_input(filename):
    """Reads input and returns a list of components as tuples."""
    with open(filename) as f:
        return [tuple(map(int, line.strip().split('/'))) for line in f]

def build_bridges(components, port=0, used=set()):
    """Recursively builds bridges and yields (strength, length)."""
    valid_bridges = []
    
    for component in components:
        if component in used or (port not in component):
            continue

        new_used = used | {component}
        next_port = component[1] if component[0] == port else component[0]

        for strength, length in build_bridges(components, next_port, new_used):
            valid_bridges.append((strength + sum(component), length + 1))

    if not valid_bridges:
        yield (0, 0)  # Base case: no further extensions
    else:
        yield from valid_bridges

def solve_day24(filename):
    components = parse_input(filename)
    bridges = list(build_bridges(components))

    # Part 1: Find the strongest bridge
    strongest_bridge = max(bridges, key=lambda x: x[0])[0]

    # Part 2: Find the longest bridge, and if tied, the strongest among them
    longest_bridge = max(bridges, key=lambda x: (x[1], x[0]))[0]

    return strongest_bridge, longest_bridge

if __name__ == "__main__":
    input_file = "2017/Day24/input.txt"
    part1, part2 = solve_day24(input_file)
    print("Part 1:", part1)
    print("Part 2:", part2)
