def find_house_with_presents(target_presents):
    houses = [0] * (target_presents // 10)
    for elf in range(1, len(houses)):
        for house in range(elf, len(houses), elf):
            houses[house] += elf * 10
    for house, presents in enumerate(houses):
        if presents >= target_presents:
            return house

def find_house_with_presents_limit(target_presents):
    houses = [0] * (target_presents // 10)
    for elf in range(1, len(houses)):
        for house in range(elf, min(len(houses), elf * 50), elf):
            houses[house] += elf * 11
    for house, presents in enumerate(houses):
        if presents >= target_presents:
            return house

def main():
    target_presents = 36000000
    print(f"Part 1: {find_house_with_presents(target_presents)}")
    print(f"Part 2: {find_house_with_presents_limit(target_presents)}")

if __name__ == "__main__":
    main()