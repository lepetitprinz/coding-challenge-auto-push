import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

cnt = 0
records = []
for _ in range(n):
    name, sign = input().split()
    if name in records:
        if sign == '+':
            records.append(name)
            cnt += 1
        else:
            records.remove(name)
            cnt -= 1
    else:
        if sign == '+':
            records.append(name)
            cnt += 1
        else:
            cnt += 1

print(cnt)