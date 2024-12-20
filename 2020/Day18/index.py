import re

def evaluate(expression, precedence):
    """Evaluates a mathematical expression based on the given precedence rules."""
    if precedence == "equal":
        # Addition and multiplication have the same precedence
        def eval_simple(expr):
            tokens = expr.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                op, num = tokens[i], int(tokens[i+1])
                if op == "+":
                    result += num
                elif op == "*":
                    result *= num
            return result

    elif precedence == "addition_first":
        # Addition has higher precedence
        def eval_simple(expr):
            while "+" in expr:
                expr = re.sub(r"(\d+) \+ (\d+)", lambda m: str(int(m[1]) + int(m[2])), expr, count=1)
            tokens = expr.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                op, num = tokens[i], int(tokens[i+1])
                if op == "*":
                    result *= num
            return result

    def eval_recursive(expr):
        while "(" in expr:
            expr = re.sub(r"\(([^()]+)\)", lambda m: str(eval_recursive(m[1])), expr)
        return eval_simple(expr)

    return eval_recursive(expression)


def solve(filename):
    """Solve Day 18 for both parts."""
    with open(filename) as f:
        expressions = f.read().strip().split("\n")

    # Part 1: Addition and multiplication have the same precedence
    part1_result = sum(evaluate(expr, "equal") for expr in expressions)

    # Part 2: Addition has higher precedence than multiplication
    part2_result = sum(evaluate(expr, "addition_first") for expr in expressions)

    return part1_result, part2_result


# Run the solution
filename = "2020/Day18/input.txt"
part1, part2 = solve(filename)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
