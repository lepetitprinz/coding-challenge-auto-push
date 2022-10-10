a, b, c, m = map(int, input().split())

t = 0
f = 0
work = 0
while t < 24:
    if f + a > m:
        f = max(f - c, 0)
    else:
        f += a
        work += b
    t += 1

print(work)