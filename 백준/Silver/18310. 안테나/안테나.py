from math import floor

def median(data, n):
    middle = n // 2
    if n % 2 == 1:
        median = data[middle]
    else:
        median = (data[middle] + data[middle -1]) / 2
    
    return median

n = int(input())
data = sorted(list(map(int, input().split())))
avg = median(data, n)

if n <= 2:
    print(data[0])
else:
    diff = 200000 
    idx = n // 2
    i = 0
    result = -1
    while abs(data[idx - i] - avg) <= diff:
        diff = abs(data[idx - i] - avg)
        result = data[idx - i]
        i += 1

    i = 0    
    while abs(data[idx + 1] - avg) < diff:
        diff = abs(data[idx + i] - avg)
        result = data[idx + i]
        i += 1

    print(result)