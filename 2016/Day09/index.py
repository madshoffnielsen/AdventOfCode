def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip()

def decompress_v1(data):
    decompressed = []
    i = 0
    while i < len(data):
        if data[i] == '(':
            marker_end = data.index(')', i)
            marker = data[i+1:marker_end]
            length, repeat = map(int, marker.split('x'))
            i = marker_end + 1
            decompressed.append(data[i:i+length] * repeat)
            i += length
        else:
            decompressed.append(data[i])
            i += 1
    return ''.join(decompressed)

def decompress_v2(data):
    def decompressed_length(data):
        length = 0
        i = 0
        while i < len(data):
            if data[i] == '(':
                marker_end = data.index(')', i)
                marker = data[i+1:marker_end]
                sub_length, repeat = map(int, marker.split('x'))
                i = marker_end + 1
                length += repeat * decompressed_length(data[i:i+sub_length])
                i += sub_length
            else:
                length += 1
                i += 1
        return length

    return decompressed_length(data)

def part1(data):
    decompressed = decompress_v1(data)
    return len(decompressed)

def part2(data):
    return decompress_v2(data)

if __name__ == "__main__":
    data = parse_input("2016/Day09/input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))