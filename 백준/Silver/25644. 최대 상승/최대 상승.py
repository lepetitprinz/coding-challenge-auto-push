def dp(n, stock):
    min_stock = stock[0]
    d = [0 for _ in range(n)]
    
    for i, s in enumerate(stock[1:]):
        if s < min_stock:
            min_stock = s
        d[i + 1] = s - min_stock
    
    return max(d)
        
n = int(input())
stock = list(map(int, input().split()))
result = dp(n, stock)
print(result)