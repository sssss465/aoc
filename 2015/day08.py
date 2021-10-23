import fileinput

lines = [l.strip() for l in fileinput.input()]

silver = 0

for line in lines:
    silver += len(line) - len(eval(line))
print(f"silver: {silver}")
