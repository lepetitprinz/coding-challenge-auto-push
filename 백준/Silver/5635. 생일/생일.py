import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = []
for _ in range(n):
    name, d, m, y = input().split()
    data.append([name, int(y), int(m), int(d)])
    
data = sorted(data, key=lambda x: (x[1], x[2], x[3]))
print(data[-1][0])
print(data[0][0])