from dataclasses import dataclass
from typing import Dict, List, Tuple
import re

@dataclass
class Rule:
    category: str = ''
    operator: str = ''
    value: int = 0
    target: str = ''
    is_default: bool = False

def parse_workflow(line: str) -> Tuple[str, List[Rule]]:
    name, rules_str = re.match(r'(\w+){(.*)}', line).groups()
    rules = []
    
    for rule_str in rules_str.split(','):
        if ':' in rule_str:
            condition, target = rule_str.split(':')
            category = condition[0]
            operator = condition[1]
            value = int(condition[2:])
            rules.append(Rule(category, operator, value, target))
        else:
            rules.append(Rule(target=rule_str, is_default=True))
    
    return name, rules

def parse_part(line: str) -> Dict[str, int]:
    return {k: int(v) for k, v in 
            re.findall(r'(\w)=(\d+)', line)}

def process_part(part: Dict[str, int], workflows: Dict[str, List[Rule]]) -> bool:
    current = 'in'
    while current not in ('A', 'R'):
        for rule in workflows[current]:
            if rule.is_default:
                current = rule.target
                break
            if rule.operator == '<':
                if part[rule.category] < rule.value:
                    current = rule.target
                    break
            else:
                if part[rule.category] > rule.value:
                    current = rule.target
                    break
    return current == 'A'

def process_ranges(ranges: Dict[str, Tuple[int, int]], 
                  workflows: Dict[str, List[Rule]], 
                  current: str='in') -> int:
    if current == 'R':
        return 0
    if current == 'A':
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1
        return product
    
    total = 0
    for rule in workflows[current]:
        if rule.is_default:
            total += process_ranges(ranges.copy(), workflows, rule.target)
        else:
            new_ranges = ranges.copy()
            if rule.operator == '<':
                if ranges[rule.category][0] < rule.value:
                    new_ranges[rule.category] = (ranges[rule.category][0], 
                                               min(rule.value - 1, 
                                                   ranges[rule.category][1]))
                    total += process_ranges(new_ranges, workflows, rule.target)
                    ranges[rule.category] = (rule.value, ranges[rule.category][1])
            else:
                if ranges[rule.category][1] > rule.value:
                    new_ranges[rule.category] = (max(rule.value + 1, 
                                                   ranges[rule.category][0]), 
                                               ranges[rule.category][1])
                    total += process_ranges(new_ranges, workflows, rule.target)
                    ranges[rule.category] = (ranges[rule.category][0], rule.value)
    
    return total

def main():
    with open("2023/Day19/input.txt") as f:
        workflows_str, parts_str = f.read().strip().split('\n\n')
    
    workflows = dict(parse_workflow(line) for line in workflows_str.splitlines())
    parts = [parse_part(line) for line in parts_str.splitlines()]
    
    # Part 1
    total = sum(sum(part.values()) for part in parts 
                if process_part(part, workflows))
    print(f"Part 1: {total}")
    
    # Part 2
    ranges = {c: (1, 4000) for c in 'xmas'}
    print(f"Part 2: {process_ranges(ranges, workflows)}")

if __name__ == "__main__":
    main()