def compare(second, value):
    div = second // value
    cnt = div
    second -= div * value
    
    return second, cnt

second = int(input())
result = ['0'] * 3
if second % 10 != 0:
    print(-1)
else:
    if second >= 300:
        second, cnt = compare(second, 300)
        result[0] = str(cnt)
    if second >= 60:
        second, cnt = compare(second, 60)
        result[1] = str(cnt)
    if second >= 10:
        second, cnt = compare(second, 10)
        result[2] = str(cnt)
    print(' '.join(result))