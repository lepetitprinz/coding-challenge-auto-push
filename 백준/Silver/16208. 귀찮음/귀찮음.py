n = int(input())
data = sorted(list(map(int, input().split())))
total = sum(data)

result = 0
for num in data:
    total -= num
    result += num * total

print(result)