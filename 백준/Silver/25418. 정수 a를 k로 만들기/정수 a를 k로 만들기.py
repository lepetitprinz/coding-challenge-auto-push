from collections import deque

def bfs(start, end, visited):
    queue = deque([[start, 0]])
    visited[start] = True
    
    while queue:
        val, cnt = queue.popleft()
        if val == end:
            break
        
        vals = [val + 1, val * 2]
        for v in vals:
            if v <= end and not visited[v]:
                queue.append([v, cnt + 1])
                visited[v] =True
                
    return cnt

start, end = map(int, input().split())
visited = [False] * (end + 1)
result = bfs(start, end, visited)
print(result)