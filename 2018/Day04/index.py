import re
from collections import defaultdict
from datetime import datetime

def read_input(file_path):
    with open(file_path, 'r') as file:
        return sorted([line.strip() for line in file])

def parse_record(record):
    timestamp_str, action = re.match(r'\[(.*)\] (.*)', record).groups()
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M')
    return timestamp, action

def process_records(records):
    guards = defaultdict(lambda: defaultdict(int))
    guard_id = None
    sleep_start = None

    for record in records:
        timestamp, action = parse_record(record)
        if "begins shift" in action:
            guard_id = int(re.search(r'#(\d+)', action).group(1))
        elif "falls asleep" in action:
            sleep_start = timestamp
        elif "wakes up" in action:
            for minute in range(sleep_start.minute, timestamp.minute):
                guards[guard_id][minute] += 1

    return guards

def part1(guards):
    sleepiest_guard = max(guards, key=lambda guard: sum(guards[guard].values()))
    sleepiest_minute = max(guards[sleepiest_guard], key=guards[sleepiest_guard].get)
    return sleepiest_guard * sleepiest_minute

def part2(guards):
    guard_minute = max(((guard, minute) for guard in guards for minute in guards[guard]), key=lambda gm: guards[gm[0]][gm[1]])
    return guard_minute[0] * guard_minute[1]

if __name__ == "__main__":
    input_file = "2018/Day04/input.txt"
    records = read_input(input_file)
    guards = process_records(records)
    
    result_part1 = part1(guards)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(guards)
    print(f"Part 2: {result_part2}")