n = int(input())

d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = d[i - 1] + 1
    if i > 1:
        d[i] = min(d[i], d[i - 2] + 1)
    if i > 4:
        d[i] = min(d[i], d[i - 2] + 1, d[i - 5] + 1)
    if i > 6:
        d[i] = min(d[i],  d[i - 2] + 1, d[i - 5] + 1, d[i - 7] + 1)

print(d[n])