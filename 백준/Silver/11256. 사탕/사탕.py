import sys

t = int(sys.stdin.readline())

for _ in range(t):
    j, n = map(int, sys.stdin.readline().split())
    box = []
    for _ in range(n):
        r, c = map(int, sys.stdin.readline().split())
        box.append(r*c)
    box = sorted(box)
    cnt = 0
    while j > 0:
        j -= box.pop()
        cnt += 1
    print(cnt)