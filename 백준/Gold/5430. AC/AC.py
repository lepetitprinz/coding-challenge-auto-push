import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solve(data: list) -> str:
    rev_cnt = 0
    queue = deque(data)
    for c in command:
        if c == 'R':
            rev_cnt += 1
        else:
            if not queue:
                return 'error'
            if rev_cnt % 2 == 1:
                queue.pop()
            else:
                queue.popleft()
    if rev_cnt % 2 == 1:
        queue.reverse()
    
    return str(list(queue)).replace(' ', '')

t = int(input())
for _ in range(t):
    command = list(input())
    n = int(input())
    data = eval(input())
    print(solve(data))