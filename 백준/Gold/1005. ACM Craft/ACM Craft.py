import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def topology_sort(graph, graph_rev, indegree, times, w):
    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    result = [0] * len(graph)
    while queue:
        curr = queue.popleft()

        # Backward network
        if graph_rev[curr]:
            result[curr] = max(result[b] for b in graph_rev[curr]) + times[curr]
        else:
            result[curr] = times[curr]

        # Check endpoint
        if curr == w:
            break

        # Forward network
        for f in graph[curr]:
            indegree[f] -= 1
            if indegree[f] == 0:
                queue.append(f)

    return result[w]

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = {i: time for i, time in enumerate(list(map(int, input().split())))}
    graph = {i: [] for i in range(n)}
    graph_rev = {i: [] for i in range(n)}

    # connection information
    indegree = [0] * n
    for _ in range(k):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph_rev[v - 1].append(u - 1)
        indegree[v - 1] += 1

    w = int(input())
    if indegree[w - 1] == 0:
        result = times[w - 1]
    else:
        result = topology_sort(graph, graph_rev, indegree, times, w-1)

    print(result)