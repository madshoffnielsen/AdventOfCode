import sys

class Cart:
    DIRECTIONS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    LEFT_TURN = {'^': '<', '<': 'v', 'v': '>', '>': '^'}
    RIGHT_TURN = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    STRAIGHT = {'^': '^', 'v': 'v', '<': '<', '>': '>'}
    INTERSECTION_TURNS = [LEFT_TURN, STRAIGHT, RIGHT_TURN]
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersection_count = 0
        self.crashed = False
    
    def move(self, tracks):
        if self.crashed:
            return
        dx, dy = self.DIRECTIONS[self.direction]
        self.x += dx
        self.y += dy
        track = tracks[self.x][self.y]
        if track == '+':
            self.direction = self.INTERSECTION_TURNS[self.intersection_count % 3][self.direction]
            self.intersection_count += 1
        elif track == '/':
            self.direction = {'^': '>', 'v': '<', '<': 'v', '>': '^'}[self.direction]
        elif track == '\\':
            self.direction = {'^': '<', 'v': '>', '<': '^', '>': 'v'}[self.direction]
    
    def position(self):
        return (self.y, self.x)

def read_input(filename):
    with open(filename) as f:
        grid = [list(line.rstrip('\n')) for line in f]
    carts = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in '^v<>':
                carts.append(Cart(i, j, cell))
                grid[i][j] = '|' if cell in '^v' else '-'
    return grid, carts

def find_first_crash(grid, carts):
    while True:
        carts.sort(key=lambda c: (c.x, c.y))
        positions = {cart.position() for cart in carts if not cart.crashed}
        for cart in carts:
            if cart.crashed:
                continue
            old_position = cart.position()
            cart.move(grid)
            new_position = cart.position()
            if new_position in positions:
                return new_position
            positions.remove(old_position)
            positions.add(new_position)

def find_last_cart(grid, carts):
    while len([c for c in carts if not c.crashed]) > 1:
        carts.sort(key=lambda c: (c.x, c.y))
        positions = {cart.position(): cart for cart in carts if not cart.crashed}
        for cart in carts:
            if cart.crashed:
                continue
            old_position = cart.position()
            cart.move(grid)
            new_position = cart.position()
            if new_position in positions and not positions[new_position].crashed:
                cart.crashed = True
                positions[new_position].crashed = True
                del positions[new_position]
            else:
                del positions[old_position]
                positions[new_position] = cart
    last_cart = next(c for c in carts if not c.crashed)
    return last_cart.position()

def main():
    grid, carts = read_input("2018/Day13/input.txt")
    first_crash = find_first_crash(grid, carts)
    print(f"Part 1: First crash at {first_crash}")
    grid, carts = read_input("2018/Day13/input.txt")  # Reload input for part 2
    last_cart = find_last_cart(grid, carts)
    print(f"Part 2: Last cart at {last_cart}")

if __name__ == "__main__":
    main()
