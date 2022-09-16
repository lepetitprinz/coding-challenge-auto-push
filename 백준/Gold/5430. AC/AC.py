import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    command = list(input())
    n = int(input())
    data = eval(input())
    if command.count('D') > n:
        print('error')
    else:
        queue = deque(data)
        rev_cnt = 0
        for c in command:
            if c == 'R':
                rev_cnt += 1
            else:
                if rev_cnt % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
        if rev_cnt % 2 == 1:
            queue.reverse()   
        result = str(list(queue)).replace(' ', '')
        print(result)