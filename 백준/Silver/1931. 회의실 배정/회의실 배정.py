import sys

n = int(input())
data = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    data.append([start, end])
data = sorted(data, key=lambda x: (x[1], x[0]))

cnt = 1
end = data[0][1]
for i in range(1, n):
    if data[i][0] >= end:
        cnt += 1
        end = data[i][1]

print(cnt)