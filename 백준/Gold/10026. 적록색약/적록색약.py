import sys
from collections import deque

def bfs(graph, start, color, visited):
    col, row = start
    queue = deque([[col, row]])
    
    while queue:
        col, row = queue.popleft()
        
        for move in moves:
            nc = col + move[0]
            nr = row + move[1]
            if (0 <= nc < n) and (0 <= nr < n):
                if not visited[nc][nr] and graph[nc][nr] == color:
                    visited[nc][nr] = True
                    queue.append([nc, nr])

n = int(input())
rgb_map = {'R': 'G'}
graph1 = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
for _ in range(n):
    row = sys.stdin.readline().rstrip()
    for i, rgb in enumerate(row):
        graph1[i].append(rgb)
        graph2[i].append(rgb_map.get(rgb, rgb))
        
count1 = 0
count2 = 0
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
moves = [(0, 1) ,(1, 0) ,(0, -1) ,(-1, 0)]
for c in range(n):
    for r in range(n):
        if not visited1[c][r]:
            bfs(graph1, [c, r], graph1[c][r], visited1)
            count1 += 1
        if not visited2[c][r]:
            count2 += 1
            bfs(graph2, [c, r], graph2[c][r], visited2)
            
print(f'{count1} {count2}')