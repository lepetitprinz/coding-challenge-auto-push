import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result[i-1] = value

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
result = [0] * n
bfs(graph, 1, visited)
print(*result[1:], sep='\n')