import fileinput

cases = []
for line in fileinput.input():
    cases.append(int(line.strip()))

s = set()
for i, a in enumerate(cases):
    if 2020-a in s:
        print(f"part1: {(2020-a) * a}")
    for b in cases[i+1:]:
        if 2020 - (a+b) in s:
            print(f"part2: {(2020-(a+b)) * a * b}")
    s.add(a)
