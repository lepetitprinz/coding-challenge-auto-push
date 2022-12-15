def append_mosaic(cnt, mosaic):
    for from_x, from_y, to_x, to_y in mosaic:
        for i in range(from_x, to_x + 1):
            for j in range(from_y, to_y + 1):
                cnt[(i, j)] += 1
                
    return cnt

n, m = map(int, input().split())

mosaic = []
for _ in range(n):
    from_x, from_y, to_x, to_y = map(int, input().split())
    mosaic.append([from_x, from_y, to_x, to_y])

cnt = {}
for i in range(1, 101):
    for j in range(1, 101):
        cnt[(i, j)] = 0

cnt = append_mosaic(cnt, mosaic)
result = sum(1 for value in cnt.values() if value > m)
print(result)
