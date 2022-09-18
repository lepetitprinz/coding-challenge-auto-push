import sys
from collections import deque

def bfs(graph, start, visited, moves):
    queue = deque(start)
    
    cnt = 0
    cnt_set = set()
    while queue:
        r, c, cnt = queue.popleft()
        cnt_set.add(cnt)
        
        for move in moves:
            nr = r + move[0]
            nc = c + move[1]
            if (0 <= nr < n) and (0 <= nc < m):
                if not visited[nr][nc] and not graph[nr][nc]:
                    visited[nr][nc] = True
                    queue.append([nr, nc, cnt + 1])
    
    return max(cnt_set)
    
n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

result = 0
start = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            start.append([i, j, 0])
result = bfs(graph, start, visited, moves)
print(result)