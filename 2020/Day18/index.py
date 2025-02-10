import re

def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

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
                expr = re.sub(r"(\d+) \+ (\d+)", 
                            lambda m: str(int(m[1]) + int(m[2])), 
                            expr, count=1)
            tokens = expr.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                op, num = tokens[i], int(tokens[i+1])
                if op == "*":
                    result *= num
            return result

    def eval_recursive(expr):
        while "(" in expr:
            expr = re.sub(r"\(([^()]+)\)", 
                         lambda m: str(eval_recursive(m[1])), 
                         expr)
        return eval_simple(expr)

    return eval_recursive(expression)

def part1(expressions):
    return sum(evaluate(expr, "equal") for expr in expressions)

def part2(expressions):
    return sum(evaluate(expr, "addition_first") for expr in expressions)

def main():
    expressions = read_input("2020/Day18/input.txt")
    print(f"Part 1: {part1(expressions)}")
    print(f"Part 2: {part2(expressions)}")

if __name__ == "__main__":
    main()