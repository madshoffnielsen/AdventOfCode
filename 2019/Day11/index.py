from collections import defaultdict

class IntcodeComputer:
    def __init__(self, program):
        self.memory = defaultdict(int)
        for i, v in enumerate(program):
            self.memory[i] = v
        self.pc = 0
        self.relative_base = 0
        self.halted = False
        
    def get_param(self, pos, mode):
        if mode == 0:   # position mode
            return self.memory[self.memory[pos]]
        elif mode == 1: # immediate mode
            return self.memory[pos]
        else:           # relative mode
            return self.memory[self.memory[pos] + self.relative_base]
            
    def get_write_address(self, pos, mode):
        if mode == 0:   # position mode
            return self.memory[pos]
        else:           # relative mode
            return self.memory[pos] + self.relative_base
            
    def run(self, inputs):
        input_ptr = 0
        outputs = []
        
        while True:
            opcode = self.memory[self.pc] % 100
            modes = [(self.memory[self.pc] // 100) % 10,
                    (self.memory[self.pc] // 1000) % 10,
                    (self.memory[self.pc] // 10000) % 10]
            
            if opcode == 99:
                self.halted = True
                return outputs
                
            if opcode == 1:  # add
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = p1 + p2
                self.pc += 4
                
            elif opcode == 2:  # multiply
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = p1 * p2
                self.pc += 4
                
            elif opcode == 3:  # input
                if input_ptr >= len(inputs):
                    return outputs
                addr = self.get_write_address(self.pc + 1, modes[0])
                self.memory[addr] = inputs[input_ptr]
                input_ptr += 1
                self.pc += 2
                
            elif opcode == 4:  # output
                p1 = self.get_param(self.pc + 1, modes[0])
                outputs.append(p1)
                self.pc += 2
                if len(outputs) == 2:
                    return outputs
                
            elif opcode == 5:  # jump-if-true
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.pc = p2 if p1 != 0 else self.pc + 3
                
            elif opcode == 6:  # jump-if-false
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.pc = p2 if p1 == 0 else self.pc + 3
                
            elif opcode == 7:  # less than
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = 1 if p1 < p2 else 0
                self.pc += 4
                
            elif opcode == 8:  # equals
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                addr = self.get_write_address(self.pc + 3, modes[2])
                self.memory[addr] = 1 if p1 == p2 else 0
                self.pc += 4
                
            elif opcode == 9:  # adjust relative base
                p1 = self.get_param(self.pc + 1, modes[0])
                self.relative_base += p1
                self.pc += 2

def paint_hull(program, start_color=0):
    computer = IntcodeComputer(program)
    hull = defaultdict(int)
    painted = set()  # Track unique painted positions
    pos = (0, 0)
    direction = 0  # 0:up, 1:right, 2:down, 3:left
    hull[pos] = start_color
    
    while True:
        outputs = computer.run([hull[pos]])
        if not outputs:
            break
            
        color, turn = outputs
        hull[pos] = color
        painted.add(pos)  # Add position to painted set
        
        direction = (direction + (1 if turn else -1)) % 4
        
        # Move robot
        if direction == 0:    # up
            pos = (pos[0], pos[1] - 1)
        elif direction == 1:  # right
            pos = (pos[0] + 1, pos[1])
        elif direction == 2:  # down
            pos = (pos[0], pos[1] + 1)
        else:                # left
            pos = (pos[0] - 1, pos[1])
    
    return len(painted), hull  # Return count of unique painted positions and hull

def print_registration(hull):
    if not hull:
        return
    min_x = min(x for x, y in hull)
    max_x = max(x for x, y in hull)
    min_y = min(y for x, y in hull)
    max_y = max(y for x, y in hull)
    
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            line += '#' if hull[(x, y)] else ' '
        print(line)

# Read input
with open('2019/Day11/input.txt', 'r') as file:
    program = list(map(int, file.read().strip().split(',')))

# Part 1
panels_painted, hull = paint_hull(program)
print(f"Part 1: Panels painted at least once: {panels_painted}")

# Part 2
_, hull = paint_hull(program, start_color=1)
print("Part 2: Registration identifier:")
print_registration(hull)