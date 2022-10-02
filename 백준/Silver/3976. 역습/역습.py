import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(n, l1, l2, s1, s2, p1, d1, p2, d2):
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = l1
    dp[0][1] = l2

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0] + d1[i - 1], dp[i - 1][1] + p2[i - 1])
        dp[i][1] = min(dp[i - 1][1] + d2[i - 1], dp[i - 1][0] + p1[i - 1])

    r1 = dp[n - 1][0] + s1
    r2 = dp[n - 1][1] + s2

    return min(r1, r2)


t = int(input())
for _ in range(t):
    n, l1, l2, s1, s2 = map(int, input().split())
    p1 = list(map(int, input().split()))
    d1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))

    result = dp(n, l1, l2, s1, s2, p1, d1, p2, d2)
    print(result)