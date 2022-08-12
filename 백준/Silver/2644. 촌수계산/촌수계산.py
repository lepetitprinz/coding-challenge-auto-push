n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[-1] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    t, f = map(int, input().split())
    graph[f - 1][t - 1] = 1
    graph[t - 1][f - 1] = 1

for k in range(n):
    for i in range(n):
        if graph[i][k] >= 0:
            for j in range(i + 1, n):
                if graph[k][j] >= 0:
                    if graph[i][j] > 0:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    else:
                        graph[i][j] = graph[i][k] + graph[k][j]
                    graph[j][i] = graph[i][j]

print(graph[x - 1][y - 1])