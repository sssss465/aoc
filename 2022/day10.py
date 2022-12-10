import fileinput

lines = [line.strip() for line in fileinput.input()]

X, cycle, silver, screen = 1, 0, 0, [' ']*240
for l in lines:
    cmd = l
    v = 0
    if l != 'noop':
        cmd, v = l.split()
    for i in range(2 if cmd == 'addx' else 1):
        if (cycle+1) % 40 == 20:  # we check after cycles
            silver += (cycle+1)*X
        if cycle % 40 in (X-1, X, X+1):
            screen[cycle] = '#'
        cycle += 1
    X += int(v)
print('silver :', silver)
print('gold')
for i in range(0, 240, 40):
    print(''.join(screen[i:i+40]))
