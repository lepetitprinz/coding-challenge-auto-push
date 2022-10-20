def dp(a, b):
    r, c = len(a), len(b)
    d = [[0] * (c + 1) for _ in range(r + 1)]
    
    for i in range(r):
        for j in range(c):
            if a[i] == b[j]:
                d[i + 1][j + 1] = d[i][j] + 1
            else:
                d[i + 1][j + 1] = max(d[i][j + 1], d[i + 1][j])
                
    result = max(max(row) for row in d)
    
    return result
    
a = input()
b = input()
result = dp(a, b)
print(result)