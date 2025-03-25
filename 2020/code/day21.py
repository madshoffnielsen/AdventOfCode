from collections import defaultdict
from typing import Dict, List, Set, Tuple

Food = Tuple[Set[str], Set[str]]
Foods = List[Food]
AllergenMap = Dict[str, str]

def read_input(file_path: str) -> Foods:
    """Read food ingredients and allergens from file."""
    foods = []
    with open(file_path) as f:
        for line in f:
            if '(' in line:
                ingredients, allergens = line.strip().split(' (contains ')
                ingredients = set(ingredients.split())
                allergens = set(allergens[:-1].split(', '))
                foods.append((ingredients, allergens))
    return foods

def find_allergens(foods: Foods) -> Tuple[Set[str], AllergenMap]:
    """Find safe ingredients and allergen mappings."""
    possibilities = defaultdict(set)
    all_ingredients = set()
    
    for ingredients, allergens in foods:
        all_ingredients.update(ingredients)
        for allergen in allergens:
            if not possibilities[allergen]:
                possibilities[allergen] = set(ingredients)
            else:
                possibilities[allergen] &= ingredients
    
    dangerous = set().union(*possibilities.values())
    safe = all_ingredients - dangerous
    
    allergen_map = {}
    while possibilities:
        for allergen, possible in list(possibilities.items()):
            if len(possible) == 1:
                ingredient = possible.pop()
                allergen_map[allergen] = ingredient
                del possibilities[allergen]
                for p in possibilities.values():
                    p.discard(ingredient)
    
    return safe, allergen_map

def part1(foods: Foods) -> int:
    """Count occurrences of safe ingredients."""
    safe, _ = find_allergens(foods)
    return sum(len(ingredients & safe) for ingredients, _ in foods)

def part2(foods: Foods) -> str:
    """Build sorted list of dangerous ingredients."""
    _, allergen_map = find_allergens(foods)
    return ','.join(allergen_map[a] for a in sorted(allergen_map))

def main():
    """Main program."""
    print("\n--- Day 21: Allergen Assessment ---")
    
    foods = read_input("2020/input/day21.txt")
    
    result1 = part1(foods)
    print(f"Part 1: {result1}")
    
    result2 = part2(foods)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()