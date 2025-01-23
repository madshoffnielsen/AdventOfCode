import re
from math import gcd
from itertools import combinations
from functools import reduce

def parse_input(input_data):
    positions = []
    for line in input_data.strip().split('\n'):
        x, y, z = map(int, re.findall(r'-?\d+', line))
        positions.append([x, y, z])
    return positions

def apply_gravity(positions, velocities):
    for (i, j) in combinations(range(len(positions)), 2):
        for axis in range(3):
            if positions[i][axis] < positions[j][axis]:
                velocities[i][axis] += 1
                velocities[j][axis] -= 1
            elif positions[i][axis] > positions[j][axis]:
                velocities[i][axis] -= 1
                velocities[j][axis] += 1

def apply_velocity(positions, velocities):
    for i in range(len(positions)):
        for axis in range(3):
            positions[i][axis] += velocities[i][axis]

def total_energy(positions, velocities):
    energy = 0
    for pos, vel in zip(positions, velocities):
        potential = sum(abs(x) for x in pos)
        kinetic = sum(abs(x) for x in vel)
        energy += potential * kinetic
    return energy

def find_cycle_length(positions):
    initial_positions = [pos[:] for pos in positions]
    velocities = [[0, 0, 0] for _ in positions]
    steps = 0
    cycle_lengths = [0, 0, 0]

    while not all(cycle_lengths):
        apply_gravity(positions, velocities)
        apply_velocity(positions, velocities)
        steps += 1

        for axis in range(3):
            if cycle_lengths[axis] == 0:
                if all(positions[i][axis] == initial_positions[i][axis] and velocities[i][axis] == 0 for i in range(len(positions))):
                    cycle_lengths[axis] = steps

    return reduce(lambda x, y: x * y // gcd(x, y), cycle_lengths)

# Read input
with open('2019/Day12/input.txt', 'r') as file:
    input_data = file.read().strip()

# Parse initial positions
positions = parse_input(input_data)

# Part 1: Simulate motion for 1000 steps
velocities = [[0, 0, 0] for _ in positions]
for _ in range(1000):
    apply_gravity(positions, velocities)
    apply_velocity(positions, velocities)

energy = total_energy(positions, velocities)
print(f"Part 1: Total energy after 1000 steps: {energy}")

# Part 2: Find the first time all moons' positions and velocities repeat
positions = parse_input(input_data)  # Reset positions
cycle_length = find_cycle_length(positions)
print(f"Part 2: First time all moons' positions and velocities repeat: {cycle_length}")