import sys
import collections
graph = collections.defaultdict(list)  # a orbited by b

for line in sys.stdin:
    x = line.rstrip()
    x = x.split(')')
    graph[x[0]].append(x[1])
    graph[x[1]].append(x[0])  # store bidirectional link

visited = set()


def dfs(p, cur=0):
    visited.add(p)
    if p == 'SAN' or p not in graph:
        return cur
    res = float('inf')
    for pl in graph[p]:
        if pl not in visited:
            s = dfs(pl, cur+1)
            res = min(res, s)
    return res


print(dfs(graph['YOU'][0]) - 1)
