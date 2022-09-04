import sys
from collections import deque

def bfs(col, row, visited):
    queue = deque([(col, row, 1)])
    visited[col][row] = 0

    while queue:
        c, r, cnt = queue.popleft()
        for horizon, vertical in move:
            col = c + horizon
            row = r + vertical
            if row == m - 1 and col == n - 1:
                return cnt + 1
            if row >= 0 and row < m and col >= 0 and col < n:
                if visited[col][row]:
                    queue.append((col, row, cnt+1))
                    visited[col][row] = 0

n, m = map(int, input().split())
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
result = bfs(col=0, row=0, visited=visited)
print(result)