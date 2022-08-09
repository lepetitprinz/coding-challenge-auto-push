import sys

n = int(input())
data = {}
for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        data[name] = 1
    else:
        data[name] = 0
    
result = sorted([name for name, status in data.items() if status == 1], reverse=True)
print(*result, sep='\n')