from collections import defaultdict

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
    
    def run(self, inputs):
        input_ptr = 0
        outputs = []
        
        while True:
            instruction = str(self.memory[self.pc]).zfill(5)
            opcode = int(instruction[-2:])
            modes = [int(x) for x in instruction[:-2][::-1]]
            
            if opcode == 99:
                return outputs
                
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
                if input_ptr >= len(inputs):
                    return outputs
                addr = self.get_write_address(self.pc + 1, modes[0])
                self.memory[addr] = inputs[input_ptr]
                input_ptr += 1
                self.pc += 2
            elif opcode == 4:
                outputs.append(self.get_param(self.pc + 1, modes[0]))
                self.pc += 2
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
                self.relative_base += self.get_param(self.pc + 1, modes[0])
                self.pc += 2

def run_springscript(program, script):
    computer = IntcodeComputer(program.copy())
    ascii_input = [ord(c) for c in script]
    output = computer.run(ascii_input)
    return output[-1] if output[-1] > 127 else ''.join(chr(x) for x in output)

# Read input
with open('2019/Day21/input.txt', 'r') as file:
    program = list(map(int, file.read().strip().split(',')))

# Part 1: Walk mode
# Jump if there's a hole ahead (not A) and landing is safe (D)
walk_script = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""

result1 = run_springscript(program, walk_script)
print(f"Part 1: {result1}")

# Part 2: Run mode
# Jump if there's a hole ahead and landing is safe
# Also check if we can continue running or need another jump
run_script = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
"""

result2 = run_springscript(program, run_script)
print(f"Part 2: {result2}")