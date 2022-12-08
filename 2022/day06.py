import fileinput
from collections import Counter
lines = [line.strip() for line in fileinput.input()]

for sz in [4, 14]:
    cnt = Counter(lines[0][:sz-1])
    for i in range(sz-1, len(lines[0])):
        cnt[lines[0][i]] += 1
        if len(cnt) == sz:
            print("silver" if sz == 4 else "gold", i+1)
            break
        cnt[lines[0][i-sz+1]] -= 1
        if cnt[lines[0][i-sz+1]] == 0:
            del cnt[lines[0][i-sz+1]]
