def dp(n, seq):
    d = [0] * n
    d[0] = seq[0]
    
    for i in range(1, n):
        curr_size = seq[i]
        prev = []
        for j in range(i):
            if seq[j] < curr_size:
                prev.append(d[j])
            
        if len(prev) > 0:
            d[i] = max(prev) + curr_size
        else:
            d[i] = curr_size
    
    return max(d)

n = int(input())
seq = list(map(int, input().split()))
result = dp(n, seq)
print(result)