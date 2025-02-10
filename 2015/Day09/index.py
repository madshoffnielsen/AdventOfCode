from itertools import permutations

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    distances = {}
    for line in lines:
        parts = line.strip().split()
        city1, city2 = parts[0], parts[2]
        distance = int(parts[4])
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        distances[city1][city2] = distance
        distances[city2][city1] = distance
    return distances

def calculate_route_distance(route, distances):
    return sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))

def find_shortest_and_longest_routes(distances):
    cities = list(distances.keys())
    shortest_route = float('inf')
    longest_route = 0
    
    for route in permutations(cities):
        distance = calculate_route_distance(route, distances)
        shortest_route = min(shortest_route, distance)
        longest_route = max(longest_route, distance)
    
    return shortest_route, longest_route

def main():
    distances = read_input("2015/Day09/input.txt")
    shortest_route, longest_route = find_shortest_and_longest_routes(distances)
    print(f"Part 1: {shortest_route}")
    print(f"Part 2: {longest_route}")

if __name__ == "__main__":
    main()