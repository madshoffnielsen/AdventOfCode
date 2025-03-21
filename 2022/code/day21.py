from collections import deque

def read_input(file_path):
    """Reads and parses the input file into a tree structure."""
    tree = {}
    with open(file_path, "r") as f:
        for line in f:
            tokens = line.strip().split()
            name = tokens[0].rstrip(":")
            if len(tokens) == 2:
                data = int(tokens[1])
                children = []
            else:
                data = tokens[2]
                children = [tokens[1], tokens[3]]
            tree[name] = (data, children)
    return tree

def evaluate_tree(tree, node):
    """Recursively evaluates the tree starting from the given node."""
    data, children = tree[node]
    if not children:
        return data
    v1 = evaluate_tree(tree, children[0])
    v2 = evaluate_tree(tree, children[1])
    if data == "+":
        return v1 + v2
    elif data == "-":
        return v1 - v2
    elif data == "*":
        return v1 * v2
    elif data == "/":
        return v1 / v2

def part1(tree):
    """Solves Part 1 by evaluating the tree starting from the root."""
    return int(evaluate_tree(tree, "root"))

def newton_method(g, x1, x2, coef=1e-2, max_iterations=1000, tolerance=0.1, debug=False):
    """Newton-Raphson method with under-relaxation to find the root of g."""
    g1 = g(x1)
    g2 = g(x2)
    if debug:
        print(f"Initial guess for Newton-Raphson: x1 = {x1}, x2 = {x2}, g1 = {g1}, g2 = {g2}")
    for i in range(max_iterations):
        dx = - (g2 - g1) / (x2 - x1) * g2
        x3 = x2 + coef * dx
        g3 = g(x3)
        if debug:
            print(f"Iteration {i}: x3 = {x3}, g3 = {g3}")
        if abs(g3) < tolerance:
            return int(round(x3)), i
        x1, x2 = x2, x3
        g1, g2 = g2, g3
    raise RuntimeError("Newton-Raphson method failed to converge.")

def part2(tree):
    """Solves Part 2 by finding the value of the 'humn' node."""
    def visit(tree, node):
        """Constructs a lambda function for each node to evaluate the tree."""
        data, children = tree[node]
        if not children:
            if node == "humn":
                return lambda v: v
            else:
                return lambda v: data
        f1 = visit(tree, children[0])
        f2 = visit(tree, children[1])
        if node == "root":
            return lambda v: (f1(v), f2(v))
        else:
            if data == "+":
                return lambda v: f1(v) + f2(v)
            elif data == "-":
                return lambda v: f1(v) - f2(v)
            elif data == "*":
                return lambda v: f1(v) * f2(v)
            elif data == "/":
                return lambda v: f1(v) / f2(v)

    f = visit(tree, "root")
    def g(v):
        v1, v2 = f(v)
        return v1 - v2

    x1, x2 = 1000, 2000  # Initial guesses
    coef = 1e-2  # Under-relaxation coefficient

    for trial in range(100):
        try:
            answer, _ = newton_method(g, x1, x2, coef)
            v1, v2 = f(answer)
            if int(v1) == int(v2):
                return answer
        except RuntimeError:
            coef *= 0.5  # Reduce the relaxation coefficient if convergence fails
    raise RuntimeError("Newton-Raphson method failed to converge after multiple trials.")

def main():
    print("\n--- Day 21: Monkey Math ---")
    file_path = "2022/input/day21.txt"
    tree = read_input(file_path)

    # Part 1
    result1 = part1(tree)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(tree)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()