t = int(input())
n = int(input())

nodes = ['A', 'B', 'C', 'D']
graph = {node: [] for node in nodes}
prob = {node: 0.25 for node in nodes}
for _ in range(n):
    u, v, p = input().split()
    graph[v].append((u, float(p)))

for _ in range(t):
    prob_update = {node: 0 for node in nodes}
    for node in nodes:
        prob_new = 0
        for i, p in graph[node]:
            prob_new += prob[i] * p
        prob_update[node] = prob_new
    prob = prob_update

for p in prob.values():
    print(100 * p)