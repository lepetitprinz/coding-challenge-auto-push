import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(start, moves, visited):
    r, c = start
    queue = deque([start])
    visited[r][c] = True
    
    while queue:
        r, c = queue.popleft()
        for move in moves:
            nr = r + move[0]
            nc = c + move[1]
            
            if (0 <= nr < h) and (0 <= nc < w) and not visited[nr][nc]:
                queue.append([nr, nc])
                visited[nr][nc] = True
    
    return visited

hash_map = {'#': 0, '.': 1}
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    visited = []
    for _ in range(h):
        row = list(input())
        conv_row = [hash_map[v] for v in row]
        visited.append(conv_row)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                cnt += 1
                visited = bfs([i, j], moves, visited)

    print(cnt)