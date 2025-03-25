import re
from typing import List, Callable

def read_input(file_path: str) -> List[str]:
    """Read mathematical expressions from file."""
    with open(file_path) as f:
        return [line.strip() for line in f]

def create_evaluator(precedence: str) -> Callable[[str], int]:
    """Create evaluation function based on precedence rules."""
    if precedence == "equal":
        def eval_simple(expr: str) -> int:
            tokens = expr.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                op, num = tokens[i], int(tokens[i+1])
                if op == "+":
                    result += num
                elif op == "*":
                    result *= num
            return result
    else:  # addition_first
        def eval_simple(expr: str) -> int:
            while "+" in expr:
                expr = re.sub(r"(\d+) \+ (\d+)", 
                            lambda m: str(int(m[1]) + int(m[2])), 
                            expr, count=1)
            tokens = expr.split()
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                if tokens[i] == "*":
                    result *= int(tokens[i+1])
            return result
    return eval_simple

def evaluate(expression: str, precedence: str) -> int:
    """Evaluate expression with given operator precedence."""
    eval_simple = create_evaluator(precedence)
    
    def eval_recursive(expr: str) -> int:
        while "(" in expr:
            expr = re.sub(r"\(([^()]+)\)", 
                         lambda m: str(eval_recursive(m[1])), 
                         expr)
        return eval_simple(expr)
    
    return eval_recursive(expression)

def part1(expressions: List[str]) -> int:
    """Sum results of expressions with equal precedence."""
    return sum(evaluate(expr, "equal") for expr in expressions)

def part2(expressions: List[str]) -> int:
    """Sum results of expressions with addition before multiplication."""
    return sum(evaluate(expr, "addition_first") for expr in expressions)

def main():
    """Main program."""
    print("\n--- Day 18: Operation Order ---")
    
    expressions = read_input("2020/input/day18.txt")
    
    result1 = part1(expressions)
    print(f"Part 1: {result1}")
    
    result2 = part2(expressions)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()