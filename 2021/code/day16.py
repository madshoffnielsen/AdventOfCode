def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def hex_to_bin(hex_str):
    return ''.join(bin(int(char, 16))[2:].zfill(4) for char in hex_str)

def parse_packet(binary_str, start_index=0):
    version = int(binary_str[start_index:start_index + 3], 2)
    type_id = int(binary_str[start_index + 3:start_index + 6], 2)
    current_index = start_index + 6

    version_sum = version

    if type_id == 4:
        literal_value = ''
        while True:
            group = binary_str[current_index:current_index + 5]
            literal_value += group[1:]
            current_index += 5
            if group[0] == '0':
                break
        return version_sum, current_index

    length_type_id = binary_str[current_index]
    current_index += 1

    if length_type_id == '0':
        sub_packet_length = int(binary_str[current_index:current_index + 15], 2)
        current_index += 15
        end_index = current_index + sub_packet_length
        while current_index < end_index:
            sub_version_sum, current_index = parse_packet(binary_str, current_index)
            version_sum += sub_version_sum
    else:
        num_sub_packets = int(binary_str[current_index:current_index + 11], 2)
        current_index += 11
        for _ in range(num_sub_packets):
            sub_version_sum, current_index = parse_packet(binary_str, current_index)
            version_sum += sub_version_sum

    return version_sum, current_index

def decode_hex_packet(hex_str):
    binary_str = hex_to_bin(hex_str)
    version_sum, _ = parse_packet(binary_str)
    return version_sum

def parse_packet2(binary_str, start_index=0):
    version = int(binary_str[start_index:start_index + 3], 2)
    type_id = int(binary_str[start_index + 3:start_index + 6], 2)
    current_index = start_index + 6

    version_sum = version

    value = 0

    if type_id == 4:
        literal_value = ''
        while True:
            group = binary_str[current_index:current_index + 5]
            literal_value += group[1:]
            current_index += 5
            if group[0] == '0':
                break
        value = int(literal_value, 2)
        return version_sum, value, current_index

    length_type_id = binary_str[current_index]
    current_index += 1

    sub_packet_values = []

    if length_type_id == '0':
        sub_packet_length = int(binary_str[current_index:current_index + 15], 2)
        current_index += 15
        end_index = current_index + sub_packet_length
        while current_index < end_index:
            sub_version_sum, sub_value, current_index = parse_packet2(binary_str, current_index)
            version_sum += sub_version_sum
            sub_packet_values.append(sub_value)
    else:
        num_sub_packets = int(binary_str[current_index:current_index + 11], 2)
        current_index += 11
        for _ in range(num_sub_packets):
            sub_version_sum, sub_value, current_index = parse_packet2(binary_str, current_index)
            version_sum += sub_version_sum
            sub_packet_values.append(sub_value)

    if type_id == 0:
        value = sum(sub_packet_values)
    elif type_id == 1:
        value = 1
        for val in sub_packet_values:
            value *= val
    elif type_id == 2:
        value = min(sub_packet_values)
    elif type_id == 3:
        value = max(sub_packet_values)
    elif type_id == 5:
        value = 1 if sub_packet_values[0] > sub_packet_values[1] else 0
    elif type_id == 6:
        value = 1 if sub_packet_values[0] < sub_packet_values[1] else 0
    elif type_id == 7:
        value = 1 if sub_packet_values[0] == sub_packet_values[1] else 0

    return version_sum, value, current_index

def decode_hex_packet2(hex_str):
    binary_str = hex_to_bin(hex_str)
    version_sum, value, _ = parse_packet2(binary_str)
    return value

def main():
    print("\n--- Day 16: Packet Decoder ---")
    input_file = '2021/input/day16.txt'
    hex_input = parse_input(input_file)
    version_sum = decode_hex_packet(hex_input)
    print(f"Part 1: {version_sum}")
    
    value = decode_hex_packet2(hex_input)
    print(f"Part 2: {value}")

if __name__ == "__main__":
    main()