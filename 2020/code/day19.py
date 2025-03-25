import re
from typing import Dict, List, Union, Tuple

Rule = Union[str, List[List[int]]]
Rules = Dict[int, Rule]

def read_input(file_path: str) -> Tuple[Rules, List[str]]:
    """Read message rules and messages from file."""
    with open(file_path) as f:
        rules_raw, messages = f.read().strip().split('\n\n')
    
    rules = {}
    for line in rules_raw.splitlines():
        num, rule = line.split(': ')
        if '"' in rule:
            rules[int(num)] = rule.strip('"')
        else:
            rules[int(num)] = [[int(x) for x in alt.split()] 
                              for alt in rule.split(' | ')]
    
    return rules, messages.splitlines()

def build_regex(rules: Rules, rule_num: int = 0, part2: bool = False, depth: int = 0) -> str:
    """Build regex pattern from rules."""
    if part2 and depth > 20:  # Prevent infinite recursion
        return ''
    
    if rule_num == 8 and part2:
        # Rule 8: 42 | 42 8
        pattern42 = build_regex(rules, 42, part2, depth + 1)
        return f'({pattern42})+'
    
    elif rule_num == 11 and part2:
        # Rule 11: 42 31 | 42 11 31
        pattern42 = build_regex(rules, 42, part2, depth + 1)
        pattern31 = build_regex(rules, 31, part2, depth + 1)
        patterns = []
        for i in range(1, 5):  # Limit depth for practical purposes
            patterns.append(f'({pattern42}{{{i}}}{pattern31}{{{i}}})')
        return f'({"|".join(patterns)})'
    
    rule = rules[rule_num]
    if isinstance(rule, str):
        return rule
        
    patterns = []
    for subrule in rule:
        pattern = ''.join(build_regex(rules, r, part2, depth + 1) 
                         for r in subrule)
        patterns.append(pattern)
    
    return f'({"|".join(patterns)})'

def count_valid_messages(rules: Rules, messages: List[str], part2: bool = False) -> int:
    """Count messages that match rule 0."""
    pattern = re.compile(f'^{build_regex(rules, part2=part2)}$')
    return sum(1 for msg in messages if pattern.match(msg))

def part1(rules: Rules, messages: List[str]) -> int:
    """Count valid messages using original rules."""
    return count_valid_messages(rules, messages)

def part2(rules: Rules, messages: List[str]) -> int:
    """Count valid messages using modified rules 8 and 11."""
    return count_valid_messages(rules, messages, True)

def main():
    """Main program."""
    print("\n--- Day 19: Monster Messages ---")
    
    rules, messages = read_input("2020/input/day19.txt")
    
    result1 = part1(rules, messages)
    print(f"Part 1: {result1}")
    
    result2 = part2(rules, messages)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()