import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = set(sorted([int(input()) for _ in range(n)]))
result = 4
for value in data:
    temp = set(range(value, value + 5))
    length = len(temp - data)
    if length < result:
        result = length

print(result)