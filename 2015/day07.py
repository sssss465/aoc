import fileinput

lines = [l.strip() for l in fileinput.input()]

mp = {}
build = {}


def resolve(node):
    if node.isdigit():
        return int(node)
    if node in build:
        return build[node]
    v = mp[node].split(' ')
    res = ''
    if 'NOT' in v:
        res = ~resolve(v[1])
    elif 'OR' in v:
        res = resolve(v[0]) | resolve(v[2])
    elif 'AND' in v:
        res = resolve(v[0]) & resolve(v[2])
    elif 'LSHIFT' in v:
        res = resolve(v[0]) << int(v[2])
    elif 'RSHIFT' in v:
        res = resolve(v[0]) >> int(v[2])
    else:
        res = resolve(v[0])
    build[node] = res
    return res


for line in lines:
    e = line.split('->')
    name = e[0].strip()
    # print(name)
    out = e[1].strip()
    # print(out)
    mp[out] = name
print(mp)
print(f"silver {resolve('a')}")
