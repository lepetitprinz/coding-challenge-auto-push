n = int(input())
data = list(input())
result = []
for _ in range(n):
    result.extend(data)

print(''.join(result))