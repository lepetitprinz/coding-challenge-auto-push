n = int(input())
data = sorted(list(map(int, input().split())))

length = n * 2
result = min(data[i] + data[length - i - 1] for i in range(n))
print(result)