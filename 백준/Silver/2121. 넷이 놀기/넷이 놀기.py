import sys

n = int(input())
a, b = map(int, input().split())
data = {}
for _ in range(n):
    data[tuple(map(int, sys.stdin.readline().split()))] = 1

cnt = 0
for x, y in data:
    if data.get((x + a, y), 0) & data.get((x, y + b), 0) & data.get((x + a, y + b), 0):
        cnt += 1

print(cnt)