import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    visited[start] = True
    
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    f, t = map(int, sys.stdin.readline().split())
    graph[f].append(t)
    graph[t].append(f)
    
for g in graph:
    g.sort()
    
visited = [False] * (n+1)
dfs(graph, v, visited)
print('')
visited = [False] * (n+1)
bfs(graph, v, visited)