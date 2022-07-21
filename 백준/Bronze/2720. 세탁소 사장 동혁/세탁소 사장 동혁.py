def compare(change, value):
    div = change // value
    cnt = div
    change -= div * value
    
    return change, cnt

test = int(input())
for _ in range(test):
    change = int(input())
    result = ['0'] * 4
    if change >= 25:
        change, cnt = compare(change, 25)
        result[0] = str(cnt)
    if change >= 10:
        change, cnt = compare(change, 10)
        result[1] = str(cnt)
    if change >= 5:
        change, cnt = compare(change, 5)
        result[2] = str(cnt)
    if change >= 1:
        change, cnt = compare(change, 1)
        result[3] = str(cnt)
    print(' '.join(result))