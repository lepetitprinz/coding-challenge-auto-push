n = int(input())
data = list(map(int, input().split()))
target = sum(data) // n

cnt = 0
for i in range(n - 1):
    if data[i] != target:
        diff = abs(target - data[i])
        cnt += diff
        if data[i] < target:
            data[i + 1] -= diff
        else:
            data[i + 1] += diff
        data[i] = target

print(cnt)