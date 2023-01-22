import sys
from heapq import heappush, heappop, heapify

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapify(heap)
for _ in range(m):
    a = heappop(heap)
    b = heappop(heap)
    add = a + b
    heappush(heap, add)
    heappush(heap, add)
    
result = sum(heap)
print(result)