import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

heap = []
n = int(input())
for _ in range(n):
    heappush(heap, int(input()))

total = 0
for _ in range(n - 1):
    a = heappop(heap)
    b = heappop(heap)
    add = a + b
    total += add
    heappush(heap, add)
    
print(total)