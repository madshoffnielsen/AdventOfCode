def solve_virus_problem(grid, bursts=10000):
    # Initialize the grid state as a dictionary, with default clean ('.')
    infected_nodes = {}
    
    # Fill the dictionary with the initial grid state
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                infected_nodes[(x, y)] = True
    
    # Start position (middle of the grid)
    x, y = len(grid[0]) // 2, len(grid) // 2
    # Initial direction is facing 'up'
    directions = ['up', 'right', 'down', 'left']
    dir_index = 0  # 'up' is at index 0
    
    # Count the number of infections
    infection_count = 0
    
    for _ in range(bursts):
        current_node = (x, y)
        
        # Check if the current node is infected or clean
        if current_node in infected_nodes:
            # Node is infected: Turn right and clean it
            dir_index = (dir_index + 1) % 4
            del infected_nodes[current_node]
        else:
            # Node is clean: Turn left and infect it
            dir_index = (dir_index - 1) % 4
            infected_nodes[current_node] = True
            infection_count += 1
        
        # Move the virus carrier one step in the direction it is facing
        if directions[dir_index] == 'up':
            y -= 1
        elif directions[dir_index] == 'right':
            x += 1
        elif directions[dir_index] == 'down':
            y += 1
        elif directions[dir_index] == 'left':
            x -= 1
    
    return infection_count

def solve_virus_problem_part2(grid, bursts=10000000):
    # Initialize the grid state as a dictionary with node states: clean (.), weakened (W), infected (#), flagged (F)
    node_states = {}
    
    # Fill the dictionary with the initial grid state (clean nodes are '.' by default)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            node_states[(x, y)] = cell
    
    # Start position (middle of the grid)
    x, y = len(grid[0]) // 2, len(grid) // 2
    # Initial direction is facing 'up'
    directions = ['up', 'right', 'down', 'left']
    dir_index = 0  # 'up' is at index 0
    
    # Count the number of infections
    infection_count = 0
    
    for _ in range(bursts):
        current_node = (x, y)
        current_state = node_states.get(current_node, '.')
        
        # Decide the behavior based on the current node's state
        if current_state == '.':
            # Clean node: Turn left, weaken the node
            dir_index = (dir_index - 1) % 4
            node_states[current_node] = 'W'  # Change state to weakened
        elif current_state == 'W':
            # Weakened node: No turn, infect the node
            node_states[current_node] = '#'  # Change state to infected
            infection_count += 1
        elif current_state == '#':
            # Infected node: Turn right, flag the node
            dir_index = (dir_index + 1) % 4
            node_states[current_node] = 'F'  # Change state to flagged
        elif current_state == 'F':
            # Flagged node: Reverse direction, clean the node
            dir_index = (dir_index + 2) % 4  # Reverse direction
            node_states[current_node] = '.'  # Change state to clean
        
        # Move the virus carrier one step in the direction it is facing
        if directions[dir_index] == 'up':
            y -= 1
        elif directions[dir_index] == 'right':
            x += 1
        elif directions[dir_index] == 'down':
            y += 1
        elif directions[dir_index] == 'left':
            x -= 1
    
    return infection_count

# Read input from the file
with open('2017/Day22/input.txt') as file:
    grid = [line.strip() for line in file.readlines()]

# Solve the problem for 10000 bursts
result = solve_virus_problem(grid, bursts=10000)
print("Part 1:", result)

# Solve the problem for 10,000,000 bursts (Part 2)
result = solve_virus_problem_part2(grid, bursts=10000000)
print("Part 2:", result)
