def check(arr):
    cnt = 0
    cnt += vertical(arr)
    cnt += horizon(arr)
    cnt += diagonal(arr)
    
    flag = False
    if cnt >= 3:
        flag = True
    
    return flag

def vertical(arr):
    cnt = 0
    for row in arr:
        flag = True
        for num in row:
            if not num:
                flag = False
                break
        if flag:
            cnt +=1
    
    return cnt

def horizon(arr):
    cnt = 0
    for i in range(5):
        flag = True
        for j in range(5):
            if not arr[j][i]:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt
    
def diagonal(arr):
    cnt = 0
    flag = True
    for i in range(5):
        if not arr[i][i]:
            flag = False
            break
    if flag:
        cnt += 1
    
    flag = True
    for j in range(5):
        if not arr[j][4 - j]:
            flag = False
            break
    if flag:
        cnt += 1
    
    return cnt

arr = [[0]* 5 for _ in range(5)]
loc = {}
for i in range(5):
    row = list(map(int, input().split()))
    for j, num in enumerate(row):
        loc[num] = (i, j)

call = []
for _ in range(5):
    call.extend(list(map(int, input().split())))

for i, num in enumerate(call):
    r, c = loc[num]
    arr[r][c] = 1
    if check(arr):
        print(i+1)
        break