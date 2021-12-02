import fileinput

lines = [*map(lambda l: l.strip(), fileinput.input())]

silver, gold = None, None
hori, vert = 0, 0
hori2, vert2 = 0, 0
aim = 0
for l in lines:
    word = l.split()[0]
    change = int(l.split()[1])
    if word == "forward":
        hori += change
        hori2 += change
        vert2 += aim * change
    elif word == "down":
        vert += change
        aim += change
    else:
        vert -= change
        aim -= change

print(f"silver: {hori * vert}")
print(f"gold: {hori2 * vert2}")
