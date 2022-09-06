import sys
from collections import deque

moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]


def bfs(graph, start, visited):
    queue = deque([start])
    col, row = start
    visited[col][row] = True

    while queue:
        col, row = queue.popleft()

        for c, r in moves:
            move_col = col + c
            move_row = row + r
            if (0 <= move_col < h) and (0 <= move_row < w):
                if graph[move_col][move_row] == 1 and not visited[move_col][move_row]:
                    queue.append([move_col, move_row])
                    visited[move_col][move_row] = True


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]

        count = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1 and not visited[i][j]:
                    bfs(graph, [i, j], visited)
                    count += 1

        print(count)