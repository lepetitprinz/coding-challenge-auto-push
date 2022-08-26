import sys

n = int(sys.stdin.readline().rstrip())
entry = {}

for _ in range(n):
    p = sys.stdin.readline().rstrip()
    if p in entry:
        entry[p] += 1
    else:
        entry[p] = 1
for _ in range(n-1):
    p = sys.stdin.readline().rstrip()
    entry[p] -= 1
    if entry[p] == 0:
        del entry[p]
        
print(list(entry.keys())[0])