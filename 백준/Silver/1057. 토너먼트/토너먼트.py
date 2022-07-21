from math import ceil

n, a, b = map(int, input().split())
r = 1
while True:
    if (abs(a-b) == 1) & (ceil(a/2) == ceil(b/2)):
        break
    else:
        a = ceil(a / 2)
        b = ceil(b / 2)
        r += 1

print(r)