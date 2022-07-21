n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    weights = list(map(int,input().split()))
    temp = 0
    result = 1
    for weight in weights:
        if weight + temp > m:
            temp = weight
            result += 1
        else:
            temp += weight
            
    print(result)