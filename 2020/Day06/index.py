def read_input(file_path):
    with open(file_path) as f:
        groups = []
        current_group = []
        
        for line in f:
            line = line.strip()
            if not line:
                if current_group:
                    groups.append(current_group)
                    current_group = []
            else:
                current_group.append(set(line))
                
        if current_group:
            groups.append(current_group)
            
        return groups

def part1(groups):
    return sum(len(set.union(*group)) for group in groups)

def part2(groups):
    return sum(len(set.intersection(*group)) for group in groups)

def main():
    groups = read_input("2020/Day06/input.txt")
    print(f"Part 1: {part1(groups)}")
    print(f"Part 2: {part2(groups)}")

if __name__ == "__main__":
    main()