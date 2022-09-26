n = int(input())
data = list(map(int, input().split()))
total = sum(data)

result = 0
for number in data:
    result += number * (total - number)
    result = result % 1000000007
    total -= number

print(result % 1000000007)