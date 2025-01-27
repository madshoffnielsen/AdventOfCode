def parse_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def parse_technique(line):
    if line == "deal into new stack":
        return ("reverse", 0)
    elif line.startswith("cut"):
        return ("cut", int(line.split()[-1]))
    else:
        return ("increment", int(line.split()[-1]))

def apply_shuffle(size, instructions):
    a, b = 1, 0
    for technique, n in instructions:
        if technique == "reverse":
            a = -a % size
            b = (size - 1 - b) % size
        elif technique == "cut":
            b = (b - n) % size
        elif technique == "increment":
            a = (a * n) % size
            b = (b * n) % size
    return a, b

def mod_pow(base, exponent, modulus):
    if exponent == 0:
        return 1
    half = mod_pow(base, exponent // 2, modulus)
    if exponent % 2 == 0:
        return (half * half) % modulus
    else:
        return (half * half * base) % modulus

def mod_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x
    
    _, x, _ = egcd(a, m)
    return x % m

def compose_shuffles(a, b, count, size):
    # Calculate a^count and geometric series for b
    a_n = mod_pow(a, count, size)
    if a == 1:
        b_n = (b * count) % size
    else:
        b_n = (b * (a_n - 1) * mod_inverse(a - 1, size)) % size
    return a_n, b_n

# Read and parse input
instructions = [parse_technique(line) for line in parse_input('2019/Day22/input.txt')]

# Part 1: Track position of card 2019
size = 10007
a, b = apply_shuffle(size, instructions)
position = (a * 2019 + b) % size
print(f"Part 1: {position}")

# Part 2: Find card at position 2020 after many shuffles
size = 119315717514047
count = 101741582076661
a, b = apply_shuffle(size, instructions)
a_n, b_n = compose_shuffles(a, b, count, size)
result = ((2020 - b_n) * mod_inverse(a_n, size)) % size
print(f"Part 2: {result}")