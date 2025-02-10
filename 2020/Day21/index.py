from collections import defaultdict

def parse_input(filename):
    foods = []
    with open(filename) as f:
        for line in f:
            if '(' in line:
                ingredients, allergens = line.strip().split(' (contains ')
                ingredients = set(ingredients.split())
                allergens = set(allergens[:-1].split(', '))
                foods.append((ingredients, allergens))
    return foods

def find_allergens(foods):
    # Map each allergen to possible ingredients
    possibilities = defaultdict(lambda: set())
    all_ingredients = set()
    
    for ingredients, allergens in foods:
        all_ingredients.update(ingredients)
        for allergen in allergens:
            if not possibilities[allergen]:
                possibilities[allergen] = set(ingredients)
            else:
                possibilities[allergen] &= ingredients
    
    # Find ingredients without allergens
    dangerous = set()
    for possible in possibilities.values():
        dangerous.update(possible)
    safe = all_ingredients - dangerous
    
    # Match allergens to ingredients
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

def part1(foods):
    safe, _ = find_allergens(foods)
    return sum(len(ingredients & safe) for ingredients, _ in foods)

def part2(foods):
    _, allergen_map = find_allergens(foods)
    return ','.join(allergen_map[a] for a in sorted(allergen_map))

def main():
    foods = parse_input("2020/Day21/input.txt")
    print(f"Part 1: {part1(foods)}")
    print(f"Part 2: {part2(foods)}")

if __name__ == "__main__":
    main()