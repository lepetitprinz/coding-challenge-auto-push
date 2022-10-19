import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

inf = int(1e10)
graph = [[inf] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    u, v, c = map(int, input().split())
    if graph[u - 1][v - 1] > c:
        graph[u - 1][v - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == inf:
            graph[i][j] = 0

for row in graph:
    print(*row)