import re
from collections import deque

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    nodes = {}
    for line in lines[2:]:
        parts = re.split(r'\s+', line.strip())
        x, y = map(int, re.findall(r'\d+', parts[0]))
        size, used, avail = map(int, [parts[1][:-1], parts[2][:-1], parts[3][:-1]])
        nodes[(x, y)] = {'size': size, 'used': used, 'avail': avail}
    return nodes

def viable_pairs(nodes):
    pairs = 0
    for a in nodes:
        for b in nodes:
            if a != b and nodes[a]['used'] > 0 and nodes[a]['used'] <= nodes[b]['avail']:
                pairs += 1
    return pairs

def bfs(nodes, start, goal):
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == goal:
            return steps
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in nodes and (nx, ny) not in visited and nodes[(nx, ny)]['used'] <= nodes[start]['size']:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    return float('inf')

def part1(nodes):
    return viable_pairs(nodes)

def part2(nodes):
    empty_node = next(node for node, data in nodes.items() if data['used'] == 0)
    target_data = (max(x for x, y in nodes), 0)
    steps_to_empty = bfs(nodes, empty_node, (target_data[0] - 1, 0))
    steps_to_goal = steps_to_empty + 1 + (target_data[0] - 1) * 5
    return steps_to_goal

def main():
    nodes = read_input("2016/Day22/input.txt")
    print(f"Part 1: {part1(nodes)}")
    print(f"Part 2: {part2(nodes)}")

if __name__ == "__main__":
    main()