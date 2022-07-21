from collections import deque

n = int(input())
move = list(map(int, input().split()))
move_map = {i: m for i, m in zip(range(1, n + 1), move)}

result = []
queue = deque(range(1, n + 1))
number = queue.popleft()
m = move_map[number]
result.append(str(number))

while queue:
    if m > 0:
        for _ in range(m-1):
            number = queue.popleft()
            queue.append(number)
        number = queue.popleft()
    else:
        for _ in range(abs(m+1)):
            number = queue.pop()
            queue.appendleft(number)
        number = queue.pop()

    result.append(str(number))
    m = move_map[number]

print(' '.join(result))