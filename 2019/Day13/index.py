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
                if len(outputs) == 3:
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

def run_game(program, play_mode=False):
    computer = IntcodeComputer(program)
    screen = defaultdict(int)
    ball_x = paddle_x = score = 0
    
    if play_mode:
        computer.memory[0] = 2  # Insert quarters to play for free
    
    while not computer.halted:
        outputs = computer.run([0 if ball_x == paddle_x else (1 if ball_x > paddle_x else -1)])
        if not outputs:
            break
        
        x, y, tile_id = outputs
        if x == -1 and y == 0:
            score = tile_id
        else:
            screen[(x, y)] = tile_id
            if tile_id == 3:
                paddle_x = x
            elif tile_id == 4:
                ball_x = x
    
    return screen, score

def count_block_tiles(screen):
    return sum(1 for tile in screen.values() if tile == 2)

# Read input
with open('2019/Day13/input.txt', 'r') as file:
    program = list(map(int, file.read().strip().split(',')))

# Part 1: Count block tiles
screen, _ = run_game(program)
block_tiles = count_block_tiles(screen)
print(f"Part 1: Number of block tiles: {block_tiles}")

# Part 2: Play the game and get the score
_, score = run_game(program, play_mode=True)
print(f"Part 2: Final score: {score}")