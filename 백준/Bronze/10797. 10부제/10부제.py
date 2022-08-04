n = int(input())
data = list(map(int, input().split()))

print(sum(1 for i in data if i == n))