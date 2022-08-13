import sys
from collections import deque

n, k = map(int, input().split())
q = []
data = {}
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    q.extend([[i+1, num] for num in temp])
    
queue = deque(q)
move = 0
cnt = 0
while len(queue) > 1:
    number = queue.popleft()
    if cnt == move:
        move = number[1] - 1
        cnt = 0
    else:
        queue.append(number)
        cnt += 1
        
result = queue.popleft()
print(*result)