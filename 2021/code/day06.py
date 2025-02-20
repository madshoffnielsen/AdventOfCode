def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return list(map(int, input_data.split(',')))

def simulate_lanternfish(initial_timers, days):
    fish_timers = [0] * 9
    
    for timer in initial_timers:
        fish_timers[timer] += 1
    
    for day in range(days):
        new_fish = fish_timers[0]
        
        for i in range(8):
            fish_timers[i] = fish_timers[i + 1]
        
        fish_timers[6] += new_fish
        fish_timers[8] = new_fish
    
    return sum(fish_timers)

def main():
    print("\n--- Day 6: Lanternfish ---")
    input_file = '2021/input/day06.txt'
    initial_timers = read_input(input_file)

    result = simulate_lanternfish(initial_timers, 80)
    print(f"Part 1: {result}")

    result = simulate_lanternfish(initial_timers, 256)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()