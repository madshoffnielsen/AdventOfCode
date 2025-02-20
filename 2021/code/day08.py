def count_easy_digits(input_file):
    with open(input_file, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    easy_digit_count = 0
    unique_segment_lengths = {2, 4, 3, 7}
    
    for line in lines:
        _, output_values = line.split(' | ')
        output_signals = output_values.split()
        
        for signal in output_signals:
            if len(signal) in unique_segment_lengths:
                easy_digit_count += 1
    
    return easy_digit_count

def deduce_mapping(patterns):
    sorted_patterns = {''.join(sorted(pattern)): pattern for pattern in patterns}
    by_length = {}
    
    for pattern in sorted_patterns:
        by_length.setdefault(len(pattern), []).append(pattern)
    
    mapping = {}
    reverse_mapping = {}
    reverse_mapping[1] = by_length[2][0]
    reverse_mapping[4] = by_length[4][0]
    reverse_mapping[7] = by_length[3][0]
    reverse_mapping[8] = by_length[7][0]
    
    for pattern in by_length[6]:
        if contains_all(pattern, reverse_mapping[4]):
            reverse_mapping[9] = pattern
        elif contains_all(pattern, reverse_mapping[7]):
            reverse_mapping[0] = pattern
        else:
            reverse_mapping[6] = pattern
    
    for pattern in by_length[5]:
        if contains_all(pattern, reverse_mapping[7]):
            reverse_mapping[3] = pattern
        elif contains_all(reverse_mapping[6], pattern):
            reverse_mapping[5] = pattern
        else:
            reverse_mapping[2] = pattern
    
    mapping = {''.join(sorted(value)): key for key, value in reverse_mapping.items()}
    return mapping

def contains_all(pattern, subset):
    return set(subset).issubset(set(pattern))

def decode_output(outputs, mapping):
    decoded_digits = ''.join(str(mapping[''.join(sorted(output))]) for output in outputs)
    return int(decoded_digits)

def decode_and_sum(input_file):
    with open(input_file, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    total_sum = 0
    
    for line in lines:
        patterns, outputs = line.split(' | ')
        patterns = patterns.split()
        outputs = outputs.split()
        mapping = deduce_mapping(patterns)
        decoded_value = decode_output(outputs, mapping)
        total_sum += decoded_value
    
    return total_sum

def main():
    print("\n--- Day 8: Seven Segment Search ---")
    input_file = '2021/Day08/input.txt'
    result = count_easy_digits(input_file)
    print(f"Part 1: {result}")

    result = decode_and_sum(input_file)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()