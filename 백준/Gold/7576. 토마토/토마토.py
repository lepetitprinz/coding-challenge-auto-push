import sys
from collections import deque


def bfs(graph, start, directions):
    queue = deque(start)
    day = 0
    while queue:
        col, row, day = queue.popleft()

        for direction in directions:
            d_col = col + direction[0]
            d_row = row + direction[1]
            if 0 <= d_col < n and 0 <= d_row < m:
                if graph[d_col][d_row] == 0:
                    graph[d_col][d_row] = 1
                    queue.append([d_col, d_row, day + 1])

    return day


def check_zero(arr):
    flag = True
    for data in arr:
        if 0 in data:
            flag = False
            break

    return flag


m, n = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

start_points = []
for c in range(n):
    for r in range(m):
        if arr[c][r] == 1:
            start_points.append([c, r, 0])

result = bfs(graph=arr, start=start_points, directions=move)
if check_zero(arr=arr):
    print(result)
else:
    print(-1)
