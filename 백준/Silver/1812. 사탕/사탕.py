import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = [int(input()) for _ in range(n)]

total = sum(data) // 2

results = []
for i in range(n):
    temp = 0
    for j in range(i - 2, -1, -2):
        temp += data[j]
    
    for k in range(i + 1, n, 2):
        temp += data[k]
    
    results.append(total - temp)

print(*results, sep='\n')