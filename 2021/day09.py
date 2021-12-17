import fileinput
from functools import reduce

lines = [l.strip() for l in fileinput.input()]

graph = []
for l in lines:
    graph.append(list(map(int, list(l))))
print(len(graph), len(graph[0]))
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
res = []
cord_low = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        small = True
        for x, y in dirs:
            if (
                i + x >= 0
                and i + x < len(graph)
                and j + y >= 0
                and j + y < len(graph[0])
            ):
                if graph[i + x][j + y] <= graph[i][j]:
                    small = False
                    break
        if small:
            cord_low.append((i, j))
            res.append(graph[i][j])
print("silver", sum([i + 1 for i in res]))


def dfs(i, j):
    if graph[i][j] == 9:
        return 0
    v = graph[i][j]
    graph[i][j] = "x"  # fill
    size = 1
    for x, y in dirs:
        if i + x >= 0 and i + x < len(graph) and j + y >= 0 and j + y < len(graph[0]):
            if graph[i + x][j + y] != "x" and graph[i + x][j + y] >= v:
                size += dfs(i + x, j + y)
    return size


gold = []
for low in cord_low:
    i, j = low
    r = dfs(i, j)
    gold.append(r)
gold = sorted(gold)
print(gold)
print("gold", reduce(lambda x, y: x * y, gold[-3:]))
