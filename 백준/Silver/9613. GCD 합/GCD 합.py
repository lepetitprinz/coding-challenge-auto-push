import sys
from math import gcd
from itertools import combinations

test = int(input())
for _ in range(test):
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    nums = data[1:]
    
    result = []
    for a, b in list(combinations(nums, 2)):
        result.append(gcd(a, b))
        
    print(sum(result))