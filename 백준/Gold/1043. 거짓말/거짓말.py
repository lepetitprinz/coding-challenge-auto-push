import sys
from collections import deque
from itertools import combinations

input = lambda : sys.stdin.readline().rstrip()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    result = [start]
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result.append(i)

    return result


n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]

party = []
graph = [set() for _ in range(n + 1)]
truth_all = set()
for _ in range(m):
    data = list(map(int, input().split()))[1:]
    party.append(set(data))
    if len(data) > 1:
        for u, v in combinations(data, 2):
            graph[u].add(v)
            graph[v].add(u)

for t in truth:
    visited = [False] * (n + 1)
    result = bfs(graph, t, visited)
    truth_all.update(result)

count = 0
for p in party:
    if not p.issubset(truth_all):
        count += 1

print(count)