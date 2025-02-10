from itertools import product

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    ingredients = []
    for line in lines:
        parts = line.strip().split()
        name = parts[0][:-1]
        capacity = int(parts[2][:-1])
        durability = int(parts[4][:-1])
        flavor = int(parts[6][:-1])
        texture = int(parts[8][:-1])
        calories = int(parts[10])
        ingredients.append((name, capacity, durability, flavor, texture, calories))
    return ingredients

def calculate_score(ingredients, amounts):
    capacity = sum(amount * ingredient[1] for amount, ingredient in zip(amounts, ingredients))
    durability = sum(amount * ingredient[2] for amount, ingredient in zip(amounts, ingredients))
    flavor = sum(amount * ingredient[3] for amount, ingredient in zip(amounts, ingredients))
    texture = sum(amount * ingredient[4] for amount, ingredient in zip(amounts, ingredients))
    calories = sum(amount * ingredient[5] for amount, ingredient in zip(amounts, ingredients))
    
    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
        return 0, calories
    
    return capacity * durability * flavor * texture, calories

def find_best_recipe(ingredients, calorie_constraint=None):
    best_score = 0
    for amounts in product(range(101), repeat=len(ingredients)):
        if sum(amounts) == 100:
            score, calories = calculate_score(ingredients, amounts)
            if calorie_constraint is None or calories == calorie_constraint:
                best_score = max(best_score, score)
    return best_score

def part1(ingredients):
    return find_best_recipe(ingredients)

def part2(ingredients):
    return find_best_recipe(ingredients, calorie_constraint=500)

def main():
    ingredients = read_input("2015/Day15/input.txt")
    print(f"Part 1: {part1(ingredients)}")
    print(f"Part 2: {part2(ingredients)}")

if __name__ == "__main__":
    main()