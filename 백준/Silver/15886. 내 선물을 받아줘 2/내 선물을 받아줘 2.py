n = int(input())
seq = input()

cnt = 0
for i in range(n - 1):
    if seq[i] == 'E' and seq[i + 1] == 'W':
        cnt += 1
        
print(cnt)