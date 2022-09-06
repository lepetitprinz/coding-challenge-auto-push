from math import floor

def seq(x, p, q, dp):
    val = dp.get(x, 0)
    if val != 0:
        return val
    dp[x] = seq(floor(x / p), p, q, dp) + seq(floor(x / q), p, q, dp)
    
    return dp[x]

n, p, q = map(int, input().split())
dp = {0: 1}
print(seq(x=n, p=p, q=q, dp=dp))