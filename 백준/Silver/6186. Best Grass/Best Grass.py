import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(arr, start, visited):
    r, c = start
    queue = deque([(r, c)])
    visited[r][c] = True

    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        r, c = queue.popleft()

        for move in moves:
            nr = r + move[0]
            nc = c + move[1]

            if 0 <= nr < h and 0 <= nc < w:
                if arr[nr][nc] == "#" and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = True

    return visited


h, w = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]

cnt = 0
visited = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if arr[i][j] == '#' and not visited[i][j]:
            cnt += 1
            visited = bfs(arr, (i, j), visited)

print(cnt)