import fileinput
import re
from functools import cache
from collections import deque

lines = [line.strip() for line in fileinput.input()]
silver = 0
gold = 1


# @cache
# def dfs(material=(0, 0, 0, 0), robots=(1, 0, 0, 0), day=0, costs=()):
#     if day == 24:  # make this faster somehow
#         return material[-1]
#     # produce
#     bluei, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = costs
#     material = list(material)
#     rob = list(robots)
#     ore, clay, obs, _ = material
#     for i in range(len(robots)):
#         material[i] += robots[i]
#     res = 0
#     if ore >= geo_ore and obs >= geo_obs:
#         material[0] -= geo_ore
#         material[2] -= geo_obs
#         rob[3] += 1
#         res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
#         material[0] += geo_ore
#         material[2] += geo_obs
#         rob[3] -= 1
#     if ore >= obs_ore and clay >= obs_clay:
#         material[0] -= obs_ore
#         material[1] -= obs_clay
#         rob[2] += 1
#         res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
#         material[0] += obs_ore
#         material[1] += obs_clay
#         rob[2] -= 1
#     if ore >= clay_ore:
#         material[0] -= clay_ore
#         rob[1] += 1
#         res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
#         material[0] += clay_ore
#         rob[1] -= 1
#     if ore >= ore_ore:
#         material[0] -= ore_ore
#         rob[0] += 1
#         res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
#         material[0] += ore_ore
#         rob[0] -= 1

#     # do nothing route
#     res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
#     return res

def max_geodes2(blueprint, max_time):
    max_robots = [float("inf")] * 4
    for i in range(3):
        max_robots[i] = max(cost[i] for cost in blueprint)

    max_geodes = 0
    max_size = 0
    q = deque([(
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        0,
    )])

    while q:
        inventory, bots, elapsed = q.popleft()

        for i, costs in enumerate(blueprint):
            if bots[i] == max_robots[i]:
                continue

            wait_time = max([(0 if costs[idx] <= inventory[idx] else
                            ((costs[idx] - inventory[idx] + bots[idx] - 1) //
                            bots[idx] if bots[idx] != 0 else max_time + 1)
            )
                for idx in range(3)
            ])

            new_elapsed = elapsed + wait_time + 1
            if new_elapsed >= max_time:
                continue

            new_inventory = [
                inventory[idx] + bots[idx] * (wait_time + 1) - costs[idx]
                for idx in range(4)
            ]

            new_bots = bots[:]
            new_bots[i] += 1

            remaining_time = max_time - new_elapsed
            if ((remaining_time - 1) * remaining_time) // 2 + new_inventory[3] + remaining_time * new_bots[3] < max_geodes:
                continue

            q.append((new_inventory, new_bots, new_elapsed))
        max_size = max(max_size, len(q))
        geodes = inventory[3] + bots[3] * (max_time - elapsed)
        max_geodes = max(geodes, max_geodes)

    # print("Max size:", max_size)
    return max_geodes


for ii, l in enumerate(lines):
    bluei, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(int, re.findall(
        r'.*?(\d+)', l))
    blueprint = []
    blueprint.append([ore_ore, 0, 0, 0])
    blueprint.append([clay_ore, 0, 0, 0])
    blueprint.append([obs_ore, obs_clay, 0, 0])
    blueprint.append([geo_ore, 0, geo_obs, 0])

    silver += max_geodes2(blueprint, 24)*bluei
    if bluei <= 3:
        gold *= max_geodes2(blueprint, 32)
    # print(silver)

print('silver', silver)
print('gold', gold)
