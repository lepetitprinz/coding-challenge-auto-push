# Solution 2
from itertools import permutations

def backtracking(a, b):
    b = int(b)
    a = sorted(list(a), reverse=True)
    result = 0
    for candidate in permutations(a, len(a)):
        value = int(''.join(candidate))
        if value < b:
            result = value
            break
    
    if len(str(result)) < len(a):
        result = -1
    
    return result
    
a, b = input().split()

if len(a) > len(b):
    print(-1)
elif len(a) < len(b):
    a = sorted(list(a), reverse=True)
    print(''.join(a))
elif min(a) > max(b):
    print(-1)
else:
    result = backtracking(a, b)
    print(result)