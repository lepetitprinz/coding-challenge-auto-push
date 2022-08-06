from collections import deque

n = int(input())
jump = {i: num for i, num in enumerate(list(map(int, input().split())))}
loc = int(input()) - 1

result = [loc]
queue = deque([loc])
while queue:
    loc = queue.popleft()
    move = jump[loc]
    left = loc - move
    right = loc + move
    
    if (left not in result) & (0 <= left < n):
        result.append(left)
        queue.append(left)
    if (right not in result) & (0 <= right < n):
        result.append(right)
        queue.append(right)
    
print(len(result))