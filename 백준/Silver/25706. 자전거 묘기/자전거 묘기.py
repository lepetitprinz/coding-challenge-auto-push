def dp(n, j):
    d = [0] * n
    d[n - 1] = 1
    for i in range(n - 2, -1, -1):
        interval = j[i]
        if interval == 0:
            d[i] = d[i + 1] + 1
        elif i + interval + 1 < n:
            d[i] = d[i + interval + 1] + 1
        else:
            d[i] = 1
    
    return d
    
n = int(input())
j = list(map(int, input().split()))
result = dp(n, j)
print(*result)