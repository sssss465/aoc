import fileinput
import re
from collections import defaultdict
from functools import cache
import itertools

lines = [line.strip() for line in fileinput.input()]
rate = defaultdict(int)
graph = defaultdict(list)
time = 30
released = 0
D = defaultdict(lambda: 1000)
for l in lines:
    source, r, dests = re.findall(r' ([\w]{2}).*=([\d]+).*es? (.+)', l)[0]
    dests = dests.split(', ')
    for dest in dests:
        graph[source].append(dest)
        D[source, dest] = 1
    if r != '0':
        rate[source] = int(r)

visited = set()


@cache
def dfs(node='AA', nodeb='AA', time=30, rel_rate=0, turn=1, silver=True):
    # if not silver and time == 1 and turn == 1:
    #     print(node, nodeb, time, rel_rate, turn, silver)
    if time == 0:
        return 0
    res = turn*rel_rate
    # path.append(node)
    if silver:
        cur = node
        time -= 1
        turn = 1
    elif not turn:
        cur = nodeb
        time -= 1
    else:
        cur = node
    if rate[cur] > 0:
        old = rate[cur]
        rate[cur] = 0
        res = max(
            res, turn*rel_rate + dfs(node, nodeb, time, rel_rate+old, turn ^ 1, silver))
        rate[cur] = old
    for dest in graph[cur]:
        if (turn) or silver:
            res = max(
                res, (turn)*rel_rate + dfs(dest, nodeb, time, rel_rate, turn ^ 1, silver))
        else:
            res = max(
                res, dfs(node, dest, time, rel_rate, turn ^ 1, silver))
    # path.pop()
    return res


# not 2349 ( too low)
print(dfs(silver=True))
# print(dfs(node='AA', nodeb='AA', time=26, rel_rate=0, turn=1, silver=False))
# cheating
for k, i, j in itertools.product(graph, graph, graph):    # floyd-warshall
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])

d2 = dict()
for r in rate:
    if rate[r]:
        d2[r] = rate[r]


@ cache
def search(t, u='AA', vs=frozenset(d2), e=False):
    return max([rate[v] * (t-D[u, v]-1) + search(t-D[u, v]-1, v, vs-{v}, e)
                for v in vs if D[u, v] < t] + [search(26, vs=vs) if e else 0])


print(search(26, e=True))
