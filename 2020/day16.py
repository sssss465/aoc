import fileinput
import collections
from functools import reduce

# what an abomination

lines = [l.strip() for l in fileinput.input()]
rate = 0

rules = {}
mine = 0
nearby = []
group = 0
for l in lines:
    if l == '':
        group += 1
        continue

    def zero(line):
        a, b = line.split(':')
        b = b.strip().split('or')
        rules[a] = [r.strip() for r in b]

    def one(line):
        if line[0] == 'y':
            return
        return [*map(int, line.split(','))]

    def two(line):
        if line[0] == 'n':
            return
        nearby.append([*map(int, line.split(','))])
    grp = [zero, one, two]
    v = grp[group](l)
    if group == 1:
        mine = v
# print(rules, mine, nearby)
ticket_cands = []
for tickets in nearby:
    discard = False
    field_match = [[] for i in range(len(tickets))]
    for field_index, f in enumerate(tickets):
        found = False
        rule_num = 0
        for k, v in rules.items():
            good = False
            for r in v:
                lo, hi = map(int, r.split('-'))
                if lo <= f <= hi:
                    good = True
            if good:
                found = True
                field_match[field_index].append(rule_num)
            rule_num += 1
        if not found:
            rate += f
            discard = True
    if not discard:
        ticket_cands.append(field_match)
res = [0]*len(mine)
# print(ticket_cands)
for i, col in enumerate(zip(*ticket_cands)):
    r = set.intersection(*map(set, col))
    # print(r)
    res[i] = r
    # assert(len(r) == 1)
while any((len(r) > 1 for r in res)):
    for r in res:
        if len(r) == 1:
            v = list(r)[0]
            for s in res:
                if r != s and v in s:
                    s.remove(v)
res2 = [0]*len(mine)
for i, r in enumerate(res):
    r = list(r)
    res2[r[0]] = mine[i]
res = res2
print(res)
cnt = 0
rr = []
for k, v in rules.items():
    k = k.split(' ')
    # print(k)
    if k[0] == 'departure':
        rr.append(res[cnt])
    cnt += 1


print('silver', rate)
print('gold', reduce(lambda l, r: l*r, rr))
