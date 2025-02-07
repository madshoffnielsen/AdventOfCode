def read_input(file_path):
    layers = {}
    with open(file_path) as f:
        for line in f:
            depth, range_val = map(int, line.strip().split(': '))
            layers[depth] = range_val
    return layers

def scanner_position(time, range_val):
    if range_val == 1:
        return 0
    period = 2 * (range_val - 1)
    return time % period

def severity(layers, delay=0):
    total = 0
    caught = False
    
    for depth, range_val in layers.items():
        if scanner_position(depth + delay, range_val) == 0:
            total += depth * range_val
            caught = True
            
    return total if delay == 0 else caught

def find_safe_delay(layers):
    delay = 0
    while severity(layers, delay):
        delay += 1
    return delay

def main():
    layers = read_input("2017/Day13/input.txt")
    print(f"Part 1: {severity(layers)}")
    print(f"Part 2: {find_safe_delay(layers)}")

if __name__ == "__main__":
    main()