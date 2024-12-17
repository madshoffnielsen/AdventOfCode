import ctypes

from collections import OrderedDict

# File
commands = open("2015/Day07/input.txt", 'r').read().splitlines()
#commands = open("2015/Day07/input2.txt", 'r').read().splitlines()

#--- Day 7: Some Assembly Required ---
wires = {}

while len(commands) > 0:
    for command in commands:
        inst = command.split("->")

        if inst[0].strip().isnumeric():
            wires[inst[1].strip()] = int(inst[0])
            commands.remove(command)
        elif inst[0].strip() in wires:
            if inst[1].strip() not in wires:
                wires[inst[1].strip()] = wires[inst[0].strip()]
                commands.remove(command)
        elif "AND" in inst[0] :
            i = inst[0].strip().split(" AND ")
            if i[0].strip() not in wires: 
                if not i[0].strip().isnumeric():
                    continue
            if i[1].strip() not in wires:
                if not i[1].strip().isnumeric():
                    continue
            
            if i[0].strip().isnumeric() and i[1].strip().isnumeric():
                wires[inst[1].strip()] = int(i[0].strip()) & int(i[1].strip())
            elif i[0].strip().isnumeric():
                wires[inst[1].strip()] = int(i[0].strip()) & wires[i[1].strip()]
            elif i[1].strip().isnumeric():
                wires[inst[1].strip()] = wires[i[0].strip()] & int(i[1].strip())
            else:
                wires[inst[1].strip()] = wires[i[0].strip()] & wires[i[1].strip()]
                
            commands.remove(command)
        elif "OR" in inst[0] :
            i = inst[0].strip().split(" OR ")
            if i[0].strip() not in wires:
                if not i[0].strip().isnumeric():
                    continue
            if i[1].strip() not in wires:
                if not i[1].strip().isnumeric():
                    continue

            if i[0].strip().isnumeric() and i[1].strip().isnumeric():
                wires[inst[1].strip()] = int(i[0].strip()) | int(i[1].strip())
            elif i[0].strip().isnumeric():
                wires[inst[1].strip()] = int(i[0].strip()) | wires[i[1].strip()]
            elif i[1].strip().isnumeric():
                wires[inst[1].strip()] = wires[i[0].strip()] | int(i[1].strip())
            else:
                wires[inst[1].strip()] = wires[i[0].strip()] | wires[i[1].strip()]

            commands.remove(command)
        elif "LSHIFT" in inst[0] :
            i = inst[0].strip().split(" LSHIFT ")
            if i[0].strip() not in wires:
                continue

            wires[inst[1].strip()] = int(wires[i[0].strip()]) << int(i[1].strip())
            commands.remove(command)
        elif "RSHIFT" in inst[0] :
            i = inst[0].strip().split(" RSHIFT ")
            if i[0].strip() not in wires:
                continue

            wires[inst[1].strip()] = int(wires[i[0].strip()]) >> int(i[1].strip())
            commands.remove(command)
        elif "NOT" in inst[0] :
            i = inst[0].strip().split("NOT ")
            if i[1].strip() not in wires:
                continue

            wires[inst[1].strip()] = ctypes.c_uint16(~ wires[i[1].strip()]).value
            commands.remove(command)

print("a: " + str(wires['a']))