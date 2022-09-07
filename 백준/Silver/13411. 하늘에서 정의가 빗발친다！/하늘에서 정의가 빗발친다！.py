import sys
from math import sqrt

def calc_duration(x, y, v):
    return sqrt(x**2 + y**2) / v
    
n = int(input())

result = []
for i in range(1, n+1):
    x, y, v = map(int, sys.stdin.readline().rstrip().split())
    duration = calc_duration(x, y, v)
    result.append([i, duration])
    
result = sorted(result, key=lambda x: (x[1], x[0]))
result = [num for num, sec in result]
print(*result, sep='\n')