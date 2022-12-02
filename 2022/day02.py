import fileinput
from collections import defaultdict, Counter

lines = [line.strip() for line in fileinput.input()]
rock = {'C': 'S', 'Z': "S", 'A': 'R', 'B': 'P',  'X': 'R', 'Y': 'P'}
beats = {'R': 'S', 'P': 'R', 'S': 'P'}
loses = {'R': 'P', 'P': 'S', 'S': 'R'}
pts = {'R': 1, 'P': 2, 'S': 3}
silver = 0
gold = 0

for line in lines:
    l, r = line.split()
    l = rock[l]
    r = rock[r]
    if r == 'R':
        rg = beats[l]
    elif r == 'P':
        rg = l
    else:
        rg = loses[l]
    silver += (6 if beats[r] == l else (l == r) * 3) + pts[r]
    gold += (6 if beats[rg] == l else (l == rg) * 3) + pts[rg]
print('silver', silver)
print('gold', gold)

# N = {"A": " CAB", "B": " ABC", "C": " BCA"}
# V = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


# def p(o, y):
#     if o == y:
#         return 3+y
#     if o == 1+(y+1) % 3:
#         return 6+y
#     return 0+y


# T1 = 0
# T2 = 0
# for i in INPUT.splitlines():
#     T1 += p(V[i[0]], V[i[2]])
#     T2 += p(V[i[0]], V[N[i[0]][V[i[2]]]])
# print(T1, T2)
