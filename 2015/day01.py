import fileinput
lines = [line.strip() for line in fileinput.input()]
print(f"silver: {sum(1 if c == '(' else -1 for c in lines[0])}")

cur = 0
for c in enumerate(lines[0]):
    if c[1] == '(':
        cur += 1
    else:
        cur -= 1
    if cur == -1:
        print(f"gold: {c[0] + 1}")
        break
