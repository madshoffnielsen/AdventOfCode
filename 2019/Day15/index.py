from collections import defaultdict, deque

class IntcodeComputer:
    def __init__(self, program):
        self.memory = defaultdict(int)
        for i, v in enumerate(program):
            self.memory[i] = v
        self.pc = 0
        self.relative_base = 0
        
    def get_param(self, pos, mode):
        if mode == 0:   # position mode
            return self.memory[self.memory[pos]]
        elif mode == 1: # immediate mode
            return self.memory[pos]
        else:           # relative mode
            return self.memory[self.memory[pos] + self.relative_base]
            
    def get_write_address(self, pos, mode):
        if mode == 0:
            return self.memory[pos]
        return self.memory[pos] + self.relative_base
            
    def run(self, input_value):
        while True:
            instruction = str(self.memory[self.pc]).zfill(5)
            opcode = int(instruction[-2:])
            modes = [int(x) for x in instruction[:-2][::-1]]
            
            if opcode == 99:
                return None
                
            if opcode == 1:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = p1 + p2
                self.pc += 4
            elif opcode == 2:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = p1 * p2
                self.pc += 4
            elif opcode == 3:
                addr = self.get_write_address(self.pc + 1, modes[0])
                self.memory[addr] = input_value
                self.pc += 2
            elif opcode == 4:
                output = self.get_param(self.pc + 1, modes[0])
                self.pc += 2
                return output
            elif opcode == 5:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.pc = p2 if p1 != 0 else self.pc + 3
            elif opcode == 6:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.pc = p2 if p1 == 0 else self.pc + 3
            elif opcode == 7:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = 1 if p1 < p2 else 0
                self.pc += 4
            elif opcode == 8:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = 1 if p1 == p2 else 0
                self.pc += 4
            elif opcode == 9:
                p1 = self.get_param(self.pc + 1, modes[0])
                self.relative_base += p1
                self.pc += 2

def explore_maze(program):
    computer = IntcodeComputer(program)
    area = defaultdict(int)
    pos = (0, 0)
    oxygen_pos = None
    movements = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    reverse_move = {1: 2, 2: 1, 3: 4, 4: 3}
    
    def dfs(pos, path):
        nonlocal oxygen_pos
        for direction in range(1, 5):
            new_pos = (pos[0] + movements[direction][0], 
                      pos[1] + movements[direction][1])
            if new_pos not in area:
                status = computer.run(direction)
                area[new_pos] = status
                if status:
                    if status == 2:
                        oxygen_pos = new_pos
                    dfs(new_pos, path + [direction])
                    computer.run(reverse_move[direction])
    
    area[pos] = 1
    dfs(pos, [])
    return area, oxygen_pos

def shortest_path(area, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        pos, steps = queue.popleft()
        if pos == end:
            return steps
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos not in visited and area[new_pos]:
                visited.add(new_pos)
                queue.append((new_pos, steps + 1))
    
    return -1

def fill_time(area, start):
    queue = deque([(start, 0)])
    visited = {start}
    max_time = 0
    
    while queue:
        pos, time = queue.popleft()
        max_time = max(max_time, time)
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos not in visited and area[new_pos]:
                visited.add(new_pos)
                queue.append((new_pos, time + 1))
    
    return max_time

# Read input
with open('2019/Day15/input.txt', 'r') as file:
    program = list(map(int, file.read().strip().split(',')))

# Part 1: Find shortest path to oxygen system
area, oxygen_pos = explore_maze(program)
steps = shortest_path(area, (0, 0), oxygen_pos)
print(f"Part 1: Steps to oxygen system: {steps}")

# Part 2: Calculate time to fill with oxygen
minutes = fill_time(area, oxygen_pos)
print(f"Part 2: Minutes to fill with oxygen: {minutes}")