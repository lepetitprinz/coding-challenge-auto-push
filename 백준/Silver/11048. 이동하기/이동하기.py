import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(n, m , arr):
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + arr[i - 1][j - 1]

    return d[n][m]
    
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = dp(n, m, arr)
print(result)