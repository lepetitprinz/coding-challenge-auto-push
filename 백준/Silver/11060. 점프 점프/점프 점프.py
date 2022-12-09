from collections import deque

def bfs(n, data, visited):
    queue = deque([[0, 0]])
    visited[0] = True
    
    while queue:
        loc, cnt = queue.popleft()
        if loc == n - 1:
            break
        for move in range(1, data[loc] + 1):
            new_loc = loc + move
            if new_loc < n and not visited[new_loc]:
                queue.append([new_loc, cnt + 1])
                visited[new_loc] = True
                
    else:
        cnt = -1
    
    return cnt
    

n = int(input())
data = list(map(int, input().split()))
visited = [False] * n

result = bfs(n, data, visited)
print(result)