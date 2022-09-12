import sys
from collections import deque


def bfs(forward, backward, start, visited):
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        loc, cnt = queue.popleft()
        if loc == 100:
            break

        for move in [1, 2, 3, 4, 5, 6]:
            new_loc = loc + move
            if new_loc <= 100 and not visited[new_loc]:
                new_loc = backward.get(new_loc, new_loc)
                new_loc = forward.get(new_loc, new_loc)
                visited[new_loc] = True
                queue.append((new_loc, cnt + 1))

    return cnt


n, m = map(int, input().split())

forward = {}
backward = {}
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    forward[start] = end

for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    backward[start] = end

visited = [False] * 101
result = bfs(forward, backward, 1, visited)
print(result)