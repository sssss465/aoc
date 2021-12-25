import fileinput
from collections import Counter, defaultdict
lines = [l.strip() for l in fileinput.input()]
mp = {}
template = lines[0]
for l in lines[2:]:
    l,r = l.split(' -> ')
    mp[l] = r
pairs = defaultdict(int)
for i in range(len(template)-1):
    pairs[template[i:i+2]] +=1 
for o in range(40):
    # cur = []
    # for i in range(len(template)-1):
    #     p = template[i:i+2]
    #     cur.append(template[i])
    #     if p in mp:
    #         cur.append(mp[p])
    # cur.append(template[-1])
    # template = ''.join(cur)
    updates = []
    for k,v in pairs.items():
        if k in mp:
            m = mp[k]
            updates.append((k, -v))
            updates.append((k[0] + m, v))
            updates.append((m + k[1], v))
    for k,v in updates:
        pairs[k] += v
    # print(pairs)
    if o == 9 or o == 39:
        # print(pairs)
        # c = Counter(template)
        c = defaultdict(int)
        for k,v in pairs.items():
            c[k[0]] += v
        c[template[-1]] += 1
        small = min(c.values())
        big = max(c.values())
        print('silver' if o == 9 else 'gold', big - small)
    
