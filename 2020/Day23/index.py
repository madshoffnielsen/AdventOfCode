def create_cups(numbers, extend_to=None):
    if extend_to:
        cups = list(numbers) + list(range(len(numbers) + 1, extend_to + 1))
    else:
        cups = list(numbers)
    
    # Create linked list using array
    next_cup = [0] * (len(cups) + 1)
    for i in range(len(cups)):
        next_cup[cups[i]] = cups[(i + 1) % len(cups)]
    return next_cup, cups[0]

def play_game(next_cup, current, moves):
    max_cup = len(next_cup) - 1
    
    for _ in range(moves):
        # Pick up three cups
        first = next_cup[current]
        second = next_cup[first]
        third = next_cup[second]
        next_cup[current] = next_cup[third]
        
        # Find destination
        destination = current - 1
        while destination < 1 or destination in (first, second, third):
            destination = max_cup if destination < 1 else destination - 1
        
        # Place picked up cups
        next_cup[third] = next_cup[destination]
        next_cup[destination] = first
        
        # Move to next cup
        current = next_cup[current]
    
    return next_cup

def get_result_part1(next_cup):
    result = []
    current = next_cup[1]
    while current != 1:
        result.append(str(current))
        current = next_cup[current]
    return ''.join(result)

def get_result_part2(next_cup):
    return next_cup[1] * next_cup[next_cup[1]]

def main():
    input_data = [int(x) for x in "135468729"]
    
    # Part 1
    next_cup, current = create_cups(input_data)
    final_state = play_game(next_cup, current, 100)
    print(f"Part 1: {get_result_part1(final_state)}")
    
    # Part 2
    next_cup, current = create_cups(input_data, 1_000_000)
    final_state = play_game(next_cup, current, 10_000_000)
    print(f"Part 2: {get_result_part2(final_state)}")

if __name__ == "__main__":
    main()