import sys
import collections
graph = collections.defaultdict(list)  # a orbited by b
planets = set()
for line in sys.stdin:
    x = line.rstrip().split(')')
    graph[x[0]].append(x[1])
    planets.add(x[1])
res = 0


def dfs(p, cur=0):
    dp = cur
    if p not in graph:
        return dp
    for pl in graph[p]:
        dp += dfs(pl, cur+1)
    return dp


for k, v in graph.items():
    if k not in planets:  # no ancestors
        print(k)
        res += dfs(k)
print(res)
