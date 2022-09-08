import sys
from collections import deque


def bfs(graph, start, visited, height):
    queue = deque([start])
    col, row = start
    visited[col][row] = True

    while queue:
        col, row = queue.popleft()

        for direction in directions:
            d_col = col + direction[0]
            d_row = row + direction[1]
            if (0 <= d_col < n) and (0 <= d_row < n):
                if graph[d_col][d_row] > height:
                    if not visited[d_col][d_row]:
                        queue.append([d_col, d_row])
                        visited[d_col][d_row] = True


n = int(input())
graph = []
heights = set()
for _ in range(n):
    height = list(map(int, sys.stdin.readline().split()))
    graph.append(height)
    heights.update(height)

counts = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for height in heights:
    count = 0
    visited = [[False] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            if graph[c][r] > height:
                if not visited[c][r]:
                    count += 1
                    bfs(graph, [c, r], visited, height)
    counts.append(count)

print(max(max(counts), 1))