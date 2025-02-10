def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    aunts = {}
    for line in lines:
        parts = line.strip().split(': ', 1)
        aunt_number = int(parts[0].split()[1])
        attributes = dict(attr.split(': ') for attr in parts[1].split(', '))
        aunts[aunt_number] = {k: int(v) for k, v in attributes.items()}
    return aunts

def find_matching_aunt(aunts, known_attributes, part2=False):
    for aunt, attributes in aunts.items():
        match = True
        for attr, value in attributes.items():
            if part2:
                if attr in ['cats', 'trees']:
                    if value <= known_attributes[attr]:
                        match = False
                        break
                elif attr in ['pomeranians', 'goldfish']:
                    if value >= known_attributes[attr]:
                        match = False
                        break
                elif known_attributes[attr] != value:
                    match = False
                    break
            else:
                if known_attributes[attr] != value:
                    match = False
                    break
        if match:
            return aunt
    return None

def main():
    known_attributes = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    
    aunts = read_input("2015/Day16/input.txt")
    print(f"Part 1: {find_matching_aunt(aunts, known_attributes)}")
    print(f"Part 2: {find_matching_aunt(aunts, known_attributes, part2=True)}")

if __name__ == "__main__":
    main()