import fileinput

lines = [l.strip() for l in fileinput.input()]

vowels = {'a', 'e', 'i', 'o', 'u'}
forbid = ['ab', 'cd', 'pq', 'xy']
silver = 0
gold = 0


def gold_condition(word):
    between = False
    for i in range(len(word) - 2):
        if word[i] == word[i + 2] and word[i+1] != word[i]:
            between = True
            break
    for i in range(len(word) - 2):
        if word[i:i+2] in word[i+2:]:
            return between
    return False


for l in lines:
    if l == '':
        continue
    vowel = 0
    twice = False
    bad = False
    for i in range(len(l) - 1):
        if l[i] in vowels:
            vowel += 1
        if l[i] == l[i + 1]:
            twice = True
    if l[len(l)-1] in vowels:
        vowel += 1
    for f in forbid:
        if f in l:
            bad = True
            break
    if not bad and vowel >= 3 and twice:
        silver += 1
    if gold_condition(l):
        gold += 1
print(f"Silver: {silver}")
print(f"Gold: {gold}")
