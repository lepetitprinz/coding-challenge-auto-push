from collections import deque

n, k = map(int, input().split())
data = list(range(2, n+1))

cnt = 0
flag = False
while data:
    cnt += 1
    p = data[0]
    data.remove(p)
    if cnt == k:
        print(p)
        break
    else:
        for val in data[:]:
            if val % p == 0:
                cnt += 1
                data.remove(val)
                if cnt == k:
                    flag = True
                    print(val)
                    break
    if flag:
        break