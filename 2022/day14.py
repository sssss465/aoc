import fileinput

lines = [line.strip() for line in fileinput.input()]

walls = {}
lowesty = 0
for line in lines:
    coords = []
    for coord in line.split('->'):
        x, y = coord.split(',')
        coords.append((int(x), int(y)))
        lowesty = max(lowesty, int(y))
    for i in range(len(coords)-1):
        startx = min(coords[i][0], coords[i+1][0])
        endx = max(coords[i][0], coords[i+1][0])
        for x in range(startx, endx+1):
            starty = min(coords[i][1], coords[i+1][1])
            endy = max(coords[i][1], coords[i+1][1])
            for y in range(starty, endy+1):
                walls[(x, y)] = True

start = [500, 0]
floor = lowesty + 2
res = 0
for case in ['silver', 'gold']:

    while True:
        cur = start[:]
        while cur[1] < floor:
            if case == 'gold' and cur[1] + 1 == floor:
                break
            if (cur[0], cur[1]+1) not in walls:
                cur[1] += 1
            elif (cur[0]-1, cur[1]+1) not in walls:
                cur = [cur[0]-1, cur[1]+1]
            elif (cur[0]+1, cur[1]+1) not in walls:
                cur = [cur[0]+1, cur[1]+1]
            else:
                break
        if case == 'silver' and cur[1] > lowesty:
            break
        res += 1
        walls[(cur[0], cur[1])] = res
        if case == 'gold' and cur == start:
            break

    print(case, res)
