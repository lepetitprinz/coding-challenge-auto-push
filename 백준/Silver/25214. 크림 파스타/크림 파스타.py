n = int(input())
data = list(map(int, input().split()))
result = []
min_val = data[0]
diff = 0
for num in data:
    if num < min_val:
        min_val = num
    if num - min_val > diff:
        diff = num - min_val
    result.append(diff)

print(*result)