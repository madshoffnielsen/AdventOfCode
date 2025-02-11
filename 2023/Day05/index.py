def read_input(file_path):
    with open(file_path) as f:
        sections = f.read().strip().split('\n\n')
        seeds = [int(x) for x in sections[0].split(': ')[1].split()]
        maps = []
        for section in sections[1:]:
            ranges = []
            for line in section.splitlines()[1:]:
                dest, source, length = map(int, line.split())
                ranges.append((source, dest, length))
            maps.append(sorted(ranges))
        return seeds, maps

def map_number(number, ranges):
    for source, dest, length in ranges:
        if source <= number < source + length:
            return dest + (number - source)
    return number

def map_range(start, length, ranges):
    result = []
    current = start
    end = start + length
    
    ranges = sorted(ranges, key=lambda x: x[0])
    
    for source, dest, r_length in ranges:
        r_end = source + r_length
        
        # Handle gap before range
        if current < source:
            result.append((current, min(source, end) - current))
            current = source
            
        # Handle overlap with range
        if current < r_end and current >= source and current < end:
            overlap_end = min(r_end, end)
            mapped_start = dest + (current - source)
            result.append((mapped_start, overlap_end - current))
            current = overlap_end
            
        if current >= end:
            break
            
    # Handle remaining gap
    if current < end:
        result.append((current, end - current))
        
    return result

def part1(seeds, maps):
    locations = []
    for seed in seeds:
        value = seed
        for ranges in maps:
            value = map_number(value, ranges)
        locations.append(value)
    return min(locations)

def part2(seeds, maps):
    ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    
    for map_ranges in maps:
        new_ranges = []
        for start, length in ranges:
            new_ranges.extend(map_range(start, length, map_ranges))
        ranges = new_ranges
        
    return min(start for start, _ in ranges)

def main():
    seeds, maps = read_input("2023/Day05/input.txt")
    print(f"Part 1: {part1(seeds, maps)}")
    print(f"Part 2: {part2(seeds, maps)}")

if __name__ == "__main__":
    main()