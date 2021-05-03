import fileinput
from collections import *

lines = []
for line in fileinput.input():
    lines.append(line.strip().rstrip('.'))
d = defaultdict(list)
for l in lines:
    k, v = l.split('contain')
    vs = v.split(',')
    vs = [(i+'s').strip() if i[-1] != 's' else i.strip() for i in vs]
    d[k.strip()] = vs
cache = set()


def dfs(bag):
    bag = bag.strip()
    q, bag = bag.split(' ', 1)
    if q == 'no':  # no other bags
        return False
    if bag in cache or bag == 'shiny gold bag' or bag == 'shiny gold bags':
        return True
    # print('going through', bag)
    for b in d[bag]:
        if dfs(b):
            cache.add(bag)
            return True
    return False


def inside(bag):
    if bag == 'no other bags':
        return 0
    q, bag = bag.split(' ', 1)
    q = int(q)
    bag = bag.strip()
    if bag in cache:
        return q*cache[bag]
    res = q
    for b in d[bag]:
        res += q * inside(b)
    cache[bag] = res // q
    return res


gold = 0
silver = 0
for k, v in d.items():
    if k == 'shiny gold bags':
        continue
    k = '1 ' + k
    if dfs(k):
        silver += 1
print('silver', silver)
cache = {}
print('gold', inside('1 shiny gold bags')-1)
