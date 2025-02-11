from math import lcm
import re

def read_input(file_path):
    with open(file_path) as f:
        instructions = [0 if x == 'L' else 1 for x in f.readline().strip()]
        f.readline()  # skip blank line
        
        nodes = {}
        for line in f:
            node, left, right = re.findall(r'[A-Z0-9]+', line)
            nodes[node] = (left, right)
            
        return instructions, nodes

def steps_to_end(start, instructions, nodes, part2=False):
    current = start
    steps = 0
    inst_len = len(instructions)
    
    while True:
        if part2:
            if current.endswith('Z'):
                return steps
        elif current == 'ZZZ':
            return steps
            
        direction = instructions[steps % inst_len]
        current = nodes[current][direction]
        steps += 1

def part1(instructions, nodes):
    return steps_to_end('AAA', instructions, nodes)

def part2(instructions, nodes):
    start_nodes = [node for node in nodes if node.endswith('A')]
    cycles = []
    
    for start in start_nodes:
        cycle_length = steps_to_end(start, instructions, nodes, True)
        cycles.append(cycle_length)
    
    return lcm(*cycles)

def main():
    instructions, nodes = read_input("2023/Day08/input.txt")
    print(f"Part 1: {part1(instructions, nodes)}")
    print(f"Part 2: {part2(instructions, nodes)}")

if __name__ == "__main__":
    main()