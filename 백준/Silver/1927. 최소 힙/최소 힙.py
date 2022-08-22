import sys
from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
    val = int(sys.stdin.readline())
    if val == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, val)