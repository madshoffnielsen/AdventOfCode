def read_input(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().strip()
    return input_data

def parse_input(input_data):
    lines = input_data.split('\n')
    algorithm = lines[0].replace('#', '1').replace('.', '0')
    image = []
    for row in lines[2:]:
        image.append([1 if char == '#' else 0 for char in row])
    return algorithm, image

def enhance_image(algorithm, image, iterations):
    outer = '0'
    for _ in range(iterations):
        count = 0
        out = []
        for row in range(-1, len(image) + 1):
            out_row = []
            for col in range(-1, len(image[0]) + 1):
                bin_str = ''
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < len(image) and 0 <= col + j < len(image[0]):
                            bin_str += str(image[row + i][col + j])
                        else:
                            bin_str += outer
                value = int(bin_str, 2)
                out_row.append(int(algorithm[value]))
                count += int(algorithm[value])
            out.append(out_row)
        bin_str = outer * 9
        outer = algorithm[int(bin_str, 2)]
        image = out
    return count

def main():
    print("\n--- Day 20: Trench Map ---")
    input_file = '2021/input/day20.txt'
    input_data = read_input(input_file)
    algorithm, image = parse_input(input_data)

    # Part 1
    result = enhance_image(algorithm, image, 2)
    print(f"Part 1: {result}")

    # Part 2
    result = enhance_image(algorithm, image, 50)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()