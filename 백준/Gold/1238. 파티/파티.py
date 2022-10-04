import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, start, distance):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, curr = heappop(queue)
        if distance[curr] < dist:
            continue
        for node, d in graph[curr]:
            cost = dist + d
            if cost < distance[node]:
                distance[node] = cost
                heappush(queue, (cost, node))
    
    return distance

INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

distance = [INF] * (n + 1)
b_dist = dijkstra(graph, x, distance)
r1 = {i: b_dist[i] for i in range(1, n + 1) if i != x}
r2 = {}
for i in range(1, n + 1):
    if i != x:
        distance = [INF] * (n + 1)
        a_dist = dijkstra(graph, i, distance)[x]
        r2[i] = a_dist
        
result = []
for i in range(1, n + 1):
    if i != x:
        result.append(r1[i] + r2[i])
print(max(result))