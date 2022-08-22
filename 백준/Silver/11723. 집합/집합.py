import sys

m = int(input())

data = set()
all_set = set(map(str, range(1, 21)))
for _ in range(m):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'add':
        data.add(command[1])
    elif command[0] == 'remove':
        val = command[1]
        if val in data:
            data.remove(val)
    elif command[0] == 'check':
        if command[1] in data:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        val = command[1]
        if val in data:
            data.remove(val)
        else:
            data.add(val)
    elif command[0] == 'all':
        data = all_set
    else:
        data = set()