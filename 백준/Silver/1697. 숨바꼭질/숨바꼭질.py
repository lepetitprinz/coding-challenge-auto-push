from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque([(n, 0)])

while queue:
    v, cnt = queue.popleft()
    visited[v] = True
    if v == k:
        break
    else:
        for i in [v - 1, v + 1, 2 * v]:
            if i >= 0 and i <= 100000 and not visited[i]:
                queue.append((i, cnt+1))

print(cnt)