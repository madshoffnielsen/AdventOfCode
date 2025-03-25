from typing import Dict, List, Set, Tuple
from math import prod

Rules = Dict[str, List[range]]
Ticket = List[int]

def read_input(file_path: str) -> Tuple[Rules, Ticket, List[Ticket]]:
    """Read ticket rules and values from input file."""
    with open(file_path) as f:
        sections = f.read().strip().split("\n\n")

    # Parse rules
    rules: Rules = {}
    for line in sections[0].splitlines():
        field, ranges = line.split(": ")
        rules[field] = []
        for part in ranges.split(" or "):
            low, high = map(int, part.split("-"))
            rules[field].append(range(low, high + 1))

    # Parse your ticket
    your_ticket = list(map(int, sections[1].splitlines()[1].split(",")))

    # Parse nearby tickets
    nearby_tickets = [
        list(map(int, line.split(","))) 
        for line in sections[2].splitlines()[1:]
    ]

    return rules, your_ticket, nearby_tickets

def is_valid_value(value: int, rules: Rules) -> bool:
    """Check if value is valid for any field."""
    return any(value in r for ranges in rules.values() for r in ranges)

def find_invalid_values(ticket: Ticket, rules: Rules) -> List[int]:
    """Find invalid values in ticket."""
    return [value for value in ticket if not is_valid_value(value, rules)]

def get_valid_tickets(tickets: List[Ticket], rules: Rules) -> List[Ticket]:
    """Filter valid tickets."""
    return [ticket for ticket in tickets if not find_invalid_values(ticket, rules)]

def determine_fields(valid_tickets: List[Ticket], rules: Rules) -> Dict[int, str]:
    """Map ticket positions to field names."""
    positions = len(valid_tickets[0])
    possible_fields: Dict[int, Set[str]] = {}
    
    # Find possible fields for each position
    for pos in range(positions):
        values = [ticket[pos] for ticket in valid_tickets]
        possible_fields[pos] = set()
        for field, ranges in rules.items():
            if all(any(v in r for r in ranges) for v in values):
                possible_fields[pos].add(field)
    
    # Eliminate fields until each position has one field
    field_mapping: Dict[int, str] = {}
    while possible_fields:
        pos = min(possible_fields, key=lambda p: len(possible_fields[p]))
        field = possible_fields[pos].pop()
        field_mapping[pos] = field
        
        for other_pos in possible_fields:
            possible_fields[other_pos].discard(field)
        
        del possible_fields[pos]
    
    return field_mapping

def part1(rules: Rules, nearby_tickets: List[Ticket]) -> int:
    """Sum invalid values in nearby tickets."""
    return sum(sum(find_invalid_values(ticket, rules)) for ticket in nearby_tickets)

def part2(rules: Rules, your_ticket: Ticket, nearby_tickets: List[Ticket]) -> int:
    """Multiply departure field values."""
    valid_tickets = get_valid_tickets(nearby_tickets, rules)
    field_mapping = determine_fields(valid_tickets + [your_ticket], rules)
    
    departure_values = [
        your_ticket[pos]
        for pos, field in field_mapping.items()
        if field.startswith("departure")
    ]
    return prod(departure_values)

def main():
    """Main program."""
    print("\n--- Day 16: Ticket Translation ---")
    
    rules, your_ticket, nearby_tickets = read_input("2020/input/day16.txt")
    
    result1 = part1(rules, nearby_tickets)
    print(f"Part 1: {result1}")
    
    result2 = part2(rules, your_ticket, nearby_tickets)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()