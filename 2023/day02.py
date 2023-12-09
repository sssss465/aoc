import fileinput
from dataclasses import dataclass, field
from collections import defaultdict
import re

lines = [line+'\n' for line in fileinput.input()]
res = 0
res2 = 0
limit = {'red':12 , 'green':13, 'blue':14}

for il,line in enumerate(lines):
    m = re.findall(r'Game (\d+): |(\d+.*?(?=;|\n))', line)
    good = True
    cnt = defaultdict(int)

    for i in range(1, len(m)):
        for a in m[i][1].split(','):
            a,c = a.strip().split(' ')
            if int(a) > limit[c]:
                good = False
            cnt[c] = max(cnt[c], int(a))
    cur = 1
    for k,v in cnt.items():
        cur *= v
    res2 += cur
    if good:
        res += il+1

print(res)
print(res2)
