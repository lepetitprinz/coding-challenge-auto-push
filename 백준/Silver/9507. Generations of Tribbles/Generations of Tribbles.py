def dp(n):
    d = [1, 1, 2, 4]
    if n <= 3:
        reuslt = d[n]
    else:
        d = d + [0] * (n - 2)
        for i in range(4, n + 1):
            d[i] = d[i - 1] + d[i - 2] + d[i - 3] + d[i - 4]
    
    return d[n]
    
t = int(input())
for _ in range(t):
    n = int(input())
    result = dp(n)
    print(result)