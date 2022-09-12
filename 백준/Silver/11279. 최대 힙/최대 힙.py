import sys
from heapq import heappush, heappop

n = int(input())
heap = []

for _ in range(n):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        if len(heap) > 0:
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -number)