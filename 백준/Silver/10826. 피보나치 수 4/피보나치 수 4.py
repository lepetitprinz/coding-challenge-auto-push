def fibo(n):
    d = [0, 1] + [0] * (n-1)
    if n > 1:
        for i in range(2, n+1):
            d[i] = d[i-1] + d[i-2]
    
    return d[n]

print(fibo(int(input())))