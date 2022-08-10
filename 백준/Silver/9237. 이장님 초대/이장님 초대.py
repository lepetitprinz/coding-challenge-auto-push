n = int(input())
data = sorted(list(map(int, input().split())), reverse=True)
result = [val + i + 1 for i, val in enumerate(data)]
print(max(result) + 1)