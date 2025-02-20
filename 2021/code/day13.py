import re

def parse_input(file_path):
    dots = []
    folds = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("fold along"):
                match = re.match(r"fold along ([xy])=(\d+)", line)
                folds.append((match[1], int(match[2])))
            elif ',' in line:
                dots.append(tuple(map(int, line.split(','))))
    
    return dots, folds

def fold_paper(dots, fold):
    axis, line = fold
    new_dots = set()
    
    for x, y in dots:
        if axis == 'x' and x > line:
            x = line - (x - line)
        elif axis == 'y' and y > line:
            y = line - (y - line)
        new_dots.add((x, y))
    
    return list(new_dots)

def count_dots_after_first_fold(file_path):
    dots, folds = parse_input(file_path)
    dots = fold_paper(dots, folds[0])
    return len(dots)

def apply_all_folds(dots, folds):
    for fold in folds:
        dots = fold_paper(dots, fold)
    return dots

def visualize_dots(dots):
    max_x = max(x for x, y in dots)
    max_y = max(y for x, y in dots)
    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for x, y in dots:
        grid[y][x] = '#'
    
    for line in grid:
        print(''.join(line))

def get_activation_code(file_path):
    dots, folds = parse_input(file_path)
    dots = apply_all_folds(dots, folds)
    visualize_dots(dots)

def main():
    print("\n--- Day 13: Transparent Origami ---")
    input_file = '2021/input/day13.txt'
    result = count_dots_after_first_fold(input_file)
    print(f"Part 1: {result}")

    print("Part 2:")
    get_activation_code(input_file)

if __name__ == "__main__":
    main()