n = int(input())
f = int(input())
base = (n // 100) * 100
for i in range(0, 100):
    if (base + i) % f == 0:
        print(str(i).zfill(2))
        break