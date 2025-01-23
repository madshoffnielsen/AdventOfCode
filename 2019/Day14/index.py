import math
from collections import defaultdict, deque

def parse_input(input_data):
    reactions = {}
    for line in input_data.strip().split('\n'):
        inputs, output = line.split(' => ')
        output_qty, output_chem = output.split(' ')
        inputs = [input.split(' ') for input in inputs.split(', ')]
        reactions[output_chem] = (int(output_qty), [(int(qty), chem) for qty, chem in inputs])
    return reactions

def ore_needed_for_fuel(reactions, fuel_amount):
    needs = defaultdict(int, {'FUEL': fuel_amount})
    leftovers = defaultdict(int)
    ore_needed = 0

    while needs:
        chem, qty_needed = needs.popitem()
        if chem == 'ORE':
            ore_needed += qty_needed
            continue

        qty_produced, inputs = reactions[chem]
        qty_needed -= leftovers[chem]
        batches = math.ceil(qty_needed / qty_produced)
        leftovers[chem] = batches * qty_produced - qty_needed

        for input_qty, input_chem in inputs:
            needs[input_chem] += input_qty * batches

    return ore_needed

def max_fuel_for_ore(reactions, ore_amount):
    low, high = 1, ore_amount
    while low < high:
        mid = (low + high + 1) // 2
        if ore_needed_for_fuel(reactions, mid) <= ore_amount:
            low = mid
        else:
            high = mid - 1
    return low

# Read input
with open('2019/Day14/input.txt', 'r') as file:
    input_data = file.read().strip()

# Parse reactions
reactions = parse_input(input_data)

# Part 1: Calculate ore needed for 1 fuel
ore_for_one_fuel = ore_needed_for_fuel(reactions, 1)
print(f"Part 1: Ore needed for 1 fuel: {ore_for_one_fuel}")

# Part 2: Calculate maximum fuel for given ore
total_ore = 1000000000000
max_fuel = max_fuel_for_ore(reactions, total_ore)
print(f"Part 2: Maximum fuel for {total_ore} ore: {max_fuel}")