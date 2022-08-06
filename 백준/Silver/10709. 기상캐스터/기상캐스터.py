def forecast(data, w):
    cloud_idx = -1
    result = []
    for i, info in enumerate(data):
        if info == 'c':
            idx = 0
            cloud_idx = i
        else:
            if cloud_idx == -1:
                idx = -1
            else:
                idx = i - cloud_idx
        result.append(idx)

    return result
                
h, w = map(int, input().split())
result = []
for _ in range(h):
    data = input()
    print(*forecast(data, w))