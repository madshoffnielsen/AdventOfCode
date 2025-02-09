def parse_input(file_path):
    ranges = []
    with open(file_path) as f:
        for line in f:
            start, end = map(int, line.strip().split('-'))
            ranges.append((start, end))
    return sorted(ranges)

def merge_ranges(ranges):
    merged = []
    current_start, current_end = ranges[0]
    
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged.append((current_start, current_end))
    return merged

def find_lowest_allowed(ranges):
    merged = merge_ranges(ranges)
    if merged[0][0] > 0:
        return 0
    return merged[0][1] + 1

def count_allowed_ips(ranges):
    merged = merge_ranges(ranges)
    count = 0
    
    # Add gap between 0 and first range if exists
    if merged[0][0] > 0:
        count += merged[0][0]
        
    # Add gaps between ranges
    for i in range(len(merged) - 1):
        count += merged[i + 1][0] - merged[i][1] - 1
        
    # Add gap after last range if exists
    if merged[-1][1] < 4294967295:
        count += 4294967295 - merged[-1][1]
        
    return count

def part1(ranges):
    return find_lowest_allowed(ranges)

def part2(ranges):
    return count_allowed_ips(ranges)

if __name__ == "__main__":
    ranges = parse_input("2016/Day20/input.txt")
    print("Part 1:", part1(ranges))
    print("Part 2:", part2(ranges))