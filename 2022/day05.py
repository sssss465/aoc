import fileinput
import re
from collections import defaultdict, deque
lines = [line for line in fileinput.input()]

i = 0
d = defaultdict(deque)
d2 = defaultdict(deque)
while i < len(lines):
    if lines[i][1] == '1':
        i += 2
        break
    hop = 0
    for j in range(0, len(lines[i]), 4):
        hop += 1
        if lines[i][j+1] == ' ':
            continue
        d[hop].appendleft(lines[i][j+1])
        d2[hop].appendleft(lines[i][j+1])
    i += 1
for i in range(i, len(lines)):
    l = re.findall(r' \d+', lines[i])
    l = list(map(int, l))
    d2[l[2]] += list(d2[l[1]])[-l[0]:]
    for m in range(l[0]):
        d[l[2]].append(d[l[1]].pop())
        d2[l[1]].pop()
print('silver:', ''.join(
    [d[i][-1] if d[i] else '' for i in range(1, max(d)+1)]))
print('gold:', ''.join(
    [d2[i][-1] if d2[i] else '' for i in range(1, max(d2)+1)]))
