import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def make_candidates(empty):
    candidates = combinations(empty, 3)

    return candidates


def update_graph(graph, coordinate):
    graph = deepcopy(graph)
    for r, c in coordinate:
        graph[r][c] = 1

    return graph


def bfs(graph, start, visited):
    virus_cnt = 0
    queue = deque([])
    for r, c in start:
        queue.append([r, c])
        visited[r][c] = True
        virus_cnt += 1

    while queue:
        r, c = queue.popleft()
        for move in moves:
            nr = r + move[0]
            nc = c + move[1]

            if (0 <= nr < n) and (0 <= nc < m):
                if not visited[nr][nc] and graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append([nr, nc])
                    virus_cnt += 1

    result = n * m - wall_cnt - virus_cnt
    return result


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

empty = []
start = []
for i, row in enumerate(graph):
    for j, val in enumerate(row):
        if val == 0:
            empty.append([i, j])
        elif val == 2:
            start.append([i, j])

wall_cnt = n * m - len(empty) - len(start) + 3

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
candidates = make_candidates(empty)
results = []
for candidate in candidates:
    temp = update_graph(graph, candidate)
    visited = [[False] * m for _ in range(n)]
    result = bfs(temp, start, visited)
    results.append(result)

print(max(results))