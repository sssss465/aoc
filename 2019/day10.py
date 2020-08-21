import math
import operator
from functools import reduce
import numpy as np
import sys
from math import atan2, atan, gcd
import collections
arr = []
for line in sys.stdin:
    x = list(line.rstrip())
    arr.append(x)

# def unit_vector(vector):
#     """ Returns the unit vector of the vector.  """
#     return vector / np.linalg.norm(vector)


# def angle_between(v1, v2):
#     x1, x2, y1, y2 = 0, v2[0] - v1[0], 0,  v2[1] - v1[1],
#     if (x2 == 0):
#         if y2 > 0:
#             return 'up'
#         return 'down'
#     angle = atan(y2 / x2)  # atan2(y, x) or atan2(sin, cos)
#     return angle


def comp(aa, bb):
    a = bb[0] - aa[0]  # rows
    b = bb[1] - aa[1]  # cols
    return (a // gcd(a, b), b // gcd(a, b))


def look(arr, spot):
    di = collections.defaultdict(list)
    # upflag, downflag = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (i, j) != spot and arr[i][j] == '#':
                ang = comp(spot, (i, j))
                # if ang in di:
                # print(ang, 'is already in from point ',
                #       di[ang], 'colliding with ', (i, j))
                # store one asteroid u can see, can be any
                di[ang].append((i, j))
    return len(di), di


res = 0
best = None
r = [[0]*len(arr[0]) for i in range(len(arr))]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '#':
            x, _ = look(arr, (i, j))
            if x > res:
                res = x
                best = (i, j)
            r[i][j] = x
            # print(i, j, x)
print("part 1 answer is ", res, best)
_, best_comps = look(arr, best)
# print(best_comps)
keys = []
for k, v in best_comps.items():
    keys.append((k[1], k[0]))

# coords = [(0.5, 1), (0, 1), (1, 0), (1, 1), (0, 0)]
coords = keys
# center = tuple(map(operator.truediv, reduce(
#     lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))

# print(center, tuple(reduce(
#     lambda x, y: map(operator.add, x, y), coords)))
center = [0, 0]
coords = sorted(coords, key=lambda coord: (90 + math.degrees(math.atan2(*
                                                                        tuple(map(operator.sub, coord, center))[::-1]))) % 360)
# print(coords)
coords = [(b, a) for a, b in coords]

for k, v in best_comps.items():
    best_comps[k] = sorted(best_comps[k], key=lambda l: abs(
        l[0] - best[0]) + abs(l[1] - best[1]))
p = 0
r = []
# print(coords)
while len(r) < 200:
    k = coords[p % len(coords)]
    if len(best_comps[k]) != 0:
        r.append(best_comps[k][0])
        del best_comps[k][0]
    else:
        del best_comps[k]
    p += 1
# print(best_comps)
print(r[:10])  # i am using row col
ans = r[-1]
print(ans)
print("part2 is ", ans[0] + ans[1] * 100)
