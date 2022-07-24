n = int(input())

cnt = -1
for i in range(n//5, -1, -1):
    value = 5 * i
    if n - value == 0:
        cnt = i 
        break
    elif (n - value) % 2 == 0:
        cnt = i + (n - value) // 2 
        break
print(cnt)