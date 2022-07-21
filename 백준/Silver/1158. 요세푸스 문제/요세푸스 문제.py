from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n+1))
result = []
cnt = k
while queue:
    cnt -= 1
    value = queue.popleft()
    if cnt == 0:
        result.append(str(value))
        cnt = k
    else:
        queue.append(value)

print('<' + ', '.join(result) + '>')