def dp(n, data):
    d = [0 for _ in range(n)]
    d[n - 1] = 1
    
    for i in range(n - 2, -1, -1):
        num = data[i]
        candidates = []
        
        for j in range(i, n):
            temp = data[j]
            if temp < num:
                candidates.append(d[j])
            
        if len(candidates) > 0:
            d[i] = max(candidates) + 1
        else:
            d[i] = 1
        
    return max(d)
        

n = int(input())
data = list(map(int, input().split()))
result = dp(n, data)
print(result)