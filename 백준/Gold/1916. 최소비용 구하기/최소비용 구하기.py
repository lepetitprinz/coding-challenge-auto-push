import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, start, end, distance):
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
    
    return distance[end]

n = int(input())
e = int(input())
INF = int(1e9)

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

start, end = map(int, input().split())  
result = dijkstra(graph, start, end, distance)
print(result)