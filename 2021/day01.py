import fileinput

lines = [*map(lambda l: l.strip(), fileinput.input())]
lines = [int(l) for l in lines]

silver = 0
gold = 0

for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i-1]):
        silver += 1
for i in range(2, len(lines)-1):
    if lines[i]+lines[i-1]+lines[i+1] > lines[i-1] + lines[i-2] + lines[i]:
        gold += 1

print("silver", silver)
print("gold", gold)
