def parse_image(data, width, height):
    layer_size = width * height
    layers = [data[i:i + layer_size] for i in range(0, len(data), layer_size)]
    return layers

def find_layer_with_fewest_zeros(layers):
    fewest_zeros_layer = min(layers, key=lambda layer: layer.count('0'))
    return fewest_zeros_layer

def calculate_checksum(layer):
    return layer.count('1') * layer.count('2')

def decode_image(layers, width, height):
    final_image = ['2'] * (width * height)
    for layer in layers:
        for i in range(len(layer)):
            if final_image[i] == '2':
                final_image[i] = layer[i]
    return final_image

def print_image(image, width):
    for i in range(0, len(image), width):
        print(''.join(image[i:i + width]).replace('0', ' ').replace('1', '#'))

# Read input from input.txt
with open('2019/Day08/input.txt', 'r') as file:
    input_data = file.read().strip()

# Image dimensions
width = 25
height = 6

# Parse the image into layers
layers = parse_image(input_data, width, height)

# Part 1: Find the layer with the fewest 0 digits and calculate the checksum
fewest_zeros_layer = find_layer_with_fewest_zeros(layers)
checksum = calculate_checksum(fewest_zeros_layer)
print("Checksum (Part 1):", checksum)

# Part 2: Decode the image and print it
final_image = decode_image(layers, width, height)
print("Decoded image (Part 2):")
print_image(final_image, width)