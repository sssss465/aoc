import fileinput
import functools

lines = [line.strip() for line in fileinput.input()]


def area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)


silver = 0
gold = 0
for l in lines:
    silver += area(*map(int, l.split('x')))
    lst = list(map(int, l.split('x')))
    lst.remove(max(lst))
    gold += 2*lst[0] + 2*lst[1] + \
        functools.reduce(lambda x, y: x*y, map(int, l.split('x')))
print(f"silver: {silver}")
print(f"gold: {gold}")
