import re

def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def has_abba(sequence):
    for i in range(len(sequence) - 3):
        if sequence[i] != sequence[i+1] and sequence[i:i+2] == sequence[i+3:i+1:-1]:
            return True
    return False

def supports_tls(ip):
    parts = re.split(r'\[|\]', ip)
    outside_brackets = parts[::2]
    inside_brackets = parts[1::2]
    
    return any(has_abba(part) for part in outside_brackets) and not any(has_abba(part) for part in inside_brackets)

def get_aba_sequences(sequence):
    return [sequence[i:i+3] for i in range(len(sequence) - 2) if sequence[i] == sequence[i+2] != sequence[i+1]]

def supports_ssl(ip):
    parts = re.split(r'\[|\]', ip)
    outside_brackets = parts[::2]
    inside_brackets = parts[1::2]
    
    for part in outside_brackets:
        for aba in get_aba_sequences(part):
            bab = aba[1] + aba[0] + aba[1]
            if any(bab in inside_part for inside_part in inside_brackets):
                return True
    return False

def part1(ips):
    return sum(1 for ip in ips if supports_tls(ip))

def part2(ips):
    return sum(1 for ip in ips if supports_ssl(ip))

if __name__ == "__main__":
    ips = parse_input("2016/Day07/input.txt")
    print("Part 1:", part1(ips))
    print("Part 2:", part2(ips))