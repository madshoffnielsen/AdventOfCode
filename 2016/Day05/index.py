import hashlib

def find_password(door_id):
    password = []
    index = 0
    while len(password) < 8:
        hash_input = f"{door_id}{index}".encode()
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith("00000"):
            password.append(hash_output[5])
        index += 1
    return ''.join(password)

def find_complex_password(door_id):
    password = ['_'] * 8
    index = 0
    filled_positions = 0
    while filled_positions < 8:
        hash_input = f"{door_id}{index}".encode()
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith("00000"):
            position = hash_output[5]
            if position.isdigit():
                position = int(position)
                if 0 <= position < 8 and password[position] == '_':
                    password[position] = hash_output[6]
                    filled_positions += 1
        index += 1
    return ''.join(password)

if __name__ == "__main__":
    door_id = "ffykfhsq"
    print("Part 1:", find_password(door_id))
    print("Part 2:", find_complex_password(door_id))