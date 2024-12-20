def memory_game(starting_numbers, nth_turn):
    # Dictionary to track the last turn a number was spoken
    last_seen = {num: idx + 1 for idx, num in enumerate(starting_numbers[:-1])}
    current = starting_numbers[-1]

    for turn in range(len(starting_numbers), nth_turn):
        if current in last_seen:
            next_num = turn - last_seen[current]
        else:
            next_num = 0

        # Update the last seen dictionary
        last_seen[current] = turn
        current = next_num

    return current


# Puzzle input
starting_numbers = [13, 0, 10, 12, 1, 5, 8]

# Part 1: Find the 2020th number spoken
result_part1 = memory_game(starting_numbers, 2020)
print(f"The 2020th number spoken is: {result_part1}")

# Part 2: Find the 30000000th number spoken
result_part2 = memory_game(starting_numbers, 30000000)
print(f"The 30000000th number spoken is: {result_part2}")
