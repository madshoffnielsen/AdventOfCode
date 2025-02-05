import re
from collections import defaultdict, deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def parse_instructions(instructions):
    dependencies = defaultdict(set)
    all_steps = set()
    for instruction in instructions:
        match = re.match(r'Step (\w) must be finished before step (\w) can begin.', instruction)
        if match:
            before, after = match.groups()
            dependencies[after].add(before)
            all_steps.update([before, after])
    return dependencies, all_steps

def part1(dependencies, all_steps):
    order = []
    available_steps = deque(sorted(step for step in all_steps if step not in dependencies))

    while available_steps:
        current_step = available_steps.popleft()
        order.append(current_step)
        for step in list(dependencies.keys()):
            dependencies[step].discard(current_step)
            if not dependencies[step]:
                available_steps.append(step)
                del dependencies[step]
        available_steps = deque(sorted(available_steps))

    return ''.join(order)

def part2(dependencies, all_steps, num_workers=5, base_duration=60):
    time = 0
    workers = [0] * num_workers
    in_progress = [None] * num_workers
    available_steps = deque(sorted(step for step in all_steps if step not in dependencies))
    completed_steps = set()

    def step_duration(step):
        return base_duration + ord(step) - ord('A') + 1

    while available_steps or any(workers) or any(in_progress):
        for i in range(num_workers):
            if workers[i] == 0 and in_progress[i]:
                completed_steps.add(in_progress[i])
                for step in list(dependencies.keys()):
                    dependencies[step].discard(in_progress[i])
                    if not dependencies[step]:
                        available_steps.append(step)
                        del dependencies[step]
                in_progress[i] = None

        available_steps = deque(sorted(available_steps))

        for i in range(num_workers):
            if workers[i] == 0 and available_steps:
                next_step = available_steps.popleft()
                in_progress[i] = next_step
                workers[i] = step_duration(next_step)

        time += 1
        workers = [max(0, w - 1) for w in workers]

    return time - 1  # Adjust for the final increment after all tasks are completed

if __name__ == "__main__":
    input_file = "2018/Day07/input.txt"
    instructions = read_input(input_file)
    dependencies, all_steps = parse_instructions(instructions)
    
    result_part1 = part1(dependencies, all_steps)
    print(f"Part 1: {result_part1}")
    
    dependencies, all_steps = parse_instructions(instructions)  # Re-parse to reset state
    result_part2 = part2(dependencies, all_steps)
    print(f"Part 2: {result_part2}")