from collections import deque

n, l = map(int, input().split())
data = sorted(list(map(int, input().split())))
queue = deque(data)

cnt = 1
temp = list(range(data[0], data[0] + l))
while queue:
    q = queue.popleft()
    if q > temp[-1]:
        cnt += 1
        temp = list(range(q, q + l))
        queue.append(q)

print(cnt)