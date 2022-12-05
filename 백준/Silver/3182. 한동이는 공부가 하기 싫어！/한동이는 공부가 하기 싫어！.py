import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(graph, start, visited):
    queue = deque([[start, 1]])
    visited[start] = True
    
    while queue:
        node, cnt = queue.popleft()
        
        for i in graph[node]:
            if not visited[i]:
                queue.append([i, cnt + 1])
                visited[node] = True
    
    return cnt
    
    
    
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n):
    graph[i + 1].append(int(input()))

results = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    cnt = bfs(graph, i, visited)
    results.append([i, cnt])

result = sorted(results, key=lambda x: (-x[1], x[0]))[0]
print(result[0])