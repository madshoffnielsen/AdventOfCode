from collections import defaultdict, deque
from math import lcm
from dataclasses import dataclass
from typing import Dict, List, Set

@dataclass
class Module:
    type: str
    name: str
    destinations: List[str]
    state: bool = False
    memory: Dict[str, bool] = None

def parse_input(file_path: str) -> Dict[str, Module]:
    modules = {}
    connections = {}
    
    with open(file_path) as f:
        for line in f:
            source, dests = line.strip().split(' -> ')
            dests = dests.split(', ')
            
            if source == 'broadcaster':
                name = source
                type = 'broadcaster'
            else:
                type = source[0]
                name = source[1:]
                
            modules[name] = Module(type, name, dests)
            connections[name] = dests
    
    # Initialize conjunction modules' memory
    for name, module in modules.items():
        if module.type == '&':
            module.memory = {}
            for source, dests in connections.items():
                if name in dests:
                    module.memory[source] = False
    
    return modules

def process_pulse(modules: Dict[str, Module], target: str = None) -> tuple[int, int]:
    low = high = 0
    queue = deque([('button', 'broadcaster', False)])
    
    seen_cycles = defaultdict(set)
    cycle_lengths = {}
    
    while queue:
        source, dest, pulse = queue.popleft()
        
        if pulse:
            high += 1
        else:
            low += 1
            
        if dest not in modules:
            continue
            
        module = modules[dest]
        
        if module.type == 'broadcaster':
            for next_dest in module.destinations:
                queue.append((dest, next_dest, pulse))
                
        elif module.type == '%':
            if not pulse:
                module.state = not module.state
                for next_dest in module.destinations:
                    queue.append((dest, next_dest, module.state))
                    
        elif module.type == '&':
            module.memory[source] = pulse
            output = not all(module.memory.values())
            for next_dest in module.destinations:
                queue.append((dest, next_dest, output))
                
    return low, high

def part1(modules: Dict[str, Module]) -> int:
    low = high = 0
    for _ in range(1000):
        l, h = process_pulse(modules)
        low += l
        high += h
    return low * high

def part2(modules: Dict[str, Module]) -> int:
    # Find the module that feeds into 'rx'
    for name, module in modules.items():
        if 'rx' in module.destinations:
            watch = name
            break
    
    # Find modules that feed into the watch module
    cycle_lengths = {}
    feeds = [name for name, m in modules.items() if watch in m.destinations]
    
    presses = 0
    while len(cycle_lengths) < len(feeds):
        presses += 1
        queue = deque([('button', 'broadcaster', False)])
        
        while queue:
            source, dest, pulse = queue.popleft()
            
            if dest == watch and pulse:
                if source not in cycle_lengths:
                    cycle_lengths[source] = presses
            
            if dest not in modules:
                continue
                
            module = modules[dest]
            if module.type == 'broadcaster':
                for next_dest in module.destinations:
                    queue.append((dest, next_dest, pulse))
            elif module.type == '%':
                if not pulse:
                    module.state = not module.state
                    for next_dest in module.destinations:
                        queue.append((dest, next_dest, module.state))
            elif module.type == '&':
                module.memory[source] = pulse
                output = not all(module.memory.values())
                for next_dest in module.destinations:
                    queue.append((dest, next_dest, output))
    
    return lcm(*cycle_lengths.values())

def main():
    modules = parse_input("2023/Day20/input.txt")
    print(f"Part 1: {part1(modules)}")
    modules = parse_input("2023/Day20/input.txt")  # Reset modules
    print(f"Part 2: {part2(modules)}")

if __name__ == "__main__":
    main()