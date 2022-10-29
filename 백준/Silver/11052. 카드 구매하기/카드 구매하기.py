def dp(n, data):
    d = [0] * n
    d[0] = data[0]

    for i in range(1, n):
        temp = []
        temp.append(data[i])
        for j in range(i):
            temp.append(d[j] + data[i - j - 1])
        d[i] = max(temp)

    return d, d[n - 1]


n = int(input())
data = list(map(int, input().split()))
d, result = dp(n, data)

print(result)