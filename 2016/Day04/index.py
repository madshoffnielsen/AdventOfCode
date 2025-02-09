import re
from collections import Counter

def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def extract_room_data(room):
    match = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)\]", room)
    name = match.group(1).replace('-', '')
    sector_id = int(match.group(2))
    checksum = match.group(3)
    return name, sector_id, checksum

def calculate_checksum(name):
    counts = Counter(name)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return ''.join([char for char, _ in sorted_counts[:5]])

def is_valid_room(name, checksum):
    return calculate_checksum(name) == checksum

def decrypt_name(name, sector_id):
    decrypted = []
    for char in name:
        if char == '-':
            decrypted.append(' ')
        else:
            decrypted.append(chr((ord(char) - ord('a') + sector_id) % 26 + ord('a')))
    return ''.join(decrypted)

def part1(rooms):
    total_sector_id = 0
    for room in rooms:
        name, sector_id, checksum = extract_room_data(room)
        if is_valid_room(name, checksum):
            total_sector_id += sector_id
    return total_sector_id

def part2(rooms):
    for room in rooms:
        name, sector_id, checksum = extract_room_data(room)
        if is_valid_room(name, checksum):
            decrypted_name = decrypt_name(room, sector_id)
            if "northpole object storage" in decrypted_name:
                return sector_id
    return None

if __name__ == "__main__":
    rooms = parse_input("2016/Day04/input.txt")
    print("Part 1:", part1(rooms))
    print("Part 2:", part2(rooms))