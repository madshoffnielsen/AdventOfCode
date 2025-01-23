def generate_pattern(position, length):
    base_pattern = [0, 1, 0, -1]
    pattern = []
    for value in base_pattern:
        pattern.extend([value] * position)
    return (pattern * (length // len(pattern) + 1))[1:length + 1]

def apply_fft_phase(signal):
    result = []
    length = len(signal)
    for i in range(length):
        pattern = generate_pattern(i + 1, length)
        total = sum(s * p for s, p in zip(signal, pattern))
        result.append(abs(total) % 10)
    return result

def apply_fft_phases(signal, phases):
    current = signal[:]
    for _ in range(phases):
        current = apply_fft_phase(current)
    return current

def apply_fft_phase_optimized(signal):
    # For the second half of the signal, each digit is just the sum of
    # all following digits modulo 10
    result = signal[:]
    for i in range(len(signal) - 2, -1, -1):
        result[i] = (result[i] + result[i + 1]) % 10
    return result

def process_real_signal(signal, offset):
    # For part 2, we only need to process the second half of the signal
    real_signal = (signal * 10000)[offset:]
    current = real_signal
    
    for _ in range(100):
        current = apply_fft_phase_optimized(current)
    
    return current[:8]

# Read input
with open('2019/Day16/input.txt', 'r') as file:
    input_signal = [int(x) for x in file.read().strip()]

# Part 1: Apply 100 phases of FFT
result = apply_fft_phases(input_signal, 100)
print(f"Part 1: First eight digits: {''.join(map(str, result[:8]))}")

# Part 2: Process real signal
offset = int(''.join(map(str, input_signal[:7])))
result = process_real_signal(input_signal, offset)
print(f"Part 2: Eight digit message: {''.join(map(str, result))}")