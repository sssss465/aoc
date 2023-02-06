import fileinput
import re
from functools import cache
from collections import deque

lines = [line.strip() for line in fileinput.input()]
silver = 0


@cache
def dfs(material=(0, 0, 0, 0), robots=(1, 0, 0, 0), day=0, costs=()):
    if day == 24:  # make this faster somehow
        return material[-1]
    # produce
    bluei, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = costs
    material = list(material)
    rob = list(robots)
    ore, clay, obs, _ = material
    for i in range(len(robots)):
        material[i] += robots[i]
    res = 0
    if ore >= geo_ore and obs >= geo_obs:
        material[0] -= geo_ore
        material[2] -= geo_obs
        rob[3] += 1
        res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
        material[0] += geo_ore
        material[2] += geo_obs
        rob[3] -= 1
    if ore >= obs_ore and clay >= obs_clay:
        material[0] -= obs_ore
        material[1] -= obs_clay
        rob[2] += 1
        res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
        material[0] += obs_ore
        material[1] += obs_clay
        rob[2] -= 1
    if ore >= clay_ore:
        material[0] -= clay_ore
        rob[1] += 1
        res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
        material[0] += clay_ore
        rob[1] -= 1
    if ore >= ore_ore:
        material[0] -= ore_ore
        rob[0] += 1
        res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
        material[0] += ore_ore
        rob[0] -= 1

    # do nothing route
    res = max(res, dfs(tuple(material), tuple(rob), day+1, costs=costs))
    return res


class State:
    def __init__(self, ore=[0, 0, 0, 0], bots=[1, 0, 0, 0], elapsed=0):
        self.ore = ore
        self.bots = bots
        self.elapsed = elapsed


for l in lines:
    bluei, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(int, re.findall(
        r'.*(\d+):.*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)', l)[0])
    blueprint = []
    blueprint.append([ore_ore, 0, 0, 0])
    blueprint.append([clay_ore, 0, 0, 0])
    blueprint.append([obs_ore, obs_clay, 0, 0])
    blueprint.append([geo_ore, 0, geo_obs, 0])

    robots = [1, 0, 0, 0]  # ore, clay, obs, geo
    material = [0, 0, 0, 0]  # ore, clay, obs, geo
    print(bluei)
    q = deque([State(ore=[0, 0, 0, 0], bots=[1, 0, 0, 0], elapsed=0)])
    max_time = 24
    max_geodes = 0
    # optimization: dont make more bots than maximum cost of blueprint
    max_robots = [max(i) for i in zip(*blueprint)]
    while q:
        t = q.popleft()
        ore, bots, elapsed = t.ore, t.bots, t.elapsed

        # for each bot run simulation
        for i in range(len(blueprint)):
            # if bots[i] == max_robots[i]:
            #     continue
            costs = blueprint[i]
            wait_time = max([0 if costs[idx] <= ore[idx] else (costs[idx] - ore[idx] + bots[idx] - 1) // bots[idx] if bots[idx] != 0 else max_time + 1
                for idx in range(3)
            ])
            new_elapsed = elapsed + wait_time + 1
            if new_elapsed >= max_time:
                continue
            new_ore = [0]*4
            for j in range(len(bots)):
                new_ore[j] = ore[j] + bots[j]*(wait_time+1) - costs[j]
            new_bots = bots[:]
            new_bots[i] += 1
            q.append(State(new_ore, new_bots, new_elapsed))
        geodes = ore[3] + bots[3]*(max_time-elapsed)
        max_geodes = max(max_geodes, geodes)
        # print(len(q))
    silver += max_geodes*bluei
    print(silver)

print(silver)
