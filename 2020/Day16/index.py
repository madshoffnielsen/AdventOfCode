import re
from math import prod

def parse_input(filename):
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")

    # Parse rules
    rules = {}
    for line in sections[0].splitlines():
        field, ranges = line.split(": ")
        range_parts = ranges.split(" or ")
        rules[field] = []
        for part in range_parts:
            low, high = map(int, part.split("-"))
            rules[field].append(range(low, high + 1))

    # Parse your ticket
    your_ticket = list(map(int, sections[1].splitlines()[1].split(",")))

    # Parse nearby tickets
    nearby_tickets = [
        list(map(int, line.split(","))) for line in sections[2].splitlines()[1:]
    ]

    return rules, your_ticket, nearby_tickets

def is_valid_value(value, rules):
    return any(value in r for ranges in rules.values() for r in ranges)

def find_invalid_values(ticket, rules):
    return [value for value in ticket if not is_valid_value(value, rules)]

def get_valid_tickets(tickets, rules):
    return [ticket for ticket in tickets if not find_invalid_values(ticket, rules)]

def determine_fields(valid_tickets, rules):
    positions = len(valid_tickets[0])
    possible_fields = {}
    
    # Find possible fields for each position
    for pos in range(positions):
        values = [ticket[pos] for ticket in valid_tickets]
        possible_fields[pos] = set()
        for field, ranges in rules.items():
            if all(any(v in r for r in ranges) for v in values):
                possible_fields[pos].add(field)
    
    # Eliminate fields until each position has one field
    field_mapping = {}
    while possible_fields:
        # Find position with only one possible field
        pos = min(possible_fields, key=lambda p: len(possible_fields[p]))
        field = possible_fields[pos].pop()
        field_mapping[pos] = field
        
        # Remove this field from all other positions
        for other_pos in possible_fields:
            possible_fields[other_pos].discard(field)
        
        del possible_fields[pos]
    
    return field_mapping

def part1(rules, nearby_tickets):
    return sum(sum(find_invalid_values(ticket, rules)) for ticket in nearby_tickets)

def part2(rules, your_ticket, nearby_tickets):
    valid_tickets = get_valid_tickets(nearby_tickets, rules)
    field_mapping = determine_fields(valid_tickets + [your_ticket], rules)
    
    departure_values = [
        your_ticket[pos]
        for pos, field in field_mapping.items()
        if field.startswith("departure")
    ]
    return prod(departure_values)

def main():
    rules, your_ticket, nearby_tickets = parse_input("2020/Day16/input.txt")
    print(f"Part 1: {part1(rules, nearby_tickets)}")
    print(f"Part 2: {part2(rules, your_ticket, nearby_tickets)}")

if __name__ == "__main__":
    main()