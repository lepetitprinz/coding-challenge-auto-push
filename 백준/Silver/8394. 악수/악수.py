def dp(n):
    d = [0, 2, 3] + [0] * (n - 3)
    for i in range(3, n):
        temp = d[i-1] + d[i-2]
        d[i] = temp % 10
        
    return d[n-1] % 10

n = int(input())
print(dp(n))