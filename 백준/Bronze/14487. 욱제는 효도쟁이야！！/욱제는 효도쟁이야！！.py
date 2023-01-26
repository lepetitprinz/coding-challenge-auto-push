n = int(input())
data = sorted(list(map(int, input().split())))
result = sum(data[:-1])
print(result)