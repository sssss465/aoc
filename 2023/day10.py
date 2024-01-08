import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict, deque
import math
import bisect

lines = [l.strip() for l in fileinput.input()]
mat = lines
empty_rows = []
empty_cols = []
factor = 2


def extra(mat, row=True):
    out = []
    for i, l in enumerate(mat):
        if all(c == "." for c in l):
            # out.append(l[:])
            if row:
                empty_rows.append(i)
            else:
                empty_cols.append(i)
        out.append(l[:])
    return out


def transpose(mat):
    return ["".join(row) for row in zip(*mat)]


pairs = defaultdict(dict)


def dist(g1, g2, factor=2):
    r1 = bisect.bisect_right(empty_rows, g1[0])
    r2 = bisect.bisect_right(empty_rows, g2[0])
    c1 = bisect.bisect_right(empty_cols, g1[1])
    c2 = bisect.bisect_right(empty_cols, g2[1])
    return (
        abs(g2[0] - g1[0])
        + abs(g2[1] - g1[1])
        + (factor - 1) * abs(r1 - r2)
        + (factor - 1) * abs(c1 - c2)
    )


mat = extra(mat)
mat = extra(mat, row=False)
gals = []

silver = 0
gold = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == "#":
            gals.append((i, j))
for i in range(len(gals)):
    for j in range(0, i):
        silver += dist(gals[i], gals[j])
        gold += dist(gals[i], gals[j], factor=10**6)

print(silver)
print(gold)


# for l in mat:
#     print(l)
