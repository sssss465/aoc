import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
import math


lines = [l.strip() for l in fileinput.input()]

inst = lines[0]
cur =0
gold=0
node = 'AAA'
graph = defaultdict(list)
q = deque()

for i in range(2, len(lines)):
    c,l,r = re.findall(r'(\w\w\w)', lines[i])
    graph[c] = [l,r]
    if c[2] == 'A':
        q.append(c)

while node != 'ZZZ':
    dir = inst[cur%len(inst)]
    if dir == 'L':
        node = graph[node][0]
    else:
        node = graph[node][1]
    cur += 1

print(cur)

def lcm(list):
    return functools.reduce(lambda x,y: x*y//math.gcd(x,y), list)
firsts = [0]*len(q)
while any(i==0 for i in firsts):
    dir = inst[gold%len(inst)]
    q2 = deque()
    for i,e in enumerate(q):
        if e[2] == 'Z' and firsts[i] == 0:
            firsts[i] = gold
        if dir == 'L':
            q2.append(graph[e][0])
        else:
            q2.append(graph[e][1])
    q = q2
    gold+=1
print(firsts)

print(lcm(firsts))
# import timeit
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=100000))
    