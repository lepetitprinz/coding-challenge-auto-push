import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return visited

t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    
    graph = [[] for _ in range(n + 1)]
    for u, v in enumerate(data):
        graph[u + 1].append(v)
    
    visited = [False] * (n + 1)
    
    cycle = 0
    for i in range(n):
        if not visited[i + 1]:
            cycle += 1
            visited = bfs(graph, i + 1, visited)
    
    print(cycle)