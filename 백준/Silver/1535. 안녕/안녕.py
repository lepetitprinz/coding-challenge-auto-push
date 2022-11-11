def dp(n, h, v):
    d = [[0] * 100 for _ in range(n + 1)]
    for j in range(100):
        if j >= h[0]:
            d[0][j] = v[0]
    
    for i in range(1, n):
        for j in range(100):
            prev = d[i - 1][j]
            if j >= h[i]:
                d[i][j] = max(prev, d[i - 1][j - h[i]] + v[i])
            else:
                d[i][j] = prev
    
    return d[n - 1][99]
    
n = int(input())
h = list(map(int, input().split()))
v = list(map(int, input().split()))
result = dp(n, h, v)
print(result)