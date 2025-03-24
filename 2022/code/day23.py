from itertools import count

def read_input(file_path):
    with open(file_path, "r") as f:
        inp = f.read().splitlines()
    return {i + j * 1j for j, line in enumerate(inp) for i, x in enumerate(line) if x == "#"}

def get_directions():
    return [
        lambda pos, M: (
            all(pos.real + dx + (pos.imag - 1) * 1j not in M for dx in (-1, 0, 1)),
            pos.real + (pos.imag - 1) * 1j,
        ),  # move north
        lambda pos, M: (
            all(pos.real + dx + (pos.imag + 1) * 1j not in M for dx in (-1, 0, 1)),
            pos.real + (pos.imag + 1) * 1j,
        ),  # move south
        lambda pos, M: (
            all(pos.real - 1 + (pos.imag + dy) * 1j not in M for dy in (-1, 0, 1)),
            pos.real - 1 + pos.imag * 1j,
        ),  # move west
        lambda pos, M: (
            all(pos.real + 1 + (pos.imag + dy) * 1j not in M for dy in (-1, 0, 1)),
            pos.real + 1 + pos.imag * 1j,
        ),  # move east
    ]

def next_position(pos, ri, M, DIRS):
    if all(
        pos.real + dx + (pos.imag + dy) * 1j not in M
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if dx != 0 or dy != 0
    ):
        return pos
    for di in range(ri, ri + 4):
        pred, npos = DIRS[di % 4](pos, M)
        if pred:
            return npos
    return pos

def simulate(M):
    DIRS = get_directions()
    part1 = None

    for ri in count():
        # Calculate the next positions
        next_positions = {}
        for pos in M:
            npos = next_position(pos, ri, M, DIRS)
            if npos not in next_positions:
                next_positions[npos] = []
            next_positions[npos].append(pos)

        # Update the positions
        nM = set()
        for npos, positions in next_positions.items():
            if len(positions) == 1:
                nM.add(npos)
            else:
                nM.update(positions)

        # Calculate Part 1 result after max_rounds
        if ri == 10:
            minx = int(min(pos.real for pos in M))
            maxx = int(max(pos.real for pos in M))
            miny = int(min(pos.imag for pos in M))
            maxy = int(max(pos.imag for pos in M))
            part1 = sum(
                1
                for i in range(minx, maxx + 1)
                for j in range(miny, maxy + 1)
                if i + j * 1j not in M
            )

        # Check if no positions moved
        if nM == M:
            return part1, ri + 1

        M = nM

def main():
    print("\n--- Day 23: Unstable Diffusion ---")
    file_path = "2022/input/day23.txt"
    M = read_input(file_path)
    part1, part2 = simulate(M)

    # Part 1
    print(f"Part 1: {part1}")

    # Part 2
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()