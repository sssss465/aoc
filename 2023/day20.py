import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect

# Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

lines = [l.strip() for l in fileinput.input()]
graph = defaultdict(list)
kind = defaultdict(str) # stores the type of module based on name
inedge = defaultdict(int)

low=0
high=0
for line in lines:
    l,r = line.split(' -> ')
    r = [i.strip() for i in r.split(',')]
    kind[l[1:]] = l[0]
    for i in r:
        graph[l[1:]].append(i)
        inedge[i] +=1
graph['button'].append('roadcaster')
inedge['button'] = -float('inf')
inedge['roadcaster'] = -float("inf")
print(graph,inedge)


state = defaultdict(set) # store state of flipflop and conjunction modules
repeat = {}
def cycle(idx):
    q = deque(['button'])
    l,h = 0,0
    times = 0
    inq = set(['button'])
    rx = False
    while q:
        t = q.popleft()
        s = state[t]
        sig = len(state[t]) < inedge[t]
        #inq.remove(t)
        rx = False
        for nei in graph[t]:
            opt = None
            if kind[t] == '%': # if state empty it means we got low
                if sig:
                    if t in state[nei]:
                        state[nei].remove(t)
                        opt = 'low'
                        l+=1
                    else:
                        state[nei].add(t)
                        opt = 'hi'
                        h+=1
            else:
                if not sig:
                    l +=1
                    if t in state[nei]:
                        state[nei].remove(t)
                    opt = 'low'
                else:
                    h +=1
                    state[nei].add(t)
                    opt = 'hi'
            if opt and not( opt == 'hi' and kind[nei] == '%' ):
                inq.add(nei)
                q.append(nei)
            if opt == 'hi' and nei == 'lx':
                repeat[t] = idx
                if len(repeat) == 4:
                    return l,h,state,rx
            #print(t,opt,nei)
        #print(q,t,s, state)
        times+=1
    return l,h, state, rx

def lcm(list):
    return functools.reduce(lambda x,y: x*y//math.gcd(x,y), list)

lows, highs = 0,0
for i in range(5000):
    ls, hs, _, rx = cycle(i+1)
    lows += ls
    highs += hs

    if i == 999:
        print(lows * highs)
    if len(repeat) == 4:
        print(i)
        print('gold', lcm(repeat.values()))
        break
        

wrong = 628697652 # too low
