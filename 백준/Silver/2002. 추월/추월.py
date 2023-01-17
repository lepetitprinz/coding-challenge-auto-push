import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q_in = deque()
q_out = deque()

for _ in range(n):
    q_in.append(input())

for _ in range(n):
    q_out.append(input())

cnt = 0
overtake = set()
while q_in:
    car_in = q_in.popleft()
    if car_in not in overtake:
        while q_out:
            car_out = q_out.popleft()
            if car_in == car_out:
                break
            else:
                cnt += 1
                overtake.add(car_out)
print(cnt)