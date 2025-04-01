from typing import List, Set, Tuple
from collections import defaultdict
from itertools import combinations

Point = Tuple[int, int]

class IntcodeComputer:
    def __init__(self, program: List[int]):
        self.memory = defaultdict(int)
        for i, v in enumerate(program):
            self.memory[i] = v
        self.ip = 0
        self.relative_base = 0
        
    def get_param(self, param: int, mode: int) -> int:
        if mode == 0:   # position mode
            return self.memory[param]
        elif mode == 1: # immediate mode
            return param
        else:           # relative mode
            return self.memory[self.relative_base + param]
            
    def get_address(self, param: int, mode: int) -> int:
        if mode == 0:   # position mode
            return param
        else:           # relative mode
            return self.relative_base + param

    def run(self, inputs: List[int] = None) -> List[int]:
        outputs = []
        input_ptr = 0
        
        while True:
            opcode = self.memory[self.ip] % 100
            modes = [(self.memory[self.ip] // 100) % 10,
                    (self.memory[self.ip] // 1000) % 10,
                    (self.memory[self.ip] // 10000) % 10]
            
            if opcode == 99:
                break
                
            elif opcode == 1: # add
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                p2 = self.get_param(self.memory[self.ip + 2], modes[1])
                addr = self.get_address(self.memory[self.ip + 3], modes[2])
                self.memory[addr] = p1 + p2
                self.ip += 4
                
            elif opcode == 2: # multiply
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                p2 = self.get_param(self.memory[self.ip + 2], modes[1])
                addr = self.get_address(self.memory[self.ip + 3], modes[2])
                self.memory[addr] = p1 * p2
                self.ip += 4
                
            elif opcode == 3: # input
                if inputs is None or input_ptr >= len(inputs):
                    return outputs
                addr = self.get_address(self.memory[self.ip + 1], modes[0])
                self.memory[addr] = inputs[input_ptr]
                input_ptr += 1
                self.ip += 2
                
            elif opcode == 4: # output
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                outputs.append(p1)
                self.ip += 2
                
            elif opcode == 5: # jump-if-true
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                p2 = self.get_param(self.memory[self.ip + 2], modes[1])
                self.ip = p2 if p1 != 0 else self.ip + 3
                
            elif opcode == 6: # jump-if-false
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                p2 = self.get_param(self.memory[self.ip + 2], modes[1])
                self.ip = p2 if p1 == 0 else self.ip + 3
                
            elif opcode == 7: # less than
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                p2 = self.get_param(self.memory[self.ip + 2], modes[1])
                addr = self.get_address(self.memory[self.ip + 3], modes[2])
                self.memory[addr] = 1 if p1 < p2 else 0
                self.ip += 4
                
            elif opcode == 8: # equals
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                p2 = self.get_param(self.memory[self.ip + 2], modes[1])
                addr = self.get_address(self.memory[self.ip + 3], modes[2])
                self.memory[addr] = 1 if p1 == p2 else 0
                self.ip += 4
                
            elif opcode == 9: # adjust relative base
                p1 = self.get_param(self.memory[self.ip + 1], modes[0])
                self.relative_base += p1
                self.ip += 2
                
        return outputs

def read_input(file_path: str) -> List[int]:
    """Read Intcode program from file."""
    with open(file_path) as f:
        return [int(x) for x in f.read().strip().split(',')]

def get_scaffold_map(program: List[int]) -> Tuple[Set[Point], Point, int]:
    """Get scaffold map and robot position from ASCII output."""
    computer = IntcodeComputer(program)
    output = computer.run()
    
    scaffolds = set()
    x, y = 0, 0
    robot_pos = None
    robot_dir = None
    
    for ascii_code in output:
        char = chr(ascii_code)
        if char == '\n':
            y += 1
            x = 0
            continue
            
        if char == '#':
            scaffolds.add((x, y))
        elif char in '^v<>':
            scaffolds.add((x, y))
            robot_pos = (x, y)
            robot_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}[char]
        x += 1
        
    return scaffolds, robot_pos, robot_dir

def get_intersections(scaffolds: Set[Point]) -> List[Point]:
    """Find scaffold intersections."""
    intersections = []
    for x, y in scaffolds:
        if all((x+dx, y+dy) in scaffolds 
               for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]):
            intersections.append((x, y))
    return intersections

def get_path(scaffolds: Set[Point], start: Point, direction: int) -> str:
    """Get path through scaffolds as movement instructions."""
    x, y = start
    path = []
    moves = [(0,-1), (1,0), (0,1), (-1,0)]  # N, E, S, W
    
    while True:
        # Try to go forward
        dx, dy = moves[direction]
        steps = 0
        while (x + dx, y + dy) in scaffolds:
            steps += 1
            x += dx
            y += dy
        if steps > 0:
            path.append(str(steps))
            
        # Try to turn
        for turn, new_dir in [('L', (direction-1) % 4), ('R', (direction+1) % 4)]:
            dx, dy = moves[new_dir]
            if (x + dx, y + dy) in scaffolds:
                path.append(turn)
                direction = new_dir
                break
        else:
            break  # No more turns possible
            
    return ','.join(path)

def compress_path(path: str) -> Tuple[str, List[str]]:
    """Compress path into main routine and movement functions."""
    parts = path.split(',')
    
    # Try all combinations of function lengths
    for a_len in range(1, 11):
        for b_len in range(1, 11):
            for c_len in range(1, 11):
                # Try to find repeating patterns
                i = 0
                funcs = []
                main = []
                used = set()
                
                while i < len(parts):
                    # Try to match existing function
                    matched = False
                    for f_idx, func in enumerate(funcs):
                        if parts[i:i+len(func)] == func:
                            main.append(chr(65 + f_idx))
                            i += len(func)
                            matched = True
                            break
                            
                    if matched:
                        continue
                        
                    # Try to create new function
                    if len(funcs) < 3:
                        if len(funcs) == 0:
                            size = a_len
                        elif len(funcs) == 1:
                            size = b_len
                        else:
                            size = c_len
                            
                        new_func = parts[i:i+size]
                        func_str = ','.join(new_func)
                        if len(func_str) <= 20 and func_str not in used:
                            funcs.append(new_func)
                            used.add(func_str)
                            main.append(chr(65 + len(funcs) - 1))
                            i += size
                            continue
                            
                    break
                else:
                    # Successfully compressed path
                    return ','.join(main), [','.join(f) for f in funcs]
                    
    raise ValueError("Could not compress path")

def part1(program: List[int]) -> int:
    """Calculate sum of alignment parameters."""
    scaffolds, _, _ = get_scaffold_map(program)
    intersections = get_intersections(scaffolds)
    return sum(x * y for x, y in intersections)

def part2(program: List[int]) -> int:
    """Get dust collected by robot."""
    # Get scaffold map and robot position
    scaffolds, robot_pos, robot_dir = get_scaffold_map(program)
    
    # Get and compress path
    path = get_path(scaffolds, robot_pos, robot_dir)
    main, funcs = compress_path(path)
    
    # Prepare input
    inputs = []
    for line in [main] + funcs + ['n']:  # 'n' for no continuous video feed
        inputs.extend(ord(c) for c in line)
        inputs.append(ord('\n'))
    
    # Run robot with movement routine
    program[0] = 2  # Wake up robot
    computer = IntcodeComputer(program)
    output = computer.run(inputs)
    
    return output[-1]  # Last output is dust collected

def main():
    """Main program."""
    print("\n--- Day 17: Set and Forget ---")
    
    program = read_input("2019/Day17/input.txt")
    
    result1 = part1(program)
    print(f"Part 1: {result1}")
    
    result2 = part2(program)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()