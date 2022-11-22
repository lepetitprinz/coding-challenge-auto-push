import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def dp(n):
    dp = [0, 0, 1]
    tot = 1
    for i in range(n):
        case = tot % 1000000009
        tot += case - dp[i]
        dp.append(case)
            
    return dp
        
t = int(input())
test = [int(input()) for _ in range(t)]
max_n = max(test)
d = dp(max_n)
result = [d[t + 2] for t in test]

print(*result, sep='\n')