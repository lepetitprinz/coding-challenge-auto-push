from collections import deque

def bfs(bridge, start, end, visited):
    queue = deque([[start, 0]])
    visited[start] = True
    
    while queue:
        loc, cnt = queue.popleft()
        if loc == end:
            return cnt
        
        m = bridge[loc]
        moves = [m * i for i in range(1, 10000 // m)]
        moves += [m * i * -1 for i in range(1, 10000 // m)]
        for move in moves:
            new_loc = loc + move
            if 0 <= new_loc < n and not visited[new_loc]:
                queue.append((new_loc, cnt +1))
                visited[new_loc] = True
    
    return -1
    
n = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())
visited = [False] * n
result = bfs(bridge, start-1, end-1, visited)
print(result)