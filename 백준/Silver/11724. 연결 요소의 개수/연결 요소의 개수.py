import sys
from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
n, m = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(graph, i, visited)
            count += 1
        
print(count)