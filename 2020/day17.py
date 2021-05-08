import fileinput
import itertools
import functools
import operator

lines = [l.strip() for l in fileinput.input()]

symbol = {'#': 1, '.': 0}
offset = [0, -1, 1]


def solve(gold=False):
    mp = {(r_c, c_c, 0) if not gold else (r_c, c_c, 0, 0) for r_c,
          row in enumerate(lines) for c_c, col in enumerate(row) if col == '#'}
    # print(mp)
    for round in range(6):
        def nearby(pos):
            return [(*map(operator.add, pos, off),) for off in itertools.product(offset, repeat=len(pos))][1:]

        def degree(pos):
            return sum(int(p in mp) for p in nearby(pos))
        # we only need to check active cubes and their neighbors because inactive cubes can only become active from 3 neighbors
        neighbors = [nei for p in mp for nei in nearby(p)]
        add = set(filter(lambda p: degree(p) == 3, neighbors))
        remove = set(filter(lambda p: degree(p) not in (2, 3), mp))
        mp = mp - remove | add
        # print(sum((i for i in mp.values())))
    print('silver' if not gold else 'gold', len(mp))


solve()
solve(True)
