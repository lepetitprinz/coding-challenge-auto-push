def dp(n, m):
    d = [[1] * m for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = d[i-1][j-1] + d[i - 1][j] + d[i][j - 1]
            d[i][j] = d[i][j] % mod
    
    return d[n - 1][m - 1] % mod

mod = int(1e9) + 7 
n, m = map(int, input().split())
result = dp(n, m)
print(result)