import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

n, e = map(int, input().split())
INF = int(1e7)
lines = {i + 1: {} for i in range(n)}
for _ in range(e):
    a, b, c = map(int, input().split())
    lines[a][b] = c
    lines[b][a] = c

routes = [[1], [1]]
points = list(map(int, input().split()))
for i in range(2):
    routes[i].append(points[i % 2])
    routes[i].append(points[(i + 1) % 2])
    routes[i].append(n)

visited = [0 for _ in range(n + 1)]
min_dist = INF
for j in range(2):
    dist = [INF, INF, INF]
    for i in range(3):
        start, end = routes[j][i], routes[j][i + 1]
        visit = visited[:]
        q = []
        heapq.heappush(q, (0, start))
        while q:
            cost, loc = heapq.heappop(q)
            if loc == end:
                dist[i] = cost
                break

            if visit[loc] == 0:
                visit[loc] = 1
                for to, c in lines[loc].items():
                    if visit[to] == 0:
                        heapq.heappush(q, (cost + c, to))
    min_dist = min(min_dist, sum(dist))

if min_dist >= INF:
    print(-1)
else:
    print(min_dist)