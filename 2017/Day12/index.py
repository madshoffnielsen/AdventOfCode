def read_input(file_path):
    connections = {}
    with open(file_path) as f:
        for line in f:
            prog, connected = line.strip().split(' <-> ')
            connections[int(prog)] = [int(x) for x in connected.split(', ')]
    return connections

def find_group(connections, start, visited):
    if start in visited:
        return set()
    
    group = {start}
    visited.add(start)
    stack = [start]
    
    while stack:
        current = stack.pop()
        for next_prog in connections[current]:
            if next_prog not in visited:
                visited.add(next_prog)
                group.add(next_prog)
                stack.append(next_prog)
    
    return group

def count_groups(connections):
    visited = set()
    groups = []
    
    for prog in connections:
        if prog not in visited:
            group = find_group(connections, prog, visited)
            groups.append(group)
    
    return len(groups)

def main():
    connections = read_input("2017/Day12/input.txt")
    group_zero = len(find_group(connections, 0, set()))
    total_groups = count_groups(connections)
    
    print(f"Part 1: {group_zero}")
    print(f"Part 2: {total_groups}")

if __name__ == "__main__":
    main()