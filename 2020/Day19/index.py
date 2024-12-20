import re

def parse_input(input_data):
    rules_section, messages_section = input_data.strip().split("\n\n")
    rules = {}
    for line in rules_section.split("\n"):
        num, rule = line.split(": ")
        if '"' in rule:
            rules[int(num)] = rule.strip('"')
        else:
            rules[int(num)] = [list(map(int, part.split())) for part in rule.split(" | ")]
    messages = messages_section.split("\n")
    return rules, messages

def build_regex(rules, rule_num=0):
    rule = rules[rule_num]
    if isinstance(rule, str):  # Base case: a literal character
        return rule
    # Otherwise, recursively build regex for sub-rules
    parts = []
    for sub_rule in rule:
        parts.append("".join(build_regex(rules, num) for num in sub_rule))
    return f"({'|'.join(parts)})"

def count_matching_messages(input_data):
    rules, messages = parse_input(input_data)
    regex = f"^{build_regex(rules)}$"
    pattern = re.compile(regex)
    return sum(1 for message in messages if pattern.fullmatch(message))

# Example usage
with open("2020/Day19/input.txt") as f:
    input_data = f.read()

result = count_matching_messages(input_data)
print(f"Number of messages matching rule 0: {result}")


def build_regex(rules, rule_num=0, depth=0, max_depth=20):
    """
    Builds regex for the rules. Adds depth limitation for recursive rules 8 and 11.
    """
    if depth > max_depth:
        return ""
    
    rule = rules[rule_num]
    if isinstance(rule, str):  # Base case: a literal character
        return rule
    
    if rule_num == 8:  # Special rule: 8 -> 42 | 42 8
        sub_regex = build_regex(rules, 42, depth + 1, max_depth)
        return f"({sub_regex}+)"  # Rule 8 matches one or more 42
    
    if rule_num == 11:  # Special rule: 11 -> 42 31 | 42 11 31
        sub_regex_42 = build_regex(rules, 42, depth + 1, max_depth)
        sub_regex_31 = build_regex(rules, 31, depth + 1, max_depth)
        return f"({ '|'.join(f'{sub_regex_42}{{{i}}}{sub_regex_31}{{{i}}}' for i in range(1, max_depth)) })"
    
    # For other rules, build regex recursively
    parts = []
    for sub_rule in rule:
        parts.append("".join(build_regex(rules, num, depth + 1, max_depth) for num in sub_rule))
    return f"({'|'.join(parts)})"

def count_matching_messages2(input_data):
    rules, messages = parse_input(input_data)
    
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    
    # Build regex for rule 0
    regex = f"^{build_regex(rules, 0)}$"
    pattern = re.compile(regex)
    return sum(1 for message in messages if pattern.fullmatch(message))

# Part 2
result_part2 = count_matching_messages2(input_data)
print(f"Part 2: Number of messages matching rule 0: {result_part2}")
