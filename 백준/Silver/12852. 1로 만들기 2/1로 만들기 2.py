def dp(n):
    d = [[0, []] for _ in range(n + 1)]
    d[1][0] = 0
    d[1][1] = [1]
    
    for i in range(2, n + 1):
        d[i][0] = d[i - 1][0] + 1
        d[i][1] = d[i - 1][1] + [i]
        
        if i % 3 == 0:
            bf = d[i // 3][0]
            if bf + 1 < d[i][0]:
                d[i][0] = bf + 1
                d[i][1] = d[i // 3][1] + [i]
                
        if i % 2 == 0:
            bf = d[i // 2][0]
            if bf + 1 < d[i][0]:
                d[i][0] = bf + 1
                d[i][1] = d[i // 2][1] + [i]

    return d[n][0], reversed(d[n][1])
    
n = int(input())
val, route = dp(n)
print(val)
print(*route)