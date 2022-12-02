n = int(input())
data = [int(input()) for _ in range(n)]

value = data.pop()
cnt = 0
for num in data[::-1]:
    if num >= value:
        cnt += num - value + 1
        value = value - 1
    else:
        value = num

print(cnt)