def part1(target):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    
    while len(recipes) < target + 10:
        # Create new recipes
        new_score = recipes[elf1] + recipes[elf2]
        recipes.extend(int(d) for d in str(new_score))
        
        # Move elves
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    
    return ''.join(map(str, recipes[target:target+10]))

def part2(target):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    target_str = str(target)
    target_len = len(target_str)
    
    while True:
        # Create new recipes
        new_score = recipes[elf1] + recipes[elf2]
        for digit in str(new_score):
            recipes.append(int(digit))
            
            # Check last recipes match target
            if len(recipes) >= target_len:
                if ''.join(map(str, recipes[-target_len:])) == target_str:
                    return len(recipes) - target_len
                elif len(recipes) > target_len and ''.join(map(str, recipes[-target_len-1:-1])) == target_str:
                    return len(recipes) - target_len - 1
        
        # Move elves
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

if __name__ == "__main__":
    target = 846601
    
    result_part1 = part1(target)
    print(f"Part 1: {result_part1}")
    
    result_part2 = part2(target)
    print(f"Part 2: {result_part2}")