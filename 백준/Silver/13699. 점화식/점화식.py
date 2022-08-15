def dp(n):
    d = [1] + [0] * (n)
    for i in range(1, n+1):
        for j in range(n):
            d[i] += d[j] * d[i - j -1]
    
    return d[n]

n = int(input())
print(dp(n))