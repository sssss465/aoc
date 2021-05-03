import fileinput
lines = []
for line in fileinput.input():
    l = line.strip()
    lines.append(int(l))

preamble = 25


def good(num, st):
    d = {}
    for i in range(st-preamble, st):
        if num-lines[i] in d:
            return True
        d[lines[i]] = i
    return False


silver = 0

for i in range(preamble, len(lines)):
    v = lines[i]
    if not good(v, i):
        silver = v
        print('silver', v)
        break

slow, fast, d = 0, 0, {}
acc = 0
for i, v in enumerate(lines):
    acc += v
    if acc - silver in d:
        slow = d[acc-silver]
        fast = i+1
        break
    d[acc] = i

print('gold', min(lines[slow:fast]) + max(lines[slow:fast]))
