import sys

n = int(input())
data = {}
for _ in range(n):
    value = int(sys.stdin.readline())
    if value in data:
        data[value] += 1
    else:
        data[value] = 1

data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
print(data[0][0])