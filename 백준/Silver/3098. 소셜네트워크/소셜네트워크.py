import sys

def bfs(n, graph, start):
    new_friends = []

    friends = graph[start]
    visited = [False for _ in range(n)]
    visited[start] = True
    for i in friends:
        for j in graph[i]:
            if j not in friends and not visited[j]:
                visited[j] = True
                new_friends.append(j)

    return new_friends

def update_relation(n, graph, new_relation_list):
    for i in range(n):
        graph[i] = graph[i] + new_relation_list[i]

    return graph

def check_relation(n, graph):
    count = sum(len(row) for row in graph)

    return count == n * (n - 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

time = 0
new_relation_cnts = []
while True:
    new_relation_cnt = 0
    new_relation_list = []
    for i in range(n):
        new_friends = bfs(n, graph, i)
        new_relation_list.append(new_friends)
        new_relation_cnt += len(new_friends)

    time += 1
    graph = update_relation(n, graph, new_relation_list)
    new_relation_cnts.append(new_relation_cnt // 2)

    if check_relation(n, graph):
        break

print(time)
print(*new_relation_cnts, sep="\n")