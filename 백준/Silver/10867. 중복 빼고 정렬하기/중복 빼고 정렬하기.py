n = int(input())
data = set(map(int, input().split()))
result = sorted(list(data))
print(*result)