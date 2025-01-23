def calculate_fuel(mass):
    return mass // 3 - 2

def calculate_total_fuel(mass):
    total_fuel = 0
    while mass > 0:
        fuel = calculate_fuel(mass)
        if fuel > 0:
            total_fuel += fuel
        mass = fuel
    return total_fuel

def total_fuel_requirement(masses, part):
    if part == 1:
        return sum(calculate_fuel(mass) for mass in masses)
    elif part == 2:
        return sum(calculate_total_fuel(mass) for mass in masses)

# Read input from input.txt
with open('2019/Day01/input.txt', 'r') as file:
    input_data = file.readlines()

# Convert input data to a list of integers
masses = [int(line.strip()) for line in input_data]

# Calculate total fuel requirement for Part 1
total_fuel_part1 = total_fuel_requirement(masses, part=1)
print("Total fuel requirement for Part 1:", total_fuel_part1)

# Calculate total fuel requirement for Part 2
total_fuel_part2 = total_fuel_requirement(masses, part=2)
print("Total fuel requirement for Part 2:", total_fuel_part2)