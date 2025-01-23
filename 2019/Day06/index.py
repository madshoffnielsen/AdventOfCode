def build_orbit_map(orbit_data):
    orbit_map = {}
    for orbit in orbit_data:
        center, orbiter = orbit.split(')')
        orbit_map[orbiter] = center
    return orbit_map

def count_orbits(orbit_map):
    total_orbits = 0
    for orbiter in orbit_map:
        current = orbiter
        while current in orbit_map:
            total_orbits += 1
            current = orbit_map[current]
    return total_orbits

def find_orbital_transfers(orbit_map, start, end):
    start_path = []
    end_path = []
    
    current = start
    while current in orbit_map:
        current = orbit_map[current]
        start_path.append(current)
    
    current = end
    while current in orbit_map:
        current = orbit_map[current]
        end_path.append(current)
    
    # Find the common ancestor
    common_ancestor = next(obj for obj in start_path if obj in end_path)
    
    # Calculate the number of transfers
    return start_path.index(common_ancestor) + end_path.index(common_ancestor)

# Read input from input.txt
with open('2019/Day06/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

# Build the orbit map
orbit_map = build_orbit_map(input_data)

# Part 1: Count the total number of direct and indirect orbits
total_orbits = count_orbits(orbit_map)
print("Total number of direct and indirect orbits (Part 1):", total_orbits)

# Part 2: Find the minimum number of orbital transfers
orbital_transfers = find_orbital_transfers(orbit_map, 'YOU', 'SAN')
print("Minimum number of orbital transfers (Part 2):", orbital_transfers)