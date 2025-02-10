import re

def read_input(file_path):
    with open(file_path) as f:
        passports = []
        current = {}
        
        for line in f:
            line = line.strip()
            if not line:
                if current:
                    passports.append(current)
                    current = {}
                continue
            
            fields = line.split()
            for field in fields:
                key, value = field.split(':')
                current[key] = value
                
        if current:
            passports.append(current)
            
        return passports

def is_valid_part1(passport):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return all(field in passport for field in required)

def is_valid_part2(passport):
    if not is_valid_part1(passport):
        return False
    
    # Birth Year
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    
    # Issue Year
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    
    # Expiration Year
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    
    # Height
    height = passport['hgt']
    if height.endswith('cm'):
        if not (150 <= int(height[:-2]) <= 193):
            return False
    elif height.endswith('in'):
        if not (59 <= int(height[:-2]) <= 76):
            return False
    else:
        return False
    
    # Hair Color
    if not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False
    
    # Eye Color
    if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    
    # Passport ID
    if not re.match(r'^[0-9]{9}$', passport['pid']):
        return False
    
    return True

def part1(passports):
    return sum(1 for p in passports if is_valid_part1(p))

def part2(passports):
    return sum(1 for p in passports if is_valid_part2(p))

def main():
    passports = read_input("2020/Day04/input.txt")
    print(f"Part 1: {part1(passports)}")
    print(f"Part 2: {part2(passports)}")

if __name__ == "__main__":
    main()