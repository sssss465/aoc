import fileinput
from collections import defaultdict, deque

lines = [line.strip() for line in fileinput.input()]

graph = defaultdict(str)
lows = []
startx, starty = 0, 0
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        graph[(i, j)] = c
        if c == 'S':
            startx, starty = i, j
        if c == 'a':
            lows.append((i, j))


def solve(startx, starty) -> int:
    q = deque([(ord('a'), startx, starty, 0)])
    mp = {'S': ord('a'), 'E': ord('z')+1}
    visited = set([(startx, starty)])
    steps = 0
    # print(graph)
    while q:
        q2 = deque()
        good = False
        for c, i, j, steps in q:
            if c == ord('z')+1:
                return steps
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not graph[(i+di, j+dj)] or (i+di, j+dj) in visited:
                    continue
                v = ord(graph[(i+di, j+dj)]) if graph[(i+di, j+dj)
                                                      ] not in mp else mp[graph[(i+di, j+dj)]]
                if v <= c+1:
                    # add visited before visiting style bfs ( faster than adding during iteration)
                    visited.add((i+di, j+dj))
                    q2.append((v, i+di, j+dj, steps+1))
        q = q2
        steps += 1
    return 10**10


print("silver:", solve(startx, starty))
print("gold:", min([solve(x, y) for x, y in lows]))
