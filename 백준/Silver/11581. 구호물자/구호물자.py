import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

INF = int(1e8)
graph = [[INF] * n for _ in range(n)]
    
for i in range(n - 1):
    l = int(input())
    conn = list(map(int, input().split()))
    for c in conn:
        graph[i][c - 1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

move_nodes = [i for i in range(n) if graph[0][i] != INF]
            
for i in move_nodes:
    if graph[i][i] != INF:
        print("CYCLE")
        break
else:
    print("NO CYCLE")