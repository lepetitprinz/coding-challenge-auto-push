def dp(n):
    d = [[1] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
            
    return d[n - 1][n - 1] % 1_000_000_007

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
result1 = dp(n + 1)
result2 = ((n - 1) ** 2 + 2 * n - 1) % 1_000_000_007
print(f"{result1} {result2}")