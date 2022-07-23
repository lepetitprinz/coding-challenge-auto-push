n = int(input())
vals = list(map(int, input().split()))
d = [vals[0]] + [0] * (n-1)
for i in range(1, n):
    d[i] = vals[i] + max(d[max(0, i-6): i])
    
print(d[n-1])