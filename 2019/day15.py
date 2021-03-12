from intcode_mod.intcode import Intcode

# wip

dirs = [1, 2, 3, 4]
opposite = {1: 2, 2: 1, 3: 4, 4: 3}
machine = Intcode([2]*100)
machine.read()
r = []
its = 0
for r in machine.run():
    # print(its := its+1)
    its += 1
    pass
print(its)
