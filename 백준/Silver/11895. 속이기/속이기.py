n = int(input())
data = sorted(list(map(int, input().split())))

temp = data[0]
for num in data[1:]:
    temp = bin(temp ^ num)
    temp = int(temp, 2)

if temp == 0:
    print(sum(data[1:]))
else:
    print(0)