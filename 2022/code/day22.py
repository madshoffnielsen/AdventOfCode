from collections import defaultdict

def read_input(file_path):
    with open(file_path, "r") as f:
        inp, seq = [z.split("\n") for z in f.read().split("\n\n")]
    return inp, seq[0]

def parse_grid(inp):
    n = len(inp)
    m = max(len(inp[i]) for i in range(n))
    for i in range(n):
        while len(inp[i]) < m:
            inp[i] += ' '
    return inp, n, m

def move_in_grid(inp, seq, n, m):
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]

    x, y, d = 0, 0, 0
    z = 0
    k = len(seq)

    while inp[x][y] == ' ':
        y += 1

    while z < k:
        num = seq[z]
        while z + 1 < k and '0' <= seq[z + 1] <= '9':
            z += 1
            num += seq[z]
        z += 1

        num = int(num)
        mv = 0
        while mv < num:
            dx, dy = DX[d], DY[d]
            X = (x + dx) % n
            Y = (y + dy) % m
            if inp[X][Y] == '.':
                x, y = X, Y
                mv += 1
            elif inp[X][Y] == ' ':
                x, y = X, Y
            else:
                break

        while inp[x][y] == ' ':
            x = (x - dx) % n
            y = (y - dy) % m

        if z < k:
            assert seq[z] in ['L', 'R']
            if seq[z] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            z += 1

    return (x + 1) * 1000 + (y + 1) * 4 + d

def part1(inp, seq):
    inp, n, m = parse_grid(inp)
    return move_in_grid(inp, seq, n, m)

def part2(inp, seq):
    inp, n, m = parse_grid(inp)

    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]

    x, y, d = 0, 0, 0
    z = 0
    side = 50
    k = len(seq)

    nxt = [defaultdict(tuple) for z in range(4)]
    for i in range(n):
        for j in range(m):
            if inp[i][j] == ' ':
                continue
            
            for z in range(4):
                try:
                    nxt[z][(i, j)] = (i + DX[z], j + DY[z], z)
                except:
                    continue

                #1
                if i == side - 1 and j >= 2 * side and z == 1:
                    nxt[1][(i, j)] = (j - side, 2 * side - 1, 2)
                if side <= i < 2 * side and j == 2 * side - 1 and z == 0:
                    nxt[0][(i, j)] = (side - 1, i + side, 3)

                #2
                if i < side and j == 3 * side - 1 and z == 0:
                    nxt[0][(i, j)] = (3 * side - 1 - i, 2 * side - 1, 2)
                if 2 * side <= i < 3 * side and j == 2 * side - 1 and z == 0:
                    nxt[0][(i, j)] = (3 * side - 1 - i, 3 * side - 1, 2)

                #8
                if i == 3 * side - 1 and side <= j <= 2 * side - 1 and z == 1:
                    nxt[1][(i, j)] = (j + 2 * side, side - 1, 2)
                if 3 * side <= i and j == side - 1 and z == 0:
                    nxt[0][(i, j)] = (3 * side - 1, i - 2 * side, 3)

                #9
                if side <= i < 2 * side and j == side and z == 2:
                    nxt[2][(i, j)] = (2 * side, i - side, 1)
                if i == 2 * side and j < side and z == 3:
                    nxt[3][(i, j)] = (j + side, side, 0)

                #10
                if i < side and j == side and z == 2:
                    nxt[2][(i, j)] = (3 * side - i - 1, 0, 0)
                if 2 * side <= i < 3 * side and j == 0 and z == 2:
                    nxt[2][(i, j)] = (3 * side - i - 1, side, 0)

                #11
                if i == 0 and 2 * side <= j < 3 * side and z == 3:
                    nxt[3][(i, j)] = (4 * side - 1, j - 2 * side, 3)
                if i == 4 * side - 1 and j < side and z == 1:
                    nxt[1][(i, j)] = (0, j + 2 * side, 1)

                #12
                if i == 0 and side <= j < 2 * side and z == 3:
                    nxt[3][(i, j)] = (j + 2 * side, 0, 0)
                if 3 * side <= i and j == 0 and z == 2:
                    nxt[2][(i, j)] = (0, i - 2 * side, 1)

    while inp[x][y] == ' ':
        y += 1

    z = 0

    while z < k:
        num = seq[z]
        while z + 1 < k and '0' <= seq[z + 1] <= '9':
            z += 1
            num += seq[z]
        z += 1

        num = int(num)

        mv = 0
        while mv < num:
            X, Y, D = nxt[d][(x, y)]
            if inp[X][Y] == '.':
                x = X
                y = Y
                d = D
                mv += 1
            else:
                break
        if z < k:
            assert seq[z] in ['L', 'R']
            if seq[z] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            z += 1

    return (x + 1) * 1000 + (y + 1) * 4 + d

def main():
    print("\n--- Day 22: Monkey Map ---")
    file_path = "2022/input/day22.txt"
    inp, seq = read_input(file_path)

    # Part 1
    result1 = part1(inp, seq)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(inp, seq)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()