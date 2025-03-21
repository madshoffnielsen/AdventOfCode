import numpy as np

ROCKS = [
    np.array([2, 3, 4, 5]),
    np.array([3, 9, 10, 11, 17]),
    np.array([2, 3, 4, 11, 18]),
    np.array([2, 9, 16, 23]),
    np.array([2, 3, 9, 10])
]

def rock_fall(input_data, count=2022):
    i = 0
    j = 0
    visited = {}
    blocked = set([0, 1, 2, 3, 4, 5, 6])
    highest = 0

    outcomes = []

    while count > 0:
        count -= 1
        rock = ROCKS[i] + (highest + 4) * 7
        while True:
            if input_data[j] == '<':
                if all(v % 7 != 0 and v - 1 not in blocked for v in rock):
                    rock -= 1
            else:
                if all(v % 7 != 6 and v + 1 not in blocked for v in rock):
                    rock += 1

            j = (j + 1) % len(input_data)

            if all(v - 7 not in blocked for v in rock):
                rock -= 7
            else:
                blocked.update(rock)
                high = max(v // 7 for v in rock)
                increase = max(0, high - highest)
                outcomes.append(increase)
                highest += increase
                state = j * len(ROCKS) + i
                if state in visited:
                    past_visits = visited[state]
                    past_visits.append(len(outcomes) - 1)
                    cycle_length = find_pattern(past_visits, outcomes)
                    if cycle_length:
                        q = count // cycle_length
                        r = count % cycle_length
                        return (
                            highest +
                            q * sum(outcomes[-cycle_length:]) +
                            sum(outcomes[-cycle_length:-cycle_length + r])
                        )
                else:
                    visited[state] = [len(outcomes) - 1]
                break

        i = (i + 1) % len(ROCKS)

    return highest

def find_pattern(past_visits, outcomes):
    last_index = past_visits[-1]
    for i in range(len(past_visits) - 1):
        test_index = past_visits[i]
        cycle_length = last_index - test_index
        if test_index + 1 < cycle_length:
            continue
        if all(outcomes[last_index - j] == outcomes[test_index - j] for j in range(cycle_length)):
            return cycle_length
    return 0

def main():
    print("\n--- Day 17: Pyroclastic Flow ---")
    with open("2022/input/day17.txt", "r") as f:
        input_data = f.read().strip()

    # Part 1
    part1_result = rock_fall(input_data)
    print(f"Part 1: {part1_result}")

    # Part 2
    part2_result = rock_fall(input_data, 1000000000000)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()