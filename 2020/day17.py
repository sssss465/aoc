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
        nb_cache = {}
        deg_cache = {}

        def nearby(pos):
            if pos in nb_cache:
                return nb_cache[pos]
            nb_cache[pos] = [(*map(operator.add, pos, off),)
                             for off in itertools.product(offset, repeat=len(pos))][1:]
            return nb_cache[pos]

        def degree(pos):
            if pos in deg_cache:
                return deg_cache[pos]
            deg_cache[pos] = sum(int(p in mp) for p in nearby(pos))
            return deg_cache[pos]
        # we only need to check active cubes and their neighbors because inactive cubes can only become active from 3 neighbors
        neighbors = [nei for p in mp for nei in nearby(p)]
        add = set(filter(lambda p: degree(p) == 3, neighbors))
        remove = set(filter(lambda p: degree(p) not in (2, 3), mp))
        mp = mp - remove | add
        # print(sum((i for i in mp.values())))
    print('silver' if not gold else 'gold', len(mp))


solve()
solve(True)
