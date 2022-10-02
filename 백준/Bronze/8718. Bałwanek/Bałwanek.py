x, k = map(int, input().split())

result = 0
if k * 7 <= x:
    result = 7 * k * 1000
elif k * 7 <= x * 2:
    result = 7* k * 500
elif k * 7 <= x * 4:
    result = 7 * k * 250
else:
    result = 0
print(result)