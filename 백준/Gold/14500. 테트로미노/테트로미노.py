import sys

def dfs(r, c, cnt, total, result):
    if result >= total + max_val * (3 - cnt):
        return result

    if cnt == 3:
        result = max(result, total)
        return result
    else:
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    if cnt == 1:
                        visited[nr][nc] = 1
                        result = dfs(r, c, cnt + 1, total + graph[nr][nc], result)
                        visited[nr][nc] = 0
                    visited[nr][nc] = 1
                    result = dfs(nr, nc, cnt + 1, total + graph[nr][nc], result)
                    visited[nr][nc] = 0

    return result

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = 0
max_val = max(map(max, graph))
for c in range(n):
    for r in range(m):
        visited[c][r] = 1
        result = dfs(c, r, 0, graph[c][r], result)
        visited[c][r] = 0

print(result)