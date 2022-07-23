import sys

def decompose(n):
    result = {}
    div = 2
    while True:
        if n == 1:
            break
        if n % div == 0:
            n = n // div
            if div in result:
                result[div] += 1
            else:
                result[div] = 1
        else:
            div += 1
    
    return result

test = int(input())
for _ in range(test):
    result = decompose(int(sys.stdin.readline()))
    for k, v in result.items():
        print(k, v)