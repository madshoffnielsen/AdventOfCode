def play_memory_game(starting_numbers, target_turn):
    # Initialize last seen positions
    last_seen = {num: turn for turn, num in enumerate(starting_numbers[:-1], 1)}
    current = starting_numbers[-1]
    
    # Play game from starting position to target
    for turn in range(len(starting_numbers), target_turn):
        # Calculate next number
        next_num = 0 if current not in last_seen else turn - last_seen[current]
        
        # Update last seen and current number
        last_seen[current] = turn
        current = next_num
        
    return current

def main():
    starting_numbers = [13, 0, 10, 12, 1, 5, 8]
    print(f"Part 1: {play_memory_game(starting_numbers, 2020)}")
    print(f"Part 2: {play_memory_game(starting_numbers, 30000000)}")

if __name__ == "__main__":
    main()