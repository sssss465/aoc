import fileinput
from functools import reduce

lines = [l.strip() for l in fileinput.input()]


def score(line):
    st = []
    mp = {")": 3, "]": 57, "}": 1197, ">": 25137}
    mp2 = {")": 1, "]": 2, "}": 3, ">": 4}
    mp3 = {"(": ")", "[": "]", "{": "}", "<": ">"}
    silver = 0
    for c in line:
        if c not in mp:
            st.append(c)
        else:
            if mp3[st[-1]] == c:
                st.pop()
            else:
                silver = mp[c]
                st = []
                break
    g = [mp2[mp3[i]] for i in st[::-1]]
    return (silver, reduce(lambda x, y: x * 5 + y, g, 0))


silver = 0
gold = []
for l in lines:
    l = list(l)
    s, g = score(l)
    silver += s
    if g != 0:
        gold.append(g)
gold = sorted(gold)
print("silver", silver)
print("gold", gold[len(gold) // 2])
