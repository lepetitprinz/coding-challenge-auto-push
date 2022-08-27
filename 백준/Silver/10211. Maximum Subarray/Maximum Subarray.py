import sys

def dp(data, n):
    d = [data[0]] + [0] * (n-1)
    for i in range(1, n):
        d[i] = max(data[i], data[i] + d[i-1])
        
    return max(d)

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline().rstrip())
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    result = dp(data, n)
    print(result)