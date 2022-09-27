import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs(start, target, visited):
    queue = deque([[start, '']])
    visited[start] = True
    
    while queue:
        val, result = queue.popleft()
        if val == target:
            break
        for method in ['D', 'S', 'L', 'R']:
            new_val = conv_val(val, method)
            if not visited[new_val]:
                visited[new_val] = True
                queue.append([new_val, result + method])

    return result

def conv_val(val, method):
    if method == 'D':
        val *= 2
        if val > 9999:
            val = val % 10000
    elif method == 'S':
        if val == 0:
            val = 9999
        else:
            val -= 1
    else:
        val = str(val).zfill(4)
        if method == 'L':
            val = int(val[1:] + val[0])
        else:
            val = int(val[-1] + val[:-1])
    
    return val

test = int(input())
for _ in range(test):
    start, target = map(int, input().split())
    
    visited = [False] * 10000
    result = bfs(start, target, visited)
    print(''.join(result))