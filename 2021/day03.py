import fileinput
import collections

lines = [*map(lambda l: l.strip(), fileinput.input())]
mp = collections.defaultdict(int)
for l in lines:
    for i, v in enumerate(l):
        if v == "1":
            mp[i] += 1
gamma = []
epsilon = []
for i in range(len(lines[0])):
    if mp[i] > len(lines) // 2:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")

gamma = "".join(gamma)
gamma = int(gamma, 2)
epsilon = "".join(epsilon)
epsilon = int(epsilon, 2)


def bit_criteria(big=True):
    i = 0
    values = lines[:]
    while i < len(lines[0]) and len(values) > 1:
        bin1 = []
        bin2 = []
        for j in range(len(values)):
            if values[j][i] == "1":
                bin1.append(values[j])
            else:
                bin2.append(values[j])
        if len(bin1) > len(bin2):
            values = bin1 if big else bin2
        elif len(bin1) < len(bin2):
            values = bin2 if big else bin1
        else:
            values = bin1 if big else bin2
        i += 1
    return int(values[0], 2)


print("silver: ", gamma * epsilon)
print("gold: ", bit_criteria() * bit_criteria(False))
