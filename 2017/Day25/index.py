import re
from collections import defaultdict

def parse_input(filename):
    """Parses the Turing Machine input instructions."""
    with open(filename) as f:
        lines = f.read().split("\n")

    # Extract initial state and steps count
    initial_state = re.search(r"Begin in state ([A-Z]).", lines[0]).group(1)
    steps = int(re.search(r"Perform a diagnostic checksum after (\d+) steps.", lines[1]).group(1))

    # Extract state transitions
    states = {}
    i = 3
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue

        state_name = re.search(r"In state ([A-Z]):", lines[i]).group(1)
        states[state_name] = {}

        for j in range(2):
            i += 1
            write_value = int(re.search(r"- Write the value (\d+).", lines[i + 1]).group(1))
            move_dir = 1 if "right" in lines[i + 2] else -1
            next_state = re.search(r"- Continue with state ([A-Z]).", lines[i + 3]).group(1)

            read_value = int(re.search(r"If the current value is (\d+):", lines[i]).group(1))
            states[state_name][read_value] = (write_value, move_dir, next_state)

            i += 3

        i += 1

    return initial_state, steps, states

def run_turing_machine(initial_state, steps, states):
    """Simulates the Turing Machine."""
    tape = defaultdict(int)
    cursor = 0
    state = initial_state

    for _ in range(steps):
        write_value, move_dir, next_state = states[state][tape[cursor]]
        tape[cursor] = write_value
        cursor += move_dir
        state = next_state

    return sum(tape.values())  # Count the number of 1s

def solve_day25(filename):
    """Solves both parts of the puzzle."""
    initial_state, steps, states = parse_input(filename)
    return run_turing_machine(initial_state, steps, states)

if __name__ == "__main__":
    input_file = "2017/Day25/input.txt"
    result = solve_day25(input_file)
    print("Part 1: Diagnostic checksum =", result)
