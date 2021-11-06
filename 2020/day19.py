import fileinput
import sys
# sys.setrecursionlimit(30)
lines = list(l.split('\n') for l in sys.stdin.read().split('\n\n'))
rules, check = lines

graph = {}
for l in rules:
    rule, match = l.split(':')
    groups = [gp.strip().split(' ')
              for gp in match.split('|')]
    graph[rule] = groups

cache = {}  # compress tree
max_depth = 7


def build(rule='0', been=set(), depth=0, gold=False):
    if rule in been and rule not in cache:
        print('cycle!', rule, been)
    # return []  # no matches due to cycle
    print(rule, depth)
    if depth > max_depth:
        return []
    been.add(rule)
    groups = graph[rule]
    if rule in cache:
        return cache[rule]
    bld = []
    # if gold:
    #     print('hey')
    #     if rule == '8':
    #         print('BUILDING 8 FOR GOLD')
    #         if '42' not in cache:
    #             ft = build('42', been=been, depth=depth+1, gold=gold)
    #         else:
    #             ft = cache['42']
    #         bd = ['']
    #         print('42 FOUND!!!', ft)
    #         for _ in range(5):
    #             bd = [r+c for r in ft for c in bd]
    #         print(bd)
    #         cache['8'] = bd
    #         return bd
    # if rule == '11':
    #     print('BUILDING 11 for GOLD')
    #     left = cache['42'] if '42' in cache else build(
    #          '42', been=been, depth=depth+1, gold=gold)
    #      right = cache['31'] if '31' in cache else build(
    #           '31', been=been, depth=depth+1, gold=gold)

    #       bd = ['']
    #        for _ in range(5):
    #             bd = [l+c+r for l in left for r in right for c in bd]
    #         cache['11'] = bd
    #         return bd

    for gp in groups:  # each or separated group
        cur = ['']
        # print(rule, gp, bld)
        for r in gp:  # each number in the group
            if "a" in r or "b" in r:  # base case
                cache[rule] = [r.strip("\"")]
                return cache[rule]
            c2 = []
            for a in build(r, been, depth+1, gold):
                # print(r, cur, gold)
                for c in cur:
                    c2.append(c + a)
            cur = c2
        for c in cur:
            bld.append(c)
    # print(rule, bld, cache)
    cache[rule] = bld
    if rule in been:
        been.remove(rule)
    return bld


silver = 0
gold = 0

res = set(build())
# print(f"cache: {cache}")
max_len_word = 0
for c in check:
    max_len_word = max(max_len_word, len(c))
    if c in res:
        silver += 1
print('silver', silver)
cache = {}
# graph['8'] = [['42'], ['42', '42'], [
#     '42', '42', '42'], ['42', '42', '42', '42']]
# graph['11'] = [['42', '31'], ['42', '42', '31', '31'],
#                ['42', '42', '42', '31', '31', '31'], ['42', '42', '42', '42', '31', '31', '31', '31']]
graph['8'] = [['42'], ['42', '8']]
graph['11'] = [['42', '31'], ['42', '11', '31']]
res = set(build(rule='0', been=set(), gold=True))
print(res)
for c in check:
    if c in res:
        gold += 1
print('gold', gold)
