def dp(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[1] = [1] * (n + 1)

    for i in range(2, k + 1):
        for j in range(n + 1):
            dp[i][j] = sum(dp[i-1][l] for l in range(0, j + 1)) % divisor

    return dp[k][n] % divisor


divisor = 10 ** 9
n, k = map(int, input().split())
result = dp(n, k)
print(result)