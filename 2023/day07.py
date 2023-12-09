import fileinput
from collections import Counter
import functools

cards = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2][::-1]
cards = [str(c) for c in cards]
cards2 = ['A', 'K', 'Q', 'T', 9, 8, 7, 6, 5, 4, 3, 2, 'J'][::-1]
cards2 = [str(c) for c in cards2]
lines = [l.strip().split(' ') for l in fileinput.input()]

def score1(cnt):
    if 5 in cnt.values():
        return 6
    if 4 in cnt.values():
        return 5
    if 3 in cnt.values() and 2 in cnt.values():
        return 4
    if 3 in cnt.values():
        return 3
    c = Counter(cnt.values())
    if c[2] == 2:
        return 2
    if 2 in cnt.values():
        return 1
    return 0

def score2(cnt): # naive backtracking
    if cnt['J'] == 0 or cnt['J'] == 5:
        return score1(cnt)
    res = 0
    for k,v in cnt.items():
        if k == 'J':
            continue
        cnt['J']-=1
        cnt[k]+=1
        res = max(res, score2(cnt))
        cnt[k]-=1
        cnt['J']+=1
    return res

def score2(cnt): # greedy 
    if cnt['J'] == 0 or cnt['J'] == 5:
        return score1(cnt)
    extra = cnt['J']
    cnt['J'] = 0
    for k,v in cnt.items():
        if v == max(cnt.values()):
            cnt[k] += extra
            return score2(cnt)
        
def compare(card1, card2):
    c1 = card1[0]
    c2 = card2[0]

    c1c = Counter(c1)
    c2c = Counter(c2)
    
    s1 = score(c1c)
    s2 = score(c2c)
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        for i in range(len(c1)):
            if cards.index(c1[i]) < cards.index(c2[i]):
                return -1
            elif cards.index(c1[i]) > cards.index(c2[i]):
                return 1
        return 0
cards, score = cards, score1 # i love global state
lines.sort(key=functools.cmp_to_key(compare))
cards, score = cards2, score2 # i love global state
lines2 = sorted(lines, key=functools.cmp_to_key(compare))
silver = 0
gold = 0
for i in range(len(lines)):
    silver += (i+1)*int(lines[i][1])
    gold += (i+1)*int(lines2[i][1])
print(silver)
print(gold)
