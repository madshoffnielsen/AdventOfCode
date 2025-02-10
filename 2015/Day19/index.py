import re

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    replacements = []
    molecule = lines[-1].strip()
    for line in lines[:-2]:
        parts = line.strip().split(" => ")
        replacements.append((parts[0], parts[1]))
    return replacements, molecule

def generate_molecules(replacements, molecule):
    molecules = set()
    for src, dest in replacements:
        for match in re.finditer(src, molecule):
            start, end = match.span()
            new_molecule = molecule[:start] + dest + molecule[end:]
            molecules.add(new_molecule)
    return molecules

def part1(replacements, molecule):
    molecules = generate_molecules(replacements, molecule)
    return len(molecules)

def part2(replacements, molecule):
    reverse_replacements = [(dest, src) for src, dest in replacements]
    steps = 0
    while molecule != "e":
        for src, dest in reverse_replacements:
            if src in molecule:
                molecule = molecule.replace(src, dest, 1)
                steps += 1
                break
    return steps

def main():
    replacements, molecule = read_input("2015/Day19/input.txt")
    print(f"Part 1: {part1(replacements, molecule)}")
    print(f"Part 2: {part2(replacements, molecule)}")

if __name__ == "__main__":
    main()