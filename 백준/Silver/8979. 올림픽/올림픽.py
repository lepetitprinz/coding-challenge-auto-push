n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data = sorted(data, key=lambda x: (-x[1], -x[2], -x[3]))

result = 0
rank = 1
p, prev = data[0][0], data[0][1:]
if p == k:
    result = rank
else:
    for i, row in enumerate(data[1:]):
        if row[1:] != prev:
            rank = i + 2
            prev = row[1:]

        if row[0] == k:
            break

print(rank)