import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
heap = []

for val in map(int, input().split()):
    heappush(heap, val)
        
for _ in range(n - 1):
    for val in map(int, input().split()):
        min_val = heappop(heap)
        if val > min_val:
            heappush(heap, val)
        else:
            heappush(heap, min_val)

print(heappop(heap))