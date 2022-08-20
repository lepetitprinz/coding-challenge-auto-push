def dp(n, k):
    d = [[1] for _ in range(n+1)]
    d[1].append(1)
    for i in range(2, n):
        before = d[i-1]
        for j in range(i-1):
            d[i].append(before[j] + before[j+1])
        d[i].append(1)
        
    return d[n-1][k-1]
    
n, k = map(int, input().split())
result = dp(n, k)
print(result)