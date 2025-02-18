def is_safe_report(levels):
    is_increasing = True
    is_decreasing = True

    for i in range(len(levels) - 1):
        difference = levels[i + 1] - levels[i]

        # Check if the difference is between 1 and 3
        if abs(difference) < 1 or abs(difference) > 3:
            return False

        # Determine if the report is consistently increasing or decreasing
        if difference < 0:
            is_increasing = False
        elif difference > 0:
            is_decreasing = False

    # A report is safe if it is either strictly increasing or strictly decreasing
    return is_increasing or is_decreasing

def count_safe_reports(filename):
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))

            if is_safe_report(levels):
                safe_count += 1

    return safe_count

def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]

        if is_safe_report(modified_levels):
            return True

    return False

def count_safe_reports_with_dampener(filename):
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))

            if is_safe_with_dampener(levels):
                safe_count += 1

    return safe_count

def main():
    filename = "2024/Day02/input.txt"

    safe_reports = count_safe_reports(filename)
    print(f"Part 1: {safe_reports}")

    safe_reports_with_dampener = count_safe_reports_with_dampener(filename)
    print(f"Part 2: {safe_reports_with_dampener}")

if __name__ == "__main__":
    main()