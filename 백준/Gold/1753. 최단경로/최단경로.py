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
    
INF = int(1e9)
n, e = map(int, input().split())
start = int(input())
distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
dijkstra(graph, start, distance)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])