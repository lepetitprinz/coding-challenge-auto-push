def dp(n, boxes):
    dp = [0] * n
    dp[0] = 1
    
    for i in range(1, n):
        curr_size = boxes[i]
        prev = []
        for j in range(i):
            if boxes[j] < curr_size:
                prev.append(dp[j])
        
        if len(prev) > 0:
            dp[i] = max(prev) + 1
        else:
            dp[i] = 1
    
    return max(dp)

n = int(input())
boxes = list(map(int, input().split()))
result = dp(n, boxes)
print(result)