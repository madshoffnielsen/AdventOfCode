import functools

def parse_input(filename):
    """Reads input file and returns pairs of packets."""
    with open(filename, 'r') as f:
        data = f.read().strip().split("\n\n")
    return [list(map(eval, pair.split("\n"))) for pair in data]

def compare_packets(left, right):
    """Custom recursive comparison function for packets."""
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)  # Returns -1, 0, or 1
    
    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            cmp = compare_packets(l, r)
            if cmp != 0:
                return cmp
        return (len(left) > len(right)) - (len(left) < len(right))
    
    # Convert single integer to list for comparison
    if isinstance(left, int):
        return compare_packets([left], right)
    if isinstance(right, int):
        return compare_packets(left, [right])

def part1(packets):
    """Computes sum of indices of correctly ordered pairs."""
    return sum(i + 1 for i, (left, right) in enumerate(packets) if compare_packets(left, right) == -1)

def part2(packets):
    """Finds decoder key by sorting all packets including divider packets [[2]] and [[6]]."""
    all_packets = [packet for pair in packets for packet in pair]  # Flatten pairs
    all_packets.extend([[[2]], [[6]]])  # Add divider packets
    
    all_packets.sort(key=functools.cmp_to_key(compare_packets))  # Sort using custom compare function
    
    index_2 = all_packets.index([[2]]) + 1
    index_6 = all_packets.index([[6]]) + 1
    
    return index_2 * index_6  # Compute decoder key

if __name__ == "__main__":
    print("\n--- Day 13: Distress Signal ---")
    packets = parse_input("2022/input/day13.txt")
    
    # Part 1
    print("Part 1:", part1(packets))
    
    # Part 2
    print("Part 2:", part2(packets))
