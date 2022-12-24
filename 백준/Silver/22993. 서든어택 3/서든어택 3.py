n = int(input())
data = list(map(int, input().split()))

p = data[0]
others = sorted(data[1:])
for a in others:
    if p > a:
        p += a
    else:
        print("No")
        break
else:
    print("Yes")