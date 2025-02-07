class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

def read_input(file_path):
    nodes = {}
    with open(file_path) as f:
        for line in f:
            parts = line.strip().replace('(', '').replace(')', '').split(' -> ')
            name_weight = parts[0].split()
            name = name_weight[0]
            weight = int(name_weight[1])
            nodes[name] = Node(name, weight)
            
            if len(parts) > 1:
                children = parts[1].split(', ')
                nodes[name].children = children
    
    # Set parent relationships
    for name, node in nodes.items():
        for child in node.children:
            nodes[child].parent = name
    
    return nodes

def find_root(nodes):
    for name, node in nodes.items():
        if node.parent is None:
            return name

def get_tower_weight(nodes, name):
    node = nodes[name]
    return node.weight + sum(get_tower_weight(nodes, child) for child in node.children)

def find_unbalanced(nodes, name):
    node = nodes[name]
    if not node.children:
        return None, node.weight

    # Get weights of all children
    weights = [(child, get_tower_weight(nodes, child)) for child in node.children]
    weight_counts = {}
    for _, w in weights:
        weight_counts[w] = weight_counts.get(w, 0) + 1
    
    # If all weights same, return total weight
    if len(weight_counts) == 1:
        return None, node.weight + sum(w for _, w in weights)
    
    # Find the unbalanced child
    expected_weight = next(w for w, count in weight_counts.items() if count > 1)
    wrong_weight = next(w for w, count in weight_counts.items() if count == 1)
    wrong_node = next(child for child, w in weights if w == wrong_weight)
    
    # Recursively check children
    child_result, child_weight = find_unbalanced(nodes, wrong_node)
    
    # If child has the problem, return its result
    if child_result is not None:
        return child_result, child_weight
    
    # Otherwise, this is the node that needs fixing
    weight_diff = expected_weight - wrong_weight
    return nodes[wrong_node].weight + weight_diff, None

def main():
    nodes = read_input("2017/Day07/input.txt")
    root = find_root(nodes)
    print(f"Part 1: {root}")
    
    corrected_weight, _ = find_unbalanced(nodes, root)
    print(f"Part 2: {corrected_weight}")

if __name__ == "__main__":
    main()