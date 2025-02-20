def calculate_syntax_error_score(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    matching_brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    total_score = 0
    
    for line in lines:
        stack = []
        for char in line:
            if char in "([{<":
                stack.append(char)
            elif char in ")]}>":
                if not stack or stack.pop() != matching_brackets[char]:
                    total_score += score_map[char]
                    break
    
    return total_score

def calculate_autocomplete_score(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    matching_brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    autocomplete_scores = []
    
    for line in lines:
        stack = []
        is_corrupted = False
        
        for char in line:
            if char in "([{<":
                stack.append(char)
            elif char in ")]}>":
                if not stack or stack.pop() != matching_brackets[char]:
                    is_corrupted = True
                    break
        
        if not is_corrupted:
            completion_string = [k for v in reversed(stack) for k, val in matching_brackets.items() if val == v]
            score = 0
            for char in completion_string:
                score = score * 5 + score_map[char]
            autocomplete_scores.append(score)
    
    autocomplete_scores.sort()
    middle_index = len(autocomplete_scores) // 2
    return autocomplete_scores[middle_index]

def main():
    print("\n--- Day 10: Syntax Scoring ---")
    input_file = '2021/input/day10.txt'
    syntax_error_score = calculate_syntax_error_score(input_file)
    print(f"Part 1: {syntax_error_score}")

    autocomplete_score = calculate_autocomplete_score(input_file)
    print(f"Part 2: {autocomplete_score}")

if __name__ == "__main__":
    main()