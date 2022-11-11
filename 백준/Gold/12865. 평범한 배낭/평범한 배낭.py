import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(n, k, w, v):
    d = [[0] * (k + 1) for _ in range(n + 1)]
    for j in range(k + 1):
        if j >= w[0]:
            d[0][j] = v[0]
    
    for i in range(1, n):
        for j in range(k + 1):
            prev = d[i - 1][j]
            if j >= w[i]:
                d[i][j] = max(prev, d[i - 1][j - w[i]] + v[i])
            else:
                d[i][j] = prev
    
    return d[n - 1][k]

n, k = map(int, input().split())
w, v = [], [] 
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
    
result = dp(n, k, w, v)
print(result)