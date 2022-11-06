# 14470
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

result = 0
if a < 0 :
    result -= a * c
    result += d
    result += b * e
else:
    result += (b - a) * e

print(result)