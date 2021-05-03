import fileinput
from dataclasses import dataclass

silver = 0
lines = []
for line in fileinput.input():
    lines.append(line.strip())
lines.append('')
recs = []
cur_rec = {}
for l in lines:
    if len(l) == 0:
        if len(cur_rec) == 8 or (len(cur_rec) == 7 and 'cid' not in cur_rec):
            silver += 1
            recs.append(cur_rec.copy())
        cur_rec = {}
        continue
    for k, v in [t.split(':') for t in l.split(' ')]:
        cur_rec[k] = v
print('silver', silver)


def good(r):
    # an abomination @shekeru
    good = True
    if not (len(r['byr']) == 4 and r['byr'].isdigit() and 1920 <= int(r['byr']) <= 2002):
        return False
    if not (len(r['iyr']) == 4 and r['iyr'].isdigit() and 2010 <= int(r['iyr']) <= 2020):
        return False
    if not (len(r['eyr']) == 4 and r['eyr'].isdigit() and 2020 <= int(r['eyr']) <= 2030):
        return False
    ht, unit = r['hgt'][:-2], r['hgt'][-2:]
    if unit not in ['cm', 'in'] or (not ht.isdigit()):
        return False
    if unit == 'cm' and not 150 <= int(ht) <= 193:
        return False
    if unit == 'in' and not 59 <= int(ht) <= 76:
        return False
    if not (len(r['hcl']) == 7 and r['hcl'][0] == '#' and all([i.isdigit() or i in ['a', 'b', 'c', 'd', 'e', 'f'] for i in r['hcl'][1:]])):
        return False
    if r['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not r['pid'].isdigit():
        return False
    if len(r['pid']) != 9:
        return False
    return True


print(recs)
gold = 0

for i, r in enumerate(recs):
    print(i)
    if good(r):
        gold += 1

print('gold', gold)
