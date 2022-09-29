import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(stairs, n):
    d = [0] * n
    d[0] = stairs[0]
    if n > 1:
        d[1] = max(d[0], 0) + stairs[1]
    if n > 2:
        d[2] = max(stairs[0], stairs[1]) + stairs[2]
    if n > 3:
        for i in range(3, n):
            d[i] = max(d[i - 3] + stairs[i-1], d[i - 2]) + stairs[i]
    
    return d[n - 1]
        
n = int(input())
stairs = [int(input()) for _ in range(n)]
result = dp(stairs, n)
print(result)
