import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect
import heapq

lines = [[int(j) for j in l.strip()] for l in fileinput.input()]

grid = lines

#print(grid)


def dijkstra(end = (len(grid)-1, len(grid[0])-1),small=1,big=3 ):

    q = [(0, (0,0), (-1,-1), 0)] # weight, position, last move, # of last moves 
    # modified dijkstra where last move cannot be done more than 3x 
    weight = defaultdict(lambda: float('inf'))
    weight[(0,0)] = 0
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    prev = {}
    res = float('inf')
    seen = set()
    while q:
        wt, cur, last_mov, last_times = heapq.heappop(q)
        #print(wt, cur, last_mov, last_times)
        if (cur, last_mov) in seen:
            continue
        seen.add((cur, last_mov))
        if cur == end:
            c = cur
            return wt
        for x,y in dirs:
            curw = 0
            if last_mov == (x,y) or last_mov == (-x,-y):
                continue
            for step in range(1,big+1):
                nx, ny = cur[0] + x*step, cur[1] + y*step
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                curw += grid[nx][ny]
                # if (x,y) == last_mov and last_times >= 3:
                #     continue
                if small <= step <= big and ((nx,ny), (x,y)) not in seen:
                    h = wt + curw # we need to add weights that may be greater in the next position
                    # because it may lead to a more favorable position (different turns) in the future
                    #weight[(nx,ny)] = h
                    heapq.heappush(q, (h, (nx,ny), (x,y), step))
    
print(dijkstra())
print(dijkstra(small=4, big=10))
