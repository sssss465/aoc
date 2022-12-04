import fileinput

lines = [line.strip() for line in fileinput.input()]
silver = 0
gold = 0
for line in lines:
    a, b = line.split(',')
    l, r = list(map(int, a.split('-'))), list(map(int, (b.split('-'))))
    if r[0] < l[0]:
        l, r = r, l
    silver += 1 if l[1] >= r[1] or l[0] == r[0] else 0
    gold += 1 if max(l[0], r[0]) <= min(l[1], r[1]) else 0
print(f"{silver=}\n{gold=}")
