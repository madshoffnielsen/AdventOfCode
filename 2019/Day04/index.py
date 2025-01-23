def is_valid_password_part1(password):
    password_str = str(password)
    has_double = False
    for i in range(1, len(password_str)):
        if password_str[i] == password_str[i - 1]:
            has_double = True
        if password_str[i] < password_str[i - 1]:
            return False
    return has_double

def is_valid_password_part2(password):
    password_str = str(password)
    has_double = False
    i = 0
    while i < len(password_str) - 1:
        if password_str[i] == password_str[i + 1]:
            if (i == 0 or password_str[i] != password_str[i - 1]) and (i + 2 == len(password_str) or password_str[i] != password_str[i + 2]):
                has_double = True
            while i < len(password_str) - 1 and password_str[i] == password_str[i + 1]:
                i += 1
        if i < len(password_str) - 1 and password_str[i] > password_str[i + 1]:
            return False
        i += 1
    return has_double

def count_valid_passwords(range_start, range_end, validation_function):
    return sum(1 for password in range(range_start, range_end + 1) if validation_function(password))

# Input range
range_start = 284639
range_end = 748759

# Part 1: Count valid passwords
valid_passwords_part1 = count_valid_passwords(range_start, range_end, is_valid_password_part1)
print("Number of valid passwords for Part 1:", valid_passwords_part1)

# Part 2: Count valid passwords with the additional criteria
valid_passwords_part2 = count_valid_passwords(range_start, range_end, is_valid_password_part2)
print("Number of valid passwords for Part 2:", valid_passwords_part2)