from functools import reduce
from itertools import count

inp = open('input.txt').read().splitlines()
M = {i + j * 1j for j, l in enumerate(inp) for i, x in enumerate(l) if x == "#"}


DIRS = [
    lambda pos: (
        all(pos.real + dx + (pos.imag - 1) * 1j not in M for dx in (-1, 0, 1)),
        pos.real + (pos.imag - 1) * 1j,
    ),  # move north
    lambda pos: (
        all(pos.real + dx + (pos.imag + 1) * 1j not in M for dx in (-1, 0, 1)),
        pos.real + (pos.imag + 1) * 1j,
    ),  # move south
    lambda pos: (
        all(pos.real - 1 + (pos.imag + dy) * 1j not in M for dy in (-1, 0, 1)),
        pos.real - 1 + pos.imag * 1j,
    ),  # move west
    lambda pos: (
        all(pos.real + 1 + (pos.imag + dy) * 1j not in M for dy in (-1, 0, 1)),
        pos.real + 1 + pos.imag * 1j,
    ),  # move east
]


def nextPos(pos, ri):
    if all(  # do not move if no neighbors
        pos.real + dx + (pos.imag + dy) * 1j not in M
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if dx != 0 or dy != 0
    ):
        return pos
    for di in range(ri, ri + 4):
        pred, npos = DIRS[di % 4](pos)
        if pred:  # move according to the first matching rule
            return npos
    return pos


for ri in count():
    nM = reduce(
        lambda S, pos: {**S, nextPos(pos, ri): S.get(nextPos(pos, ri), []) + [pos]},
        M,
        {},
    )
    nM = {npos for npos, pos in nM.items() if len(pos) == 1} | {
        p for _, pos in nM.items() for p in pos if len(pos) > 1
    }
    if ri == 10:
        minx = int(min(pos.real for pos in M))
        maxx = int(max(pos.real for pos in M))
        miny = int(min(pos.imag for pos in M))
        maxy = int(max(pos.imag for pos in M))
        print(
            "Part1:",
            sum(
                1
                for i in range(minx, maxx + 1)
                for j in range(miny, maxy + 1)
                if i + j * 1j not in M
            ),
        )

    if nM == M:
        print("Part2:", ri + 1)
        break
    M = nM