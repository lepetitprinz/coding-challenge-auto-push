import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(k, coins):
    d = [10001] * (k + 1)
    d[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            d[i] = min(d[i], d[i - coin] + 1)

    result = -1
    if d[k] != 10001:
        result = d[k]

    return result

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = dp(k, coins)
print(ans)