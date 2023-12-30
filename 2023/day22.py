import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect
from dataclasses import dataclass

lines = [l.strip() for l in fileinput.input()]
bricks = []

def intersect(a,b,c,d): # check two ranges intersect
   # print((x1, x2, y1, y2), max(x1, x2) >= min(y1, y2))
    x1 = min(a,b)
    x2 = max(a,b)
    y1 = min(c,d)
    y2 = max(c,d)
    return max(x1,y1) <= min(x2,y2)

def collide(brick1, brick2):
    return intersect(brick1.x, brick1.endx, brick2.x, brick2.endx) and intersect(brick1.y, brick1.endy, brick2.y, brick2.endy) and intersect(brick1.z, brick1.endz, brick2.z, brick2.endz)
    
@dataclass(frozen=True)
class Brick:
    id: int
    
    x: int
    y: int
    z: int

    endx: int
    endy: int
    endz: int

    def above(self, other):
        return intersect(self.x, self.endx, other.x, other.endx) and intersect(self.y, self.endy, other.y, other.endy) and other.endz <  self.z

    def below(self,other):
        return intersect(self.x, self.endx, other.x, other.endx) and intersect(self.y, self.endy, other.y, other.endy) and self.endz < other.z
        
    # def __repr__(self):
    #     return f"{self.id}"

endmp = defaultdict(list)
startmp = defaultdict(list)
for id,line in enumerate(lines):
    x,y,z,endx,endy,endz = (int(i) for i in re.findall(r'(\d+)', line))
    #print(x,y,z,endx,endy,endz)
    
    if z < endz:
        bricks.append(Brick(id, int(x), int(y), int(z), int(endx), int(endy), int(endz)))
    else:
        bricks.append(Brick(id, int(endx), int(endy), int(endz), int(x), int(y), int(z)))

graph = defaultdict(list)
graph2 = defaultdict(set)
inedge = defaultdict(int)
bricks.sort(key=lambda b: (b.z))

# print(bricks[1].above(bricks[2]), bricks[1], bricks[2])
bricks_still = []
crits = set()
#check order of brick drop
for i,b in enumerate(bricks):
    cur=0
    while b.z-cur > 1 and all(not collide(Brick(b.id, b.x,b.y,b.z-cur-1, b.endx,b.endy,b.endz-cur-1),b2) for b2 in endmp[b.z-cur-1]):
        cur+=1
    c = Brick(b.id, b.x,b.y,b.z-cur, b.endx,b.endy,b.endz-cur)
    #print(endmp[b.z-cur-1])
    lands = 0
    crit_cur = set()
    for b2 in endmp[b.z-cur-1]:
        if collide(Brick(b.id, b.x,b.y,b.z-cur-1, b.endx,b.endy,b.endz-cur-1),b2):
            #print('', c ,'landed on', b2)
            crit_cur.add(b2)
    if len(crit_cur) <2 :
        for ctz in crit_cur:
            crits.add(ctz)
    endmp[b.endz-cur].append(c)
    startmp[b.z-cur].append(c)
    bricks_still.append(c)
    # if i ==30:
    #     break

inedge = defaultdict(int)
for b in bricks_still:
    for nei in startmp[b.endz+1]:
        if nei.above(b):
            #print(nei ,'is above', b)
            graph[b].append(nei)
            inedge[nei] +=1
            graph2[nei].add(b)
print(len(bricks_still) - len(crits))

s = set(bricks_still)
# print(graph)
# print(graph2)

def count(brick):
    inedgec = inedge.copy()
    q = [brick]
    cnt = 0
    while q:
        q2 = []
        for b in q:
            cnt+=1
            for nei in graph[b]:
                inedgec[nei]-=1
                if not inedgec[nei]:
                    q2.append(nei)
        q = q2
    return cnt-1


print(sum(count(b) for b in crits))
wrong = 1175,1222,846, 415, 413  # too high
#for all cubes, check all , all candidate cubes cannot be above each other in order to be above us

wrong2 = 104661
    
    
