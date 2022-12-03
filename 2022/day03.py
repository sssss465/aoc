import fileinput

lines = [line.strip() for line in fileinput.input()]
silver = 0
for line in lines:
    s1, s2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    r = s1.intersection(s2)
    assert (len(r) == 1)
    c = r.pop()
    o = ord(c)
    if ord('A') <= o <= ord('Z'):
        silver += 27 + o - ord('A')
    else:
        silver += 1 + o - ord('a')
gold = 0
for i in range(0, len(lines), 3):
    s1, s2, s3 = set(lines[i]), set(lines[i+1]), set(lines[i+2])
    r = s1.intersection(s2).intersection(s3)
    assert (len(r) == 1)
    c = r.pop()
    o = ord(c)
    if ord('A') <= o <= ord('Z'):
        gold += 27 + o - ord('A')
    else:
        gold += 1 + o - ord('a')
print(silver)
print(gold)
