def read_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip().split()))

def parse_node(data, index=0):
    num_children = data[index]
    num_metadata = data[index + 1]
    index += 2
    children = []
    for _ in range(num_children):
        child, index = parse_node(data, index)
        children.append(child)
    metadata = data[index:index + num_metadata]
    index += num_metadata
    return (children, metadata), index

def sum_metadata(node):
    children, metadata = node
    return sum(metadata) + sum(sum_metadata(child) for child in children)

def value_of_node(node):
    children, metadata = node
    if not children:
        return sum(metadata)
    value = 0
    for m in metadata:
        if 1 <= m <= len(children):
            value += value_of_node(children[m - 1])
    return value

def part1(data):
    root, _ = parse_node(data)
    return sum_metadata(root)

def part2(data):
    root, _ = parse_node(data)
    return value_of_node(root)

if __name__ == "__main__":
    input_file = "2018/Day08/input.txt"
    data = read_input(input_file)
    
    result_part1 = part1(data)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(data)
    print(f"Part 2: {result_part2}")