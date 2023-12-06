import fileinput
import re
import bisect

lines = [l.strip() for l in fileinput.input()]
t2 = int(''.join([str(i) for i in re.findall(r'(\d+)', lines[0])]))
d2 = int(''.join([str(i) for i in re.findall(r'(\d+)', lines[1])]))

times = [int(i) for i in re.findall(r'(\d+)', lines[0])]
dists = [int(i) for i in re.findall(r'(\d+)', lines[1])]

silver = 1
for i,t in enumerate(times):
    cur = 0
    for j in range(t):
        if j * (t-j) > dists[i]:
            cur+=1
    silver*=cur

def bisect(rr=False):
    left=0
    right = t2
    while left < right:
        mid = (left+right)//2
        if (not rr and mid * (t2 - mid) < d2) or (rr and mid * (t2-mid) > d2 ):
            left = mid+1
        else:
            right = mid
    return left
    
start = bisect()
end = bisect(start)
gold = end-start

print(silver)
print(gold)
