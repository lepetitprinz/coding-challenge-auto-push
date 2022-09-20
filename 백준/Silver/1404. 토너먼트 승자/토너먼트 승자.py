data = list(map(int, input().split()))
prob = [[0] * 8 for _ in range(8)]
idx = 0
for i in range(7):
    for j in range(i + 1, 8):
        val = data[idx]
        prob[i][j] = val
        prob[j][i] = (100 - val)
        idx += 1

results = [1] * 8
group = list(range(8))
for i in range(3):
    result = results[:]
    for j, g in enumerate(group):
        q = g // 2
        r = (g + 1) % 2
        group[j] = q
        start = (2 ** (i + 1)) * q + (2 ** i) * r
        p = 0
        for k in range(2 ** i):
            p += results[start + k] * prob[j][start + k]
        result[j] = p * results[j] / 100
    results = result
print(*results)
