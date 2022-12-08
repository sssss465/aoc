from enum import Enum
from collections import defaultdict
from dataclasses import dataclass

with open("7") as f:
    commands = f.read().split('$')


@dataclass
class File():
    name: str
    size: int
    dir: bool = False


# Initialize the current directory and the dir_sizes dictionary
current_dir = ['/']
dir_sizes = defaultdict(list)
CAP = 70000000
MIN = 30000000
# Initialize the total size of all directories with a total size of at most 100000
total_size = 0
gold = float('inf')

# Process each command
for command in commands[1:]:
    # Split the command into a command and arguments
    cmd, *files = command.strip(' ').split('\n')
    cmd, dir = cmd.split() if ' ' in cmd else (cmd, '')
    #print(cmd, dir, files)
    if cmd == 'ls' and len(files) >= 2:  # last line has no return
        files.pop()
    # Handle "cd" commands
    if cmd == "cd":
        # Check if we are moving to the root directory
        if dir == '/':
            current_dir = ['/']
        elif dir == '..':
            current_dir.pop()
        else:
            current_dir.append(dir + '/')
    # Handle "ls" commands
    elif cmd == "ls":
        # Parse the output of the "ls" command
        for entry in files:
            # Check if the entry is a file or a directory
            l, r = entry.split()
            if l == 'dir':
                dir_sizes[''.join(current_dir)].append(File(r, 0, True))
            else:
                dir_sizes[''.join(current_dir)].append(File(r, int(l)))
# Print the total size of all directories with a total size of at most 100000

USED = 0


def dfs(dir='/', g=False) -> int:
    global total_size, gold, USED, dirrs
    cur = 0
    for file in dir_sizes[dir]:
        if file.dir:
            cur += dfs(dir + file.name + '/', g)
        else:
            cur += file.size
    if not g and cur <= 100000:
        total_size += cur
        # print(dir, cur)
    if g and CAP - USED + cur >= MIN:
       # print(cur, gold, CAP - USED, CAP - USED + cur, MIN)
        gold = min(gold, cur)
    return cur


USED = dfs(dir='/')
# print(USED, MIN - CAP, MIN - CAP + USED, MIN - 26840445 - 3180034, MIN)
dfs(dir='/', g=True)
print(f"silver: {total_size}\ngold: {gold}")
