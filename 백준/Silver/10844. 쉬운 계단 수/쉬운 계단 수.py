def dp(n):
    d = [{}] * n
    d[0] = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    for i in range(1, n):
        temp = {i: 0 for i in range(10)}
        for k, v in d[i - 1].items():
            if k == 0:
                temp[1] += v
            elif k == 9:
                temp[8] += v
            else:
                temp[k - 1] += v
                temp[k + 1] += v
        d[i] = temp

    result = sum(v for v in d[n - 1].values())

    return result % int(1e9)

n = int(input())
result = dp(n)
print(result)