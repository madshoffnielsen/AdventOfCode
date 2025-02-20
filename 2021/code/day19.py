from collections import defaultdict
from itertools import combinations

def rotations(beacon):
    x, y, z = beacon
    return [
        [ x,  y,  z], [ x,  z, -y], [ x, -y, -z], [ x, -z,  y],
        [-x, -y,  z], [-x, -z, -y], [-x,  y, -z], [-x,  z,  y],
        [ y, -x,  z], [ y,  z,  x], [ y,  x, -z], [ y, -z, -x],
        [-y,  x,  z], [-y, -z,  x], [-y, -x, -z], [-y,  z, -x],
        [ z,  y, -x], [ z,  x,  y], [ z, -y,  x], [ z, -x, -y],
        [-z, -y, -x], [-z, -x,  y], [-z,  y,  x], [-z,  x, -y]
    ]

def manhattan_distance(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

def read_scanners(filename):
    scanners = []
    with open(filename) as f:
        current_scanner = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('---'):
                if current_scanner:
                    scanners.append(current_scanner)
                current_scanner = []
            else:
                x, y, z = map(int, line.split(','))
                current_scanner.append((x, y, z))
        if current_scanner:
            scanners.append(current_scanner)
    return scanners

def find_scanner_positions(scanners):
    n = len(scanners)
    scanner_positions = [(0, 0, 0)]
    aligned_beacons = set(scanners[0])
    unaligned = set(range(1, n))
    
    while unaligned:
        for i in unaligned:
            found_match = False
            for rot_idx in range(24):
                rotated = [rotations(beacon)[rot_idx] for beacon in scanners[i]]
                offsets = defaultdict(int)
                
                for aligned in aligned_beacons:
                    for rotated_beacon in rotated:
                        offset = tuple(a - b for a, b in zip(aligned, rotated_beacon))
                        offsets[offset] += 1
                        
                        if offsets[offset] >= 12:
                            found_match = True
                            scanner_pos = offset
                            new_beacons = {tuple(b + o for b, o in zip(beacon, offset)) 
                                         for beacon in rotated}
                            aligned_beacons.update(new_beacons)
                            scanner_positions.append(scanner_pos)
                            break
                    
                    if found_match:
                        break
                        
                if found_match:
                    break
                    
            if found_match:
                unaligned.remove(i)
                break
    
    return aligned_beacons, scanner_positions

def solve(filename):
    scanners = read_scanners(filename)
    beacons, scanner_positions = find_scanner_positions(scanners)
    
    # Part 1: Number of beacons
    part1 = len(beacons)
    
    # Part 2: Maximum Manhattan distance between scanners
    part2 = max(manhattan_distance(a, b) 
               for a, b in combinations(scanner_positions, 2))
    
    return part1, part2

def main():
    print("\n--- Day 19: Beacon Scanner ---")
    filename = "2021/input/day19.txt"
    part1, part2 = solve(filename)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()