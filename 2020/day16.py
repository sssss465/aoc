import fileinput
import collections

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
for tickets in nearby:
    for f in tickets:
        found = False
        for k, v in rules.items():
            good = False
            for r in v:
                lo, hi = map(int, r.split('-'))
                if lo <= f <= hi:
                    good = True
                    break
            if good:
                found = True
                break
        if not found:
            rate += f


print('silver', rate)
