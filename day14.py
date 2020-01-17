import sys
import collections

graph = collections.defaultdict(dict)

total = collections.defaultdict(int)

for line in sys.stdin:
    line = line.strip().split('=>')
    l1 = line[0].strip().split(',')
    l2 = line[1].strip().split(',')
    for g in l2:
        g = g.strip().split(' ')
        total[g[1]] = 0
        for l in l1:
            l = l.strip().split(' ')
            print(l)
            graph[g[1]][l[1]] = int(l[0])
print(graph)
print(total)


def dfs(node, quantity=1):
    # print('hello', node, quantity)
    if node == 'ORE':
        return quantity

    material = 0
    for mat, quant in graph[str(node)].items():
        material += dfs(mat, quant)
    # print('returning', material*quantity, material, quantity)
    return material


r = dfs('FUEL', 1)
print(r)
