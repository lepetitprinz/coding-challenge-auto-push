from collections import deque

def bfs(start, end):
    queue = deque([[start, 1]])
    visited = set([start])
    
    while queue:
        val, cnt = queue.popleft()
        if val == end:
            break
        
        next_vals = [val * 2, val * 10 + 1]
        for next_val in next_vals:
            if next_val <= end and next_val not in visited:
                queue.append([next_val, cnt + 1])
                visited.add(next_val)
    else:
        cnt = -1
        
    return cnt

start, end = map(int, input().split())
result = bfs(start, end)
print(result)