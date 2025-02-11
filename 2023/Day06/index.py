from math import ceil, floor, sqrt
from functools import reduce

def read_input(file_path):
    with open(file_path) as f:
        times = [int(x) for x in f.readline().split(':')[1].split()]
        distances = [int(x) for x in f.readline().split(':')[1].split()]
        return times, distances

def count_ways_to_win(time, distance):
    # Need to beat distance, not equal it
    a = -1
    b = time
    c = -(distance + 1)  # Add 1 to ensure we beat the record
    
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0
        
    x1 = (-b + sqrt(discriminant)) / (2*a)
    x2 = (-b - sqrt(discriminant)) / (2*a)
    
    # Round appropriately for integer solutions
    return floor(x2) - ceil(x1) + 1

def part1(times, distances):
    return reduce(lambda x, y: x * y, 
                 [count_ways_to_win(t, d) for t, d in zip(times, distances)])

def part2(times, distances):
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))
    return count_ways_to_win(time, distance)

def main():
    times, distances = read_input("2023/Day06/input.txt")
    print(f"Part 1: {part1(times, distances)}")
    print(f"Part 2: {part2(times, distances)}")

if __name__ == "__main__":
    main()