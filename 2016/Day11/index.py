import re
from collections import deque

def parse_input(file_path):
    floors = []
    with open(file_path) as f:
        for line in f:
            items = re.findall(r'(\w+ generator|\w+-compatible microchip)', line)
            floors.append(set(items))
    return floors

def is_valid(floors):
    for floor in floors:
        generators = {item.split()[0] for item in floor if 'generator' in item}
        chips = {item.split('-')[0] for item in floor if 'microchip' in item}
        if generators and chips - generators:
            return False
    return True

def get_neighbors(state):
    floors, elevator = state
    current_floor = floors[elevator]
    items = list(current_floor)
    neighbors = []

    for i in range(len(items)):
        for j in range(i, len(items)):
            for direction in [-1, 1]:
                new_elevator = elevator + direction
                if 0 <= new_elevator < len(floors):
                    new_floors = [set(floor) for floor in floors]  # Convert frozensets to sets
                    new_floors[elevator].remove(items[i])
                    if i != j:
                        new_floors[elevator].remove(items[j])
                    new_floors[new_elevator].add(items[i])
                    if i != j:
                        new_floors[new_elevator].add(items[j])
                    if is_valid(new_floors):
                        neighbors.append((tuple(map(frozenset, new_floors)), new_elevator))  # Convert back to frozensets
    return neighbors

def canonicalize_state(state):
    floors, elevator = state
    item_map = {}
    item_id = 0
    new_floors = []

    for floor in floors:
        new_floor = set()
        for item in floor:
            item_type = 'generator' if 'generator' in item else 'microchip'
            element = item.split()[0] if item_type == 'generator' else item.split('-')[0]

            if element not in item_map:
                item_map[element] = chr(ord('A') + item_id)
                item_id += 1

            new_item = f"{item_map[element]} {item_type}" if item_type == 'generator' else f"{item_map[element]}-{item_type}"
            new_floor.add(new_item)
        new_floors.append(frozenset(new_floor))

    return (tuple(new_floors), elevator)

def bfs(initial_state):
    queue = deque([(initial_state, 0)])
    visited = set()
    visited.add(canonicalize_state(initial_state))

    while queue:
        state, steps = queue.popleft()
        floors, elevator = state

        if all(len(floor) == 0 for floor in floors[:-1]):
            return steps

        for neighbor in get_neighbors(state):
            canonical_neighbor = canonicalize_state(neighbor)
            if canonical_neighbor not in visited:
                visited.add(canonical_neighbor)
                queue.append((neighbor, steps + 1))

    return -1

def part1(floors):
    initial_state = (tuple(map(frozenset, floors)), 0)
    return bfs(initial_state)

def part2(floors):
    floors[0].update([
        'elerium generator', 'elerium-compatible microchip',
        'dilithium generator', 'dilithium-compatible microchip'
    ])
    initial_state = (tuple(map(frozenset, floors)), 0)
    return bfs(initial_state)

if __name__ == "__main__":
    floors = parse_input("2016/Day11/input.txt")
    print("Part 1:", part1(floors))
    print("Part 2:", part2(floors))