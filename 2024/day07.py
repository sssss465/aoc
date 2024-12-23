import fileinput
from functools import cache

lines = [l.strip() for l in fileinput.input()]

# dp?? lmao

silver = 0 
gold=0

def solve(values, target, cur, gold=False):
    if cur == 0:
        return [values[0]]
    res = []
    for choice in solve(values, target, cur-1, gold):
        res.append(values[cur] + choice)
        res.append(values[cur] * choice)
        if gold:
            #print(choice, values[cur], str(choice) + str(values[cur]))
            res.append(int(str(choice) + str(values[cur])))
    return res

for l in lines:
    target, values = l.split(':')
    target = int(target)
    values = values.strip()
    values = values.split(' ')
    values = [int(v) for v in values]
    picks = solve(values, target, cur=len(values)-1)
    picksgold = solve(values, target, cur=len(values)-1, gold=True)
    #print(target, values, picks, picksgold)
    if target in picks:
        #print(picks)
        silver += target
    if target in picksgold:
        #print(picks)
        gold += target

print(silver)
print(gold)
    
    
