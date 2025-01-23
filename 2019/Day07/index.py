from itertools import permutations

class IntcodeComputer:
    def __init__(self, program):
        self.program = program.copy()
        self.pc = 0
        self.halted = False
        
    def get_param(self, pos, mode):
        if mode == 0:
            return self.program[self.program[pos]]
        return self.program[pos]
        
    def run(self, inputs):
        input_ptr = 0
        while self.pc < len(self.program):
            opcode = self.program[self.pc] % 100
            modes = [(self.program[self.pc] // 100) % 10,
                    (self.program[self.pc] // 1000) % 10,
                    (self.program[self.pc] // 10000) % 10]
            
            if opcode == 99:
                self.halted = True
                return None
                
            if opcode == 1:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.program[self.program[self.pc + 3]] = p1 + p2
                self.pc += 4
            elif opcode == 2:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.program[self.program[self.pc + 3]] = p1 * p2
                self.pc += 4
            elif opcode == 3:
                if input_ptr >= len(inputs):
                    return None
                self.program[self.program[self.pc + 1]] = inputs[input_ptr]
                input_ptr += 1
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
                self.program[self.program[self.pc + 3]] = 1 if p1 < p2 else 0
                self.pc += 4
            elif opcode == 8:
                p1 = self.get_param(self.pc + 1, modes[0])
                p2 = self.get_param(self.pc + 2, modes[1])
                self.program[self.program[self.pc + 3]] = 1 if p1 == p2 else 0
                self.pc += 4

def run_sequence(program, phases):
    signal = 0
    for phase in phases:
        computer = IntcodeComputer(program)
        output = computer.run([phase, signal])
        signal = output
    return signal

def run_feedback_loop(program, phases):
    computers = [IntcodeComputer(program) for _ in range(5)]
    signal = 0
    
    # Initialize with phase settings
    for i, phase in enumerate(phases):
        computers[i].run([phase])
    
    while True:
        for i in range(5):
            output = computers[i].run([signal])
            if output is None and computers[i].halted:
                return signal
            if output is not None:
                signal = output

# Read input
with open('2019/Day07/input.txt', 'r') as file:
    program = list(map(int, file.read().strip().split(',')))

# Part 1
max_signal = max(run_sequence(program, phases) for phases in permutations(range(5)))
print(f"Part 1: {max_signal}")

# Part 2
max_signal = max(run_feedback_loop(program, phases) for phases in permutations(range(5, 10)))
print(f"Part 2: {max_signal}")