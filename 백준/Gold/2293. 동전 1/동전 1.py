import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(n, k, coins):
    d = [0 for _ in range(k + 1)]
    d[0] = 1
    
    for coin in coins:
        for i in range(coin, k + 1):
            if i - coin >= 0:
                d[i] += d[i - coin]
    
    return d[k]
                
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
result = dp(n, k, coins)
print(result)