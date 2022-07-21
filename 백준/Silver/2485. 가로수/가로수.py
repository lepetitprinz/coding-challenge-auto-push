import sys
from math import gcd

n = int(sys.stdin.readline())
diff_list = []
temp = int(sys.stdin.readline())
g = 0
for i in range(n-1):
    val = int(sys.stdin.readline())
    diff = val - temp
    diff_list.append(diff)
    temp = val
    if i == 0:
        g = diff
    else:
        g = gcd(g, diff)
        
result = sum(d//g -1 for d in diff_list)
print(result)