n = int(input())
data = set(map(int, input().split()))
x = int(input())

cnt = 0
for num in data:
    if x - num in data:
        cnt += 1

print(cnt // 2)