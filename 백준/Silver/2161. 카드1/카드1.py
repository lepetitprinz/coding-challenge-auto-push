from collections import deque

n = int(input())
queue = deque(range(1, n+1))
result = []
while queue:
    result.append(str(queue.popleft()))
    if len(queue) == 0:
        break
    q = queue.popleft()
    queue.append(q)

print(' '.join(result))