import fileinput

lines = [l.strip() for l in fileinput.input()]

silver = 0
gold = 0
for line in lines:
    silver += len(line) - len(eval(line))
    gold += 2 + line.count('\\') + line.count('"')
print(f"silver: {silver}")
print(f"gold: {gold}")
