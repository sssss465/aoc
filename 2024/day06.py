import fileinput

lines = [list(l.strip()) for l in fileinput.input()]

start = [0,0]
obs = set()

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '^':
            start = [i,j]
            lines[i][j] = '.'
        if lines[i][j] == '#':
            obs.add((i,j))

def run(i,j):
    cur = tuple(start[:])
    d = (-1, 0) # start facing up, turn right every obs
    visited = set()
    while cur[0] >= 0 and cur[0] < len(lines) and cur[1] >= 0 and cur[1] < len(lines[0]):
        state = (cur,d)
        #print(state)
        if state in visited:
            return 1, visited
        visited.add(state)
        while (cur[0] + d[0], cur[1] + d[1]) in obs: # BUG was here!! if there is multiple obstacles we keep turning
            d = (d[1], -d[0])
        cur = (cur[0]+d[0], cur[1]+d[1])
    return 0, visited

silvstate, silvervis = run(-1,-1) 
print(silvstate)
gold = 0
path = set(s[0] for s in silvervis)
print('silver', len(path))
for states in path:
    (i,j)= states
    if [i,j] != start and (i,j) not in obs:
        obs.add((i,j))
        res = run(i,j)[0]
        obs.remove((i,j))
        if res:
            #print(i,j)
            gold+=1
        #gold += 
print('gold', gold)

# 1617 too high
# 1616 too high
