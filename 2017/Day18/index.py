from collections import defaultdict, deque

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip().split() for line in f]

class Program:
    def __init__(self, instructions, pid=0):
        self.registers = defaultdict(int)
        self.registers['p'] = pid
        self.instructions = instructions
        self.pos = 0
        self.last_sound = None
        self.queue = deque()
        self.send_count = 0
        self.waiting = False

    def get_value(self, x):
        try:
            return int(x)
        except ValueError:
            return self.registers[x]

    def execute(self, other=None):
        if self.pos < 0 or self.pos >= len(self.instructions):
            return None

        inst = self.instructions[self.pos]
        cmd = inst[0]
        
        if cmd == 'snd':
            if other:
                other.queue.append(self.get_value(inst[1]))
                self.send_count += 1
            else:
                self.last_sound = self.get_value(inst[1])
        elif cmd == 'set':
            self.registers[inst[1]] = self.get_value(inst[2])
        elif cmd == 'add':
            self.registers[inst[1]] += self.get_value(inst[2])
        elif cmd == 'mul':
            self.registers[inst[1]] *= self.get_value(inst[2])
        elif cmd == 'mod':
            self.registers[inst[1]] %= self.get_value(inst[2])
        elif cmd == 'rcv':
            if other:
                if not self.queue:
                    self.waiting = True
                    return None
                self.waiting = False
                self.registers[inst[1]] = self.queue.popleft()
            elif self.get_value(inst[1]) != 0:
                return self.last_sound
        elif cmd == 'jgz':
            if self.get_value(inst[1]) > 0:
                self.pos += self.get_value(inst[2])
                return None

        self.pos += 1
        return None

def part1(instructions):
    prog = Program(instructions)
    while True:
        result = prog.execute()
        if result is not None:
            return result

def part2(instructions):
    prog0 = Program(instructions, 0)
    prog1 = Program(instructions, 1)
    
    while True:
        prog0.execute(prog1)
        prog1.execute(prog0)
        
        if prog0.waiting and prog1.waiting and not prog0.queue and not prog1.queue:
            return prog1.send_count

def main():
    instructions = read_input("2017/Day18/input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")

if __name__ == "__main__":
    main()