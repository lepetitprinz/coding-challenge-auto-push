def dp(n):
    d = [0] * n
    if n > 1:
        for i in range(1, n):
            d[i] = d[i-1] + i

    return d[n -1]

n = int(input())

result = dp(n)
print(result)