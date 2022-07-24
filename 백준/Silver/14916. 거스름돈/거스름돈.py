n = int(input())
dp = [0] + [-1] * n
for i in range(n+1):
    if i >= 5:
        if dp[i-5] >= 0 and dp[i-2] >= 0:
            dp[i] = min(dp[i-5] + 1, dp[i-2] + 1)
        elif dp[i-5] >= 0:
            dp[i] = dp[i-5] + 1
        elif dp[i-2] >= 0:
            dp[i] = dp[i-2] + 1

    else:
        if i % 2 == 0:
            dp[i] = i // 2
if dp[n] == 0:
    print(-1)
else:
    print(dp[n])