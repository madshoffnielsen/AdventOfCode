def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return list(map(int, input_data.split(',')))

def calculate_minimum_fuel(positions):
    positions.sort()
    median = positions[len(positions) // 2]
    
    total_fuel = sum(abs(pos - median) for pos in positions)
    return total_fuel

def calculate_fuel_cost(positions, target):
    return sum((abs(pos - target) * (abs(pos - target) + 1)) // 2 for pos in positions)

def find_optimal_position(positions):
    min_pos = min(positions)
    max_pos = max(positions)
    
    left, right = min_pos, max_pos
    while left < right:
        mid = (left + right) // 2
        fuel_left = calculate_fuel_cost(positions, mid)
        fuel_right = calculate_fuel_cost(positions, mid + 1)
        
        if fuel_left < fuel_right:
            right = mid
        else:
            left = mid + 1
    
    return calculate_fuel_cost(positions, left)

def main():
    print("\n--- Day 7: The Treachery of Whales ---")
    input_file = '2021/input/day07.txt'
    positions = read_input(input_file)

    result = calculate_minimum_fuel(positions)
    print(f"Part 1: {result}.")

    result = find_optimal_position(positions)
    print(f"Part 2: {result}.")

if __name__ == "__main__":
    main()