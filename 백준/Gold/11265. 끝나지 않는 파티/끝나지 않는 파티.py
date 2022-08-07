import sys

n, m = map(int, input().split())

inf = int(1e11)
graph = [[inf] * (n) for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j, val in enumerate(row):
        graph[i][j] = val

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
for _ in range(m):
    i, j, hour = map(int, sys.stdin.readline().split())
    if graph[i-1][j-1] > hour:
        print("Stay here")
    else:
        print("Enjoy other party")