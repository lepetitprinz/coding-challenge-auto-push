from collections import deque


def solution(graph):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    max_route = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "L":
                visited = [[False] * w for _ in range(h)]
                route = bfs(graph, (i, j), visited, moves)
                max_route = max(max_route, route)

    return max_route


def bfs(graph, start, visited, moves):
    r, c = start
    queue = deque([(r, c, 0)])
    visited[r][c] = True

    max_route = 0
    while queue:
        r, c, route = queue.popleft()
        if route > max_route:
            max_route = route

        for move in moves:
            nr = r + move[0]
            nc = c + move[1]

            if (0 <= nr < h) and (0 <= nc < w):
                if not visited[nr][nc] and graph[nr][nc] == "L":
                    queue.append((nr, nc, route + 1))
                    visited[nr][nc] = True

    return max_route


h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]

ans = solution(graph)
print(ans)