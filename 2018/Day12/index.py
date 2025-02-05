def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        initial_state = lines[0].strip().split(': ')[1]
        rules = {}
        for line in lines[2:]:
            pattern, result = line.strip().split(' => ')
            rules[pattern] = result
        return initial_state, rules

def get_next_state(current, rules, padding=4):
    # Add padding to handle edge cases
    state = '.' * padding + current + '.' * padding
    new_state = ''
    for i in range(2, len(state) - 2):
        pattern = state[i-2:i+3]
        new_state += rules.get(pattern, '.')
    return new_state

def calculate_sum(state, first_pot):
    return sum(i + first_pot for i, pot in enumerate(state) if pot == '#')

def part1(initial_state, rules, generations=20):
    state = initial_state
    first_pot = 0
    
    for _ in range(generations):
        new_state = get_next_state(state, rules)
        # Adjust first pot number based on padding
        first_pot -= 2
        # Trim leading/trailing dots
        while new_state.startswith('.'):
            new_state = new_state[1:]
            first_pot += 1
        while new_state.endswith('.'):
            new_state = new_state[:-1]
        state = new_state
        
    return calculate_sum(state, first_pot)

def part2(initial_state, rules, target=50000000000):
    state = initial_state
    first_pot = 0
    previous_sum = 0
    previous_diff = 0
    
    for gen in range(1000):  # Check for pattern in first 1000 generations
        new_state = get_next_state(state, rules)
        first_pot -= 2
        while new_state.startswith('.'):
            new_state = new_state[1:]
            first_pot += 1
        while new_state.endswith('.'):
            new_state = new_state[:-1]
        
        current_sum = calculate_sum(new_state, first_pot)
        current_diff = current_sum - previous_sum
        
        if current_diff == previous_diff:
            # Pattern found, calculate final sum
            remaining_gens = target - gen - 1
            return current_sum + (current_diff * remaining_gens)
            
        state = new_state
        previous_sum = current_sum
        previous_diff = current_diff
    
    return None

if __name__ == "__main__":
    input_file = "2018/Day12/input.txt"
    initial_state, rules = read_input(input_file)
    
    result_part1 = part1(initial_state, rules)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(initial_state, rules)
    print(f"Part 2: {result_part2}")