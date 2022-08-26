import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    o1 = list(sys.stdin.readline().rstrip().split())
    o2 = list(sys.stdin.readline().rstrip().split())
    
    o1_map = {w: i for i, w in enumerate(o1)}
    encrypt = {i: o1_map[w] for i, w in enumerate(o2)}
    p = list(sys.stdin.readline().rstrip().split())
    
    result = [None] * len(p)
    for i, w in enumerate(p):
        result[encrypt[i]] = w
    
    print(*result)