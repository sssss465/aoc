import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict, deque
from functools import cache
import math
import bisect


lines = [l.strip() for l in fileinput.input()]


reflect = {
    "|": {(0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)]},
    "-": {(1, 0): [(0, -1), (0, 1)], (-1, 0): [(0, -1), (0, 1)]},
    "/": {(1, 0): [(0, -1)], (0, 1): [(-1, 0)], (-1, 0): [(0, 1)], (0, -1): [(1, 0)]},
    "\\": {(1, 0): [(0, 1)], (0, 1): [(1, 0)], (-1, 0): [(0, -1)], (0, -1): [(-1, 0)]},
    ".": {},
}


def solve(start, d):
    visited = defaultdict(set)
    q: deque[tuple[tuple, tuple]] = deque([(start, d)])  # pos dir
    while q:
        pos, d = q.popleft()
        if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
            continue
        if d in visited[pos]:
            continue
        visited[pos].add(d)
        if d in reflect[lines[pos[0]][pos[1]]]:
            for npos in reflect[lines[pos[0]][pos[1]]][d]:
                nx, ny = pos[0] + npos[0], pos[1] + npos[1]
                q.append(((nx, ny), npos))
        else:
            q.append(((pos[0] + d[0], pos[1] + d[1]), d))

        # for i in range(len(lines)):
        #     for j in range(len(lines[0])):
        #         if (i, j) in visited:
        #             print("#", end="")
        #         else:
        #             print(lines[i][j], end="")
        #     print("\n", end="")
        # print()
    return len(visited)


print(solve((0, 0), (0, 1)))  # silver


def finddir(pos):
    dirs = []
    if pos[0] == 0:
        dirs.append((1, 0))
    if pos[0] == len(lines) - 1:
        dirs.append((-1, 0))
    if pos[1] == 0:
        dirs.append((0, 1))
    if pos[1] == len(lines[0]) - 1:
        dirs.append((0, -1))
    return dirs


print(
    max(
        solve((i, j), d)
        for i in range(len(lines))
        for j in range(len(lines[0]))
        for d in finddir((i, j))
        if i in (0, len(lines) - 1) or j in (0, len(lines[0]) - 1)
    )
)  # gold
