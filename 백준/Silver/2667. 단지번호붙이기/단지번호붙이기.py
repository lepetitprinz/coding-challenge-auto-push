import sys
from collections import deque


def bfs(graph, start, visited):
    col, row = start
    queue = deque([start])
    visited[col][row] = True

    number = 1
    while queue:
        col, row = queue.popleft()

        for move in moves:
            move_col = col + move[0]
            move_row = row + move[1]
            if (0 <= move_col < n) and (0 <= move_row < n):
                if graph[move_col][move_row] == '1':
                    if not visited[move_col][move_row]:
                        number += 1
                        queue.append([move_col, move_row])
                        visited[move_col][move_row] = True

    return number


n = int(input())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = []
cnt = 0
for col in range(n):
    for row in range(n):
        if graph[col][row] != '0':
            if not visited[col][row]:
                cnt += 1
                result.append(bfs(graph, [col, row], visited))

print(cnt)
print(*sorted(result), sep='\n')