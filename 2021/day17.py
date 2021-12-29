targetx = [81, 129]
targety = [-150, -108]
# targetx = [135, 155]
# targety = [-102, -78]


def good(vx, vy):
    px, py = 0, 0
    maxy = 0
    while px <= targetx[1] and py >= targety[0]:
        px += vx
        py += vy
        maxy = max(maxy, py)
        vx = max(vx - 1, 0)
        vy -= 1
        if (
            px >= targetx[0]
            and px <= targetx[1]
            and py >= targety[0]
            and py <= targety[1]
        ):
            return (True, maxy)
    return (False, maxy)


# print(good(6, 9))

mmy = 0
gold = 0
for i in range(200):
    for j in range(-200, 200):
        t, maxy = good(i, j)
        if t:
            mmy = max(mmy, maxy)
            gold += 1
print("silver", mmy)
print("gold", gold)
