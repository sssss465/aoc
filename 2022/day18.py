import fileinput
from itertools import product, combinations
from collections import Counter, defaultdict
from functools import cache
import sys

sys.setrecursionlimit(4500)

lines = [l.strip() for l in fileinput.input()]

cubes = {}
for l in lines:
    x, y, z = l.split(',')
    cubes[(int(x), int(y), int(z))] = 6
air = defaultdict(int)

visited = set()

# we can't use cache here because one dfs cycle may mark an area as a dead end, however it may have an exit


def exterior(cube):
    if any(e < -1 or e > 22 for e in cube):
        return True
    visited.add(cube)
    good = False
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if (cube[0]+dx, cube[1]+dy, cube[2]+dz) not in cubes and (cube[0]+dx, cube[1]+dy, cube[2]+dz) not in visited:
            r = exterior((cube[0]+dx, cube[1]+dy, cube[2]+dz))
            if r:
                good = True
                break
    return good


# not 2432, 2417, 2442
for x, y, z in list(cubes):
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if (x+dx, y+dy, z+dz) in cubes:
            cubes[x, y, z] -= 1
        else:
            air[x+dx, y+dy, z+dz] += 1
print('silver', sum(cubes.values()))

# print(exterior((8, 14, 19)), exterior((4, 5, 15)))
gold, bad = set(), set()
for i, c in enumerate(air.keys()):
    if c in gold or c in bad:
        continue
    r = exterior(c)
    # we mark bad nodes as well because they won't have a corresponding air value
    if r:   # all nodes that are outside are transitively outside
        gold |= visited
    else:
        bad |= visited
    visited.clear()
print('gold', sum(air[c] for c in gold))
