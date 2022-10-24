import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
INF = int(1e8)
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    else:
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != k:
                if graph[i][j] == 1:
                    continue
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

members = []
min_val = 50
for i, row in enumerate(graph):
    score = max(row)
    if score < min_val:
        min_val = score
    members.append((i + 1, score))

cnt = 0
result = []
for member, score in members:
    if score == min_val:
        result.append(member)
        cnt += 1

print(f"{min_val} {cnt}")
print(*result)
