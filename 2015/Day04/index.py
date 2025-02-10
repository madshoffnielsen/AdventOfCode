import hashlib

def find_hash_with_prefix(secret_key, prefix):
    number = 0
    while True:
        hash_input = f"{secret_key}{number}".encode()
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith(prefix):
            return number
        number += 1

def part1(secret_key):
    return find_hash_with_prefix(secret_key, "00000")

def part2(secret_key):
    return find_hash_with_prefix(secret_key, "000000")

def main():
    secret_key = "yzbqklnj"
    print(f"Part 1: {part1(secret_key)}")
    print(f"Part 2: {part2(secret_key)}")

if __name__ == "__main__":
    main()