import sys

n = int(input())
x_map = {}
y_map = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x in x_map:
        x_map[x] += 1
    else:
        x_map[x] = 1
    if y in y_map:
        y_map[y] += 1
    else:
        y_map[y] = 1

result = 0
result += sum(1 for cnt in x_map.values() if cnt > 1)
result += sum(1 for cnt in y_map.values() if cnt > 1)
print(result)