import re

def parse_input(filename):
    with open(filename) as f:
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

def build_regex(rules, rule_num=0, part2=False, depth=0):
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
        # Match equal numbers of 42s and 31s
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

def count_valid_messages(rules, messages, part2=False):
    pattern = re.compile(f'^{build_regex(rules, part2=part2)}$')
    return sum(1 for msg in messages if pattern.match(msg))

def main():
    rules, messages = parse_input("2020/Day19/input.txt")
    print(f"Part 1: {count_valid_messages(rules, messages)}")
    print(f"Part 2: {count_valid_messages(rules, messages, True)}")

if __name__ == "__main__":
    main()