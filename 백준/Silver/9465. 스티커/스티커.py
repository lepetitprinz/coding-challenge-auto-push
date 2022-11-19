import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(n, s):
    d = [[0, 0] for _ in range(n)]
    d[0][0] = s[0][0]
    d[0][1] = s[1][0]
    
    if n > 1:
        d[1][0] = s[1][0] + s[0][1]
        d[1][1] = s[0][0] + s[1][1]
    
    if n > 2:
        for i in range(2, n):
            d[i][0] = max(d[i - 2][0], d[i - 2][1], d[i - 1][1]) + s[0][i]
            d[i][1] = max(d[i - 2][0], d[i - 2][1], d[i - 1][0]) + s[1][i]
    
    return max(d[n - 1])
    
t = int(input())
for _ in range(t):
    n = int(input())
    stickers = []
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))
    
    result = dp(n, stickers)
    print(result)