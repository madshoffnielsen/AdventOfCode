import re
from itertools import combinations

def read_input(file_path):
    """Reads and parses the input file."""
    with open(file_path, "r") as f:
        return f.read().strip()

def parse_input(input_data):
    """Parses the input data and computes shortest paths using Floyd-Warshall."""
    valves = {}
    distances = {}
    
    for line in input_data.strip().split("\n"):
        parts = re.findall(r"[A-Z]{2}|\d+", line)
        valve = parts[0]
        flow_rate = int(parts[1])
        neighbors = parts[2:]
        valves[valve] = (flow_rate, neighbors)
    
    # Initialize distances
    for valve in valves:
        distances[valve] = {}
        for neighbor in valves:
            distances[valve][neighbor] = float('inf')
        distances[valve][valve] = 0
        for neighbor in valves[valve][1]:
            distances[valve][neighbor] = 1
    
    # Compute shortest paths using Floyd-Warshall
    for k in valves:
        for i in valves:
            for j in valves:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    return valves, distances

def find_max_pressure(valves, distances, time_limit):
    """DFS search to maximize pressure release within the time limit."""
    def dfs(valve, time_remaining, visited, pressure):
        max_pressure = pressure
        for next_valve in valves:
            if next_valve not in visited and valves[next_valve][0] > 0:
                travel_time = distances[valve][next_valve] + 1
                if time_remaining >= travel_time:
                    max_pressure = max(
                        max_pressure,
                        dfs(next_valve, time_remaining - travel_time, visited | {next_valve},
                            pressure + valves[next_valve][0] * (time_remaining - travel_time))
                    )
        return max_pressure
    
    return dfs("AA", time_limit, set(), 0)

def find_max_pressure_with_elephant(valves, distances, time_limit):
    """Optimizes pressure release with an elephant helper."""
    useful_valves = [v for v in valves if valves[v][0] > 0]
    best_pressure = 0

    # Split useful valves into two groups for player and elephant
    for human_valves in combinations(useful_valves, len(useful_valves) // 2):
        human_valves = set(human_valves)
        elephant_valves = set(useful_valves) - human_valves
        
        human_pressure = find_max_pressure({v: valves[v] for v in human_valves}, distances, time_limit)
        elephant_pressure = find_max_pressure({v: valves[v] for v in elephant_valves}, distances, time_limit)
        
        best_pressure = max(best_pressure, human_pressure + elephant_pressure)
    
    return best_pressure

def main():
    print("\n--- Day 16: Proboscidea Volcanium ---")
    input_data = read_input("2022/input/day16.txt")
    valves, distances = parse_input(input_data)

    # Part 1
    part1_result = find_max_pressure(valves, distances, 30)
    print(f"Part 1: {part1_result}")

    # Part 2
    part2_result = find_max_pressure_with_elephant(valves, distances, 26)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()