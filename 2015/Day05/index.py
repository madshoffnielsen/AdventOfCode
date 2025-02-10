def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def is_nice_part1(s):
    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]
    
    # Rule 1: At least three vowels
    if sum(1 for char in s if char in vowels) < 3:
        return False
    
    # Rule 2: At least one letter appears twice in a row
    if not any(s[i] == s[i+1] for i in range(len(s) - 1)):
        return False
    
    # Rule 3: Does not contain the strings "ab", "cd", "pq", or "xy"
    if any(f in s for f in forbidden):
        return False
    
    return True

def is_nice_part2(s):
    # Rule 1: A pair of any two letters that appears at least twice without overlapping
    if not any(s[i:i+2] in s[i+2:] for i in range(len(s) - 1)):
        return False
    
    # Rule 2: At least one letter which repeats with exactly one letter between them
    if not any(s[i] == s[i+2] for i in range(len(s) - 2)):
        return False
    
    return True

def part1(strings):
    return sum(1 for s in strings if is_nice_part1(s))

def part2(strings):
    return sum(1 for s in strings if is_nice_part2(s))

def main():
    strings = read_input("2015/Day05/input.txt")
    print(f"Part 1: {part1(strings)}")
    print(f"Part 2: {part2(strings)}")

if __name__ == "__main__":
    main()