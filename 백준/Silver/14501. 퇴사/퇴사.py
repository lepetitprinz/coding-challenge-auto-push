def dp(n, time, profit, d):
    for i in range(n - 1, -1, -1):
        if time[i] + i > n:
            d[i] = d[i+1]
        else:
            d[i] = max(d[i+1], profit[i] + d[i + time[i]])

    return d[0]

n = int(input())
time = []
profit = []
d = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)
    d.append(p)
d.append(0)

result = dp(n, time, profit, d)
print(result)