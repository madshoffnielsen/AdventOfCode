from collections import defaultdict

def parse_input(file_path):
    graph = defaultdict(list)
    with open(file_path, 'r') as file:
        for line in file:
            from_cave, to_cave = line.strip().split('-')
            graph[from_cave].append(to_cave)
            graph[to_cave].append(from_cave)
    return graph

def is_small_cave(cave):
    return cave.islower()

def count_paths(graph, current, visited):
    if current == 'end':
        return 1
    
    if is_small_cave(current) and current in visited:
        return 0
    
    visited.add(current)
    path_count = sum(count_paths(graph, neighbor, visited.copy()) for neighbor in graph[current] if neighbor != 'start')
    return path_count

def count_paths2(graph, current, visited, small_cave_visited_twice):
    if current == 'end':
        return 1
    
    if is_small_cave(current):
        if visited.get(current, 0) == 1 and not small_cave_visited_twice:
            small_cave_visited_twice = True
        elif visited.get(current, 0) >= 1:
            return 0
        
        visited[current] = visited.get(current, 0) + 1
    
    path_count = sum(count_paths2(graph, neighbor, visited.copy(), small_cave_visited_twice) for neighbor in graph[current] if neighbor != 'start')
    
    if is_small_cave(current):
        visited[current] -= 1
        if visited[current] == 0:
            del visited[current]
    
    return path_count

def main():
    print("\n--- Day 12: Passage Pathing ---")
    input_file = '2021/input/day12.txt'
    graph = parse_input(input_file)

    total_paths = count_paths(graph, 'start', set())
    print(f"Part 1: {total_paths}")

    total_paths2 = count_paths2(graph, 'start', {}, False)
    print(f"Part 2: {total_paths2}")

if __name__ == "__main__":
    main()