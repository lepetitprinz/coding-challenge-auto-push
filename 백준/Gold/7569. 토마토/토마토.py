import sys
from collections import deque


def bfs(graph, start_list, directions):
    queue = deque(start_list)

    day = 0
    while queue:
        height, col, row, day = queue.popleft()
        for direction in directions:
            d_height = height + direction[0]
            d_col = col + direction[1]
            d_row = row + direction[2]
            if 0 <= d_col < n and 0 <= d_row < m and 0 <= d_height < h:
                if graph[d_height][d_col][d_row] == 0:
                    graph[d_height][d_col][d_row] = 1
                    queue.append([d_height, d_col, d_row, day + 1])

    return day, graph


def check_zero(graph):
    flag = True
    for arr in graph:
        for row in arr:
            if 0 in row:
                flag = False
                break

    return flag


m, n, h = map(int, input().split())
graph = []
for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    graph.append(arr)

start_list = []
for k in range(h):
    for c in range(n):
        for r in range(m):
            if graph[k][c][r] == 1:
                start_list.append([k, c, r, 0])

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
result, graph = bfs(graph, start_list, directions)
if check_zero(graph):
    print(result)
else:
    print(-1)