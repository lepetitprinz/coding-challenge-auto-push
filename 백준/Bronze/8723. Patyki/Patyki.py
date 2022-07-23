length = list(map(int, input().split()))
length = sorted(length)

if len(set(length)) == 1:
    print(2)
elif length[0] ** 2 + length[1] ** 2 ==length[2] ** 2:
    print(1)
else:
    print(0)