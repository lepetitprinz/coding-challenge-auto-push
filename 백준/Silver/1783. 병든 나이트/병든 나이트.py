r, c = map(int, input().split())

result = 0
if r == 1:
    result = 1
elif r == 2:
    result = min((c+1) // 2, 4)
elif c < 7:
    result = min(c, 4)
else:
    result = c - 2

print(result)