import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, start, distance, max_dist, item):
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
    
    cnt = 0
    for i, d in enumerate(distance):
        if d <= max_dist:
            cnt += item[i]
            
    return cnt

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(r):
    u, v, d = map(int, input().split())
    graph[u - 1].append([v - 1, d])
    graph[v - 1].append([u - 1, d])

INF = int(1e6)
result = 0
for s in range(n):
    distance = [INF] * (n + 1)
    cnt = dijkstra(graph, s, distance, m, item)
    if cnt > result:
        result = cnt

print(result)