import fileinput
from collections import defaultdict
lines = []
for line in fileinput.input():
    l = line.strip()
    lines.append(l)
group = defaultdict(int)
lines.append('')
silver = 0
gold = 0
for l in lines:
    if l == '':
        silver += len(group)
        sz = group['size']
        gold += sum([1 if v == sz else 0 for v in group.values()])-1
        group = defaultdict(int)
        continue
    for c in l:
        group[c] += 1
    group['size'] += 1
print('silver', silver)
print('gold', gold)
