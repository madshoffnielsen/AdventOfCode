def increment_password(password):
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        if password[i] == 'z':
            password[i] = 'a'
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def is_valid(password):
    # Rule 1: Password must include one increasing straight of at least three letters
    has_straight = any(ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2 for i in range(len(password) - 2))
    
    # Rule 2: Password must not contain the letters i, o, or l
    has_forbidden_letters = any(c in password for c in 'iol')
    
    # Rule 3: Password must contain at least two different, non-overlapping pairs of letters
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            pairs.add(password[i])
            i += 1
        i += 1
    
    return has_straight and not has_forbidden_letters and len(pairs) >= 2

def find_next_password(password):
    while True:
        password = increment_password(password)
        if is_valid(password):
            return password

def main():
    input_password = "vzbxkghb"
    next_password = find_next_password(input_password)
    print(f"Part 1: {next_password}")
    next_password = find_next_password(increment_password(next_password))
    print(f"Part 2: {next_password}")

if __name__ == "__main__":
    main()