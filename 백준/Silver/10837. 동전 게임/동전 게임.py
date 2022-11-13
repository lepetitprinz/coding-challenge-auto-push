import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(k, m, n):
    result = 0
    if m == n:
        result = 1
    elif m > n:
        if k - (m - 1) >= (m - 1) - n:
            result = 1
    else:
        if (k - n) >= (n - 1) - m:
            result = 1
    return result
    
k = int(input())
c = int(input())
for _ in range(c):
    m, n = map(int, input().split())
    result = solve(k, m, n)
    print(result)