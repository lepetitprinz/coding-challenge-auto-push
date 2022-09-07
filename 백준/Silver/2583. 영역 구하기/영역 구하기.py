import sys
from collections import deque

def draw_rectangle(graph, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = True

    return graph


def bfs(start, visited, moves):
    queue = deque([start])
    c, r = start
    visited[c][r] = True

    area = 1
    while queue:
        c, r = queue.popleft()
        for move in moves:
            move_c = c + move[0]
            move_r = r + move[1]
            if (0 <= move_c < m) and (0 <= move_r < n):
                if not visited[move_c][move_r]:
                    area += 1
                    visited[move_c][move_r] = True
                    queue.append([move_c, move_r])


    return area


m, n, k = map(int, input().split())
visited = [[False] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    visited = draw_rectangle(visited, (x1, y1), (x2, y2))

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
count = 0
areas = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            areas.append(bfs(start=[i, j], visited=visited, moves=moves))

print(count)
print(*sorted(areas))