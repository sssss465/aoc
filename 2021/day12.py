import fileinput
import collections

lines = [l.strip() for l in fileinput.input()]

# lines = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]

graph = collections.defaultdict(list)


def solve(visited={}, p="silver"):
    paths = [0]

    def been(d, k, twice):
        if twice:
            return d[k] > 1
        return d[k] > 0

    def dfs(node, visited={}, paths=[], twice=True):
        # print(node, visited, paths, twice, p)
        if been(visited, node, twice):
            return 0
        if node == "end":
            # print(paths + [node], twice)
            return 1
        if not node.isupper():
            visited[node] += 1
        res = 0
        for n in graph[node]:
            if not been(visited, n, twice):
                res += dfs(
                    n,
                    visited,
                    paths + [node],
                    False if twice and visited[node] > 1 and node != "start" else twice,
                )
            # elif twice:
            #     print("tring branch", node)
            #     res += dfs(n, visited, [], False)
        if not node.isupper():
            visited[node] -= 1
        return res

    return dfs("start", visited, [], p == "gold")


for l in lines:
    l, r = l.split("-")
    graph[l].append(r)
    graph[r].append(l)

print("silver", solve(collections.defaultdict(int)))
print("gold", solve(collections.defaultdict(int, {"start": 1}), "gold"))
