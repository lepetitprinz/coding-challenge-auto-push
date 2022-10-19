def calc_coordinate(c, p):
    quotient = p // c
    remainder = p % c
    
    if remainder == 0:
        i = quotient
        j = c
    else:
        i = quotient + 1
        j = remainder

    return i, j
    
def dp(r, c):
    d = [[1] * c for _ in range(r)]
    for i in range(1, r):
        for j in range(1, c):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
    
    return d[r - 1][c - 1]
    
r, c, p = map(int, input().split())

result = 0
if p != 0:
    i, j = calc_coordinate(c, p)
    r1 = dp(i, j)
    r2 = dp(r - i + 1, c - j + 1)
    result = r1 * r2
    
else:
    result = dp(r, c)
    
print(result)