import fileinput

lines = []
for l in fileinput.input():
    lines.append(l.strip())


def run(lines):
    visited = [0]*len(lines)
    p = 0
    acc = 0
    while p < len(lines):
        op, off = lines[p].split(' ')
        off = int(off)
        if visited[p] == 1:
            return False, acc
        visited[p] = 1
        if op == 'nop':
            pass
        elif op == 'acc':
            acc += off
        elif op == 'jmp':
            p += off
            continue
        p += 1
    return True, acc


_, acc = run(lines)
print('silver', acc)

for i in range(len(lines)):
    op, _ = lines[i].split()
    if op == 'nop':
        lines[i] = 'jmp' + lines[i][3:]
    elif op == 'jmp':
        lines[i] = 'nop' + lines[i][3:]
    compl, acc = run(lines)
    if compl:
        print('gold', acc)
        break
    lines[i] = op + lines[i][3:]
