from math import ceil

def dp(n):
    d = [0] * (n + 1)
    square_list = [i ** 2 for i in range(1, int(ceil(10**5)))]
    for i in range(1, n + 1):
        square = []
        for j in square_list:
            if j > i:
                break
            else:
                square.append(d[i - j])
        d[i] = min(square) + 1
    
    return d[n]
    
n = int(input())
result = dp(n)
print(result)