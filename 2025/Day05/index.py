from typing import List, Tuple

def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f]

def parse_input(lines: List[str]) -> Tuple[List[Tuple[int, int]], List[int]]:
    ranges = []
    ids = []
    in_ranges = True
    for line in lines:
        if line == '':
            in_ranges = False
            continue
        if in_ranges:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            ids.append(int(line))
    return ranges, ids

def is_fresh(id: int, ranges: List[Tuple[int, int]]) -> bool:
    return any(start <= id <= end for start, end in ranges)

def part1(ranges: List[Tuple[int, int]], ids: List[int]) -> int:
    return sum(1 for id in ids if is_fresh(id, ranges))

def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not ranges:
        return []
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged

def part2(ranges: List[Tuple[int, int]]) -> int:
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)

def main() -> None:
    lines = read_input("2025/Day05/input.txt")
    ranges, ids = parse_input(lines)
    print("Part 1:", part1(ranges, ids))
    print("Part 2:", part2(ranges))

if __name__ == "__main__":
    main()