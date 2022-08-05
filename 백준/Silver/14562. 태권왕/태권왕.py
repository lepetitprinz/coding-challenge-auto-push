from collections import deque

def bfs(queue, min_cnt):
    while queue:
        s, t, cnt = queue.popleft()
        if s * 2 <= t + 3:
            queue.append([s * 2, t + 3, cnt + 1])
            queue.append([s + 1, t, cnt + 1])
        else:
            min_cnt = min(min_cnt, cnt + (t - s))
    
    return min_cnt

t = int(input())
queue = deque()
for _ in range(t):
    a, b = map(int, input().split())
    queue.append([a, b, 0])
    result = bfs(queue, b - a)
    print(result)