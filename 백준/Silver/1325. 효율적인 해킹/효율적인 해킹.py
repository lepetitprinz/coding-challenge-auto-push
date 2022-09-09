import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    depth = 0
    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                depth += 1
    
    return depth

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)

result = {}
for i in range(1, n+1):
    visited = [False] * (n+1)
    depth = bfs(graph, i, visited)
    if depth in result:
        result[depth].append(i)
    else:
        result[depth] = [i]

print(*sorted(result[max(result)]))