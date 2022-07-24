import sys

n = int(input())
data = sorted([int(sys.stdin.readline()) for _ in range(n)])
result = []
for i in range(1, n+1):
    result.append(data.pop() * i)

print(max(result))