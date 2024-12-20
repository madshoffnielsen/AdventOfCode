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
    """Check if a value is valid for any rule."""
    return any(value in r for ranges in rules.values() for r in ranges)


def discard_invalid_tickets(tickets, rules):
    """Discard tickets with invalid values."""
    valid_tickets = []
    for ticket in tickets:
        if all(is_valid_value(value, rules) for value in ticket):
            valid_tickets.append(ticket)
    return valid_tickets


def identify_fields(valid_tickets, rules):
    """Determine which field corresponds to each column."""
    field_possibilities = {field: set(range(len(valid_tickets[0]))) for field in rules}

    for ticket in valid_tickets:
        for idx, value in enumerate(ticket):
            for field, ranges in rules.items():
                if not any(value in r for r in ranges):
                    field_possibilities[field].discard(idx)

    # Resolve fields with only one possibility iteratively
    resolved_fields = {}
    while field_possibilities:
        for field, positions in field_possibilities.items():
            if len(positions) == 1:
                resolved_pos = positions.pop()
                resolved_fields[field] = resolved_pos
                del field_possibilities[field]
                for other_positions in field_possibilities.values():
                    other_positions.discard(resolved_pos)
                break

    return resolved_fields


def solve(filename):
    rules, your_ticket, nearby_tickets = parse_input(filename)

    # Part 1: Sum of invalid values
    invalid_sum = sum(
        value
        for ticket in nearby_tickets
        for value in ticket
        if not is_valid_value(value, rules)
    )

    # Part 2: Discard invalid tickets and identify fields
    valid_tickets = discard_invalid_tickets(nearby_tickets, rules)
    resolved_fields = identify_fields(valid_tickets, rules)

    # Calculate the product of "departure" fields in your ticket
    departure_product = prod(
        your_ticket[idx]
        for field, idx in resolved_fields.items()
        if field.startswith("departure")
    )

    return invalid_sum, departure_product


# Run the solution
filename = "2020/Day16/input.txt"
part1, part2 = solve(filename)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
