a, b = map(int, input().split())
c = int(input())

total = a + b
if total < 2 * c:
    print(total)
else:
    print(total - 2 * c)