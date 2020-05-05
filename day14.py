# https://adventofcode.com/2019/day/14
import math
import collections as cl
import sys

from collections import deque

graph = cl.defaultdict(list)
total = cl.defaultdict(int)
total_fuel = 0
for Line in sys.stdin:
    # store each pair
    Mats, Recp = [[[int(Pr.split(' ')[0]), Pr.split(' ')[1]] for Pr in
                   Sd.strip().split(", ")] for Sd in Line.split('=>')]
    for quantity_recv, elem_recv in Recp:
        total[elem_recv] = 0
        if elem_recv == "FUEL":
            total_fuel = quantity_recv
        graph[elem_recv] = [quantity_recv, []]
        for quantity_mat, elem_mat in Mats:
            graph[elem_recv][1].append([quantity_mat, elem_mat])
# print(graph, total)
r = cl.defaultdict(int)
have = cl.defaultdict(int)
# def bfs(graph, total_fuel):
#     q = deque()
#     q.append(graph['FUEL'])
#     res = 0
#     while len(q) > 0:
#         cur_quant, curproducts = q.popleft()
#         print(q, "     ",  curproducts)
#         for quant, prod in curproducts:
#             if prod == 'ORE':
#                 continue
#             if graph[prod][1][0][1] == 'ORE':
#                 r[prod] += cur_quant*quant
#             q.append([cur_quant * quant, graph[prod][1]])
#     return res


def Simulate(Quantity):
    Tree = cl.defaultdict(int, {'FUEL': Quantity})
    while not all(Pt == "ORE" or Tree[Pt] <= 0 for Pt in Tree):
        for Material, Quantity in Tree.copy().items():
            # print(Material, Quantity, Tree)
            if Material == "ORE":
                continue
            Coeff, Products = graph[Material]
            rTimes = math.ceil(Quantity / Coeff)
            for Amnt, Element in Products:
                Tree[Element] += Amnt * rTimes
            Tree[Material] -= rTimes * Coeff
    # print(Tree)
    return Tree["ORE"]


# res = 0
# print(bfs(graph, total_fuel))
# for k, v in r.items():
#     quant, prods = graph[k]
#     ore_amt = prods[0][0]
#     big = math.ceil(v / quant)
#     print(k, v, big)
#     res += big * ore_amt
Steps, Order = cl.defaultdict(set), cl.defaultdict(list)


def Walk(Pt, n=0):
    for _, X in graph[Pt][1]:
        if X in graph:
            Walk(X, n+1)
    Steps[Pt].add(n)


Walk("FUEL")
for k, v in Steps.items():
    Order[max(v)].append(k)
low = 10**12 // Simulate(1)
high = 10*low
while Simulate(high) < 1e12:
    low = high
    high = 10*low
while low < high:
    mid = (low+high) // 2
    ore = Simulate(mid)
    if ore < 1e12:
        low = mid+1
    else:
        high = mid
print(low, high)
print(Simulate(high))

print("Silver:", Simulate(total_fuel))
print("Gold:", int(high-1))
