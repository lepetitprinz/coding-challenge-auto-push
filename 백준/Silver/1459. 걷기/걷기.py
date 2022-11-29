x, y, w, s = map(int, input().split())

path_1 = (x + y) * w
path_2 = min(x, y) * s + abs(x - y) * w
if (x + y) % 2 == 0:
    path_3 = max(x, y) * s
else:
    path_3 = (max(x, y) - 1) * s + w
result = min(path_1, path_2, path_3)
print(result)