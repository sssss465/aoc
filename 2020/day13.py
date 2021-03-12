import fileinput

lines = [x for x in fileinput.input()]

early = int(lines[0])
buses = []
for i in lines[1].split(','):
    if i != 'x':
        buses.append(int(i))
