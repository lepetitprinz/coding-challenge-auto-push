n, k, a, b = map(int, input().split())

leaf = [k] * n
day = 0
while True:
    day += 1
    idx = leaf.index(min(leaf))
    for i in range(idx, idx + a):
        leaf[i] += b

    leaf = [l - 1 for l in leaf]
    if 0 in leaf:
        break

print(day)