import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
queue = deque()

while True:
    number = int(input())
    if number == -1:
        break

    if number == 0:
        queue.popleft()
    else:
        if len(queue) < n:
            queue.append(number)
            
print(*queue)