from functools import cache

def read_input(file_path):
    with open(file_path) as f:
        rows = []
        for line in f:
            pattern, groups = line.strip().split()
            groups = tuple(map(int, groups.split(',')))
            rows.append((pattern, groups))
        return rows

@cache
def count_arrangements(pattern, groups, pos=0, group_idx=0, current_group=0):
    # Base case: reached end of pattern
    if pos == len(pattern):
        if group_idx == len(groups) and current_group == 0:
            return 1
        if group_idx == len(groups) - 1 and groups[group_idx] == current_group:
            return 1
        return 0

    result = 0
    possible_chars = ['.', '#'] if pattern[pos] == '?' else [pattern[pos]]

    for char in possible_chars:
        if char == '#':
            # Continue or start damaged spring group
            result += count_arrangements(pattern, groups, pos + 1, 
                                      group_idx, current_group + 1)
        else:  # char == '.'
            if current_group == 0:
                # Continue operational springs
                result += count_arrangements(pattern, groups, pos + 1, 
                                          group_idx, 0)
            elif group_idx < len(groups) and groups[group_idx] == current_group:
                # End current group and start new
                result += count_arrangements(pattern, groups, pos + 1, 
                                          group_idx + 1, 0)

    return result

def unfold_pattern(pattern, groups):
    pattern = '?'.join([pattern] * 5)
    groups = groups * 5
    return pattern, groups

def part1(rows):
    return sum(count_arrangements(p, g) for p, g in rows)

def part2(rows):
    unfolded = [unfold_pattern(p, g) for p, g in rows]
    return sum(count_arrangements(p, g) for p, g in unfolded)

def main():
    rows = read_input("2023/Day12/input.txt")
    print(f"Part 1: {part1(rows)}")
    print(f"Part 2: {part2(rows)}")

if __name__ == "__main__":
    main()