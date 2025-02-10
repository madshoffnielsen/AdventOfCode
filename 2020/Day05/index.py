def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]

def get_seat_id(boarding_pass):
    # Convert F/B to binary for row
    row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
    # Convert L/R to binary for column
    col = int(boarding_pass[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

def part1(boarding_passes):
    return max(get_seat_id(bp) for bp in boarding_passes)

def part2(boarding_passes):
    seat_ids = sorted(get_seat_id(bp) for bp in boarding_passes)
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] - seat_ids[i] == 2:
            return seat_ids[i] + 1
    return None

def main():
    boarding_passes = read_input("2020/Day05/input.txt")
    print(f"Part 1: {part1(boarding_passes)}")
    print(f"Part 2: {part2(boarding_passes)}")

if __name__ == "__main__":
    main()