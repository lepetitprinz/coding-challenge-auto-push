import sys

input = lambda: sys.stdin.readline().rstrip()

n, t = map(int, input().split())

interval = []
for _ in range(n):
    s, add, c = map(int, input().split())
    
    for i in range(c):
        time = s + (add * i)
        if time >= t:
            interval.append(time)
            break

if len(interval) > 0:
    min_interval = min(interval)
    print(min_interval - t)
else:
    print(-1)