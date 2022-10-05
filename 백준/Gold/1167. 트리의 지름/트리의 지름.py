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


n = int(input())
INF = int(1e7)
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    data = list(map(int, input().split()))
    i = 1
    node = data[0]
    while True:
        if data[i] == -1:
            break
        else:
            graph[node].append((data[i], data[i + 1]))
            i += 2

distance = [INF] * (n + 1)
dist1 = dijkstra(graph, 1, distance)
start = dist1.index(max(dist1[1:]))
distance = [INF] * (n + 1)
dist2 = dijkstra(graph, start, distance)
print(max(dist2[1:]))