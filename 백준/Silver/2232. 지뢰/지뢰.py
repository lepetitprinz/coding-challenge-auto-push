import sys
import heapq
sys.setrecursionlimit(50000)

def check(data, idx, direction, visit):
    move = idx + direction
    if 0 <= move < length:
        if not visit.get(move, 0):
            if data[move] < data[idx]:
                visit[move] = 1
                visit = check(data, move, direction, visit)

    return visit

n = int(input())
data = []
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    data.append(num)
    heapq.heappush(heap, (-num, i))

visit = {}
result = []
length = len(data)
while True:
    val, idx = heapq.heappop(heap)
    if not visit.get(idx, 0):
        visit[idx] = 1
        result.append(idx+1)
        visit = check(data, idx, 1, visit)
        visit = check(data, idx, -1, visit)

    if len(visit) == length:
        break
        
result = sorted(result)
print(*result, sep='\n')