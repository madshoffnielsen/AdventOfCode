def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip()

def knot_hash_round(numbers, lengths, pos=0, skip=0):
    n = len(numbers)
    for length in lengths:
        if length > n:
            continue
            
        # Reverse the sublist
        start = pos
        sublist = []
        for i in range(length):
            sublist.append(numbers[(start + i) % n])
        sublist.reverse()
        
        for i in range(length):
            numbers[(start + i) % n] = sublist[i]
        
        # Move position and increase skip size
        pos = (pos + length + skip) % n
        skip += 1
    
    return pos, skip

def part1(input_str):
    numbers = list(range(256))
    lengths = [int(x) for x in input_str.split(',')]
    knot_hash_round(numbers, lengths)
    return numbers[0] * numbers[1]

def part2(input_str):
    # Convert input to ASCII codes and add standard suffix
    lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    pos = skip = 0
    
    # Run 64 rounds
    for _ in range(64):
        pos, skip = knot_hash_round(numbers, lengths, pos, skip)
    
    # Create dense hash
    dense_hash = []
    for i in range(0, 256, 16):
        result = numbers[i]
        for j in range(1, 16):
            result ^= numbers[i + j]
        dense_hash.append(result)
    
    # Convert to hex string
    return ''.join(f'{x:02x}' for x in dense_hash)

def main():
    input_str = read_input("2017/Day10/input.txt")
    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")

if __name__ == "__main__":
    main()