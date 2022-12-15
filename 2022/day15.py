import fileinput
import re
import bisect

lines = [line.strip() for line in fileinput.input()]
sensors = {}
dist = {}  # distance from sensor to nearest beacon
beacons = set()
left, right = float('inf'), -float('inf')  # bound graph
for l in lines:
    l1, l2, l3, l4 = map(int, re.findall(r'([+-]*\d+)', l))
    sensors[(l1, l2)] = (l3, l4)
    beacons.add((l3, l4))
    dist[(l1, l2)] = abs(l4 - l2) + abs(l3 - l1)
# beacons cant exist where there has been closer beacon already reported to a sensor


def solve(y=2000000):
    def bound(sensor) -> list[list[int]]:
        dy = abs(sensor[1] - y)
        d = dist[sensor]
        dx = d - dy
        if dx < 0:
            return []
        return [sensor[0] - dx, sensor[0] + dx]
    ranges = sorted([r for s in sensors if (r := bound(s))])
    # merge ranges
    res = []
    for r in ranges:
        if not res or res[-1][1]+1 < r[0]:
            res.append(r)
        else:
            res[-1][1] = max(res[-1][1], r[1])
    return res


search = 4000000

print('silver', sum([r[1] - r[0] for r in solve()]))
for y in range(0, search+1):
    bounds = solve(y)
    lb = bisect.bisect_left(bounds, [0, float('inf')])-1
    rb = bisect.bisect_left(bounds, [search, float('inf')])-1
    if len(bounds) > 1:
        x = (bounds[rb][0] + bounds[lb][1]) // 2
        gold = x*4000000 + y
        print('gold', gold)
        break
