import fileinput
import re

lines = [line.strip() for line in fileinput.input()]
silver = 0
for l in lines:
    bluei, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(int, re.findall(
        r'.*(\d+):.*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)', l)[0])
    robots = [1, 0, 0, 0]  # ore, clay, obs, geo
    material = [0, 0, 0, 0]  # ore, clay, obs, geo
    print(bluei)
    for _ in range(24):
        ore, clay, obs, _ = material
        rob = [0]*4
        # build one robot
        if ore >= geo_ore and obs >= geo_obs:
            material[0] -= geo_ore
            material[2] -= geo_obs
            rob[3] += 1
        elif ore >= obs_ore and clay >= obs_clay:
            material[0] -= obs_ore
            material[1] -= obs_clay
            rob[2] += 1
        elif ore >= clay_ore:
            material[0] -= clay_ore
            rob[1] += 1
        elif ore >= ore_ore:
            material[0] -= ore_ore
            rob[0] += 1
        # produce
        for i in range(4):
            material[i] += robots[i]
        robots = list(sum(x) for x in zip(robots, rob))

        print(material, robots)

    silver += material[-1]*bluei

print(silver)
