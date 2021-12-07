import fileinput

lines = [l.strip() for l in fileinput.input()]

silver = 10e10
s = list(map(int, lines[0].split(",")))
gold = 10e10

avg = 0
for c in s:
    avg += c
avg //= len(s)
for t in range(min(s), max(s) + 1):
    bd = 0
    bd2 = 0
    for c in s:
        bd += abs(c - t)
        sm = min(c, t)
        b = max(c, t)
        n = b - sm
        bd2 += n * (n + 1) // 2
    silver = min(silver, bd)
    gold = min(gold, bd2)

print("silver", silver)
print("gold", gold)
