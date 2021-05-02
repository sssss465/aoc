import fileinput
import collections

lines = [1, 20, 11, 6, 12, 0]
# lines = [0, 3, 6]

pos = collections.defaultdict(list)
for i in range(len(lines)):
    pos[lines[i]].append(i+1)

last = lines[-1]
silver = 0
for t in range(len(lines)+1, 30000001):
    p = pos[last]
    cur = 0 if len(p) < 2 else p[-1]-p[-2]
    if len(pos[cur]) >= 10000:
        pos[cur] = [pos[cur][-1]]
    pos[cur].append(t)
    last = cur
    if t == 10:
        silver = last
print('silver', silver)
print('gold', last)
