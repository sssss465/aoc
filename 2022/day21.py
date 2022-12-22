import fileinput
import sys

sys.setrecursionlimit(10000)

lines = [line.strip() for line in fileinput.input()]

mp = {}

for l in lines:
    k, v = l.split(': ')
    k = k.strip()
    v = v.strip()
    if not ('*' in v or '+' in v or '/' in v or '-' in v):
        v = int(v)
    else:
        v = [v[5].strip(), v[:4].strip(), v[7:].strip()]
    mp[k] = v


def dfs(k):
    if type(mp[k]) is int:
        return mp[k]
    else:
        op = mp[k][0]
        if op == '+':
            return dfs(mp[k][1]) + dfs(mp[k][2])
        if op == '-':
            return dfs(mp[k][1]) - dfs(mp[k][2])
        if op == '/':
            return dfs(mp[k][1]) // dfs(mp[k][2])
        if op == '*':
            return dfs(mp[k][1]) * dfs(mp[k][2])
    return None


mp2 = {}  # accumulated result for that node, whether or not it is on humn path


def dfs2(k):
    if type(mp[k]) is int:
        if k == 'humn':
            mp2[k] = mp[k], True
            return mp[k], True
        mp2[k] = mp[k], False
        return mp[k], False
    else:
        op = mp[k][0]
        left, hmnl = dfs2(mp[k][1])
        right, hmnr = dfs2(mp[k][2])
        if k == 'root':
            return left+right, True
        if op == '+':
            mp2[k] = left + right, hmnl or hmnr
            return left + right, hmnl or hmnr
        if op == '-':
            mp2[k] = left - right, hmnl or hmnr
            return left - right, hmnl or hmnr
        if op == '/':
            mp2[k] = left // right, hmnl or hmnr
            return left // right, hmnl or hmnr
        if op == '*':
            mp2[k] = left * right, hmnl or hmnr
            return left * right, hmnl or hmnr


print('silver', dfs('root'))
# mp['root'][0] = '+'  # change the operation to addition
print('silver', target := dfs2('root')[0])
# traverse from the tree from the root to humn
# undo the operation that was done
cur = 'root'
while cur != 'humn':
    op, lnode, rnode = mp[cur]
    lefthumn = mp2[lnode][1]
    if cur != 'root':
        if op == '+':
            if lefthumn:
                target -= mp2[rnode][0]
            else:
                target -= mp2[lnode][0]
        if op == '-':
            if lefthumn:
                target += mp2[rnode][0]
            else:
                target = mp2[lnode][0] - target
        if op == '/':
            if lefthumn:
                target *= mp2[rnode][0]
            else:
                target = mp2[lnode][0] / target
        if op == '*':
            if lefthumn:
                target //= mp2[rnode][0]
            else:
                target //= mp2[lnode][0]
    else:
        target = mp2[lnode][0] if not lefthumn else mp2[rnode][0]

    if lefthumn:
        cur = lnode
    else:
        cur = rnode

print('gold', target)
