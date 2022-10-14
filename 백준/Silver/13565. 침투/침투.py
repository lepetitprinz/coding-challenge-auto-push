import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(graph, start, visited):
    r, c = start
    queue = deque([start])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        if r == m - 1:
            flag = True
            break

        for move in moves:
            nr = r + move[0]
            nc = c + move[1]
            if (0 <= nr < m) and (0 <= nc < n):
                if not visited[nr][nc] and graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append([nr, nc])
    else:
        flag = False

    return flag


m, n = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(m)]

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i, val in enumerate(graph[0]):
    if val == 0:
        visited = [[False] * n for _ in range(m)]
        if bfs(graph, [0, i], visited):
            print('YES')
            break
else:
    print('NO')