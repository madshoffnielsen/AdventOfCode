import json
from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_value(x, y, _input, s_key, e_key, a_key):
    v = _input[y][x]
    key = json.dumps([x, y])
    if v == 'S':
        if not s_key[0]:
            s_key[0] = key
            a_key[key] = 1
        return 'a'
    elif v == 'E':
        if not e_key[0]:
            e_key[0] = key
        return 'z'
    elif v == 'a':
        a_key[key] = 1
    return v

def is_adjacent(v, v2):
    # Check if v2 is one higher or less than v
    return ord(v2) - ord(v) <= 1

def build_graph(_input):
    graph = {}  # adjacency list
    s_key = [None]
    e_key = [None]
    a_key = {}

    rows, cols = len(_input), len(_input[0])

    for y in range(rows):
        for x in range(cols):
            key = json.dumps([x, y])
            if key not in graph:
                graph[key] = []
            v = get_value(x, y, _input, s_key, e_key, a_key)

            # Check adjacent cells
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    v2 = get_value(nx, ny, _input, s_key, e_key, a_key)
                    if is_adjacent(v, v2):
                        graph[key].append(json.dumps([nx, ny]))

    return graph, s_key[0], e_key[0], a_key

def bfs(graph, start, end=None):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    queue.append(path + [adj])

    return []

def main():
    print("\n--- Day 12: Hill Climbing Algorithm ---")
    input = read_input("2022/input/day12.txt")
    graph, s_key, e_key, a_key = build_graph(input)

    # Part 1: Shortest path from start to end
    part1_path = bfs(graph, s_key, e_key)
    part1_steps = len(part1_path) - 1 if part1_path else float('inf')
    print(f"Part 1: {part1_steps}")

    # Part 2: Shortest path from any 'a' to end
    part2_steps = float('inf')
    for a in a_key.keys():
        path = bfs(graph, a, e_key)
        if path:
            part2_steps = min(part2_steps, len(path) - 1)
    print(f"Part 2: {part2_steps}")

if __name__ == "__main__":
    main()