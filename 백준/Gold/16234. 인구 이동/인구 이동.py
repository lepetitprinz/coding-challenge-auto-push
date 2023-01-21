import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def check(arr):
    for i in range(n):
        for j in range(n):
            value = arr[i][j]
            for move in [(1, 0), (0, 1)]:
                ni = i + move[0] 
                nj = j + move[1]
                if (0 <= ni < n) and (0 <= nj < n):
                    if l <= abs(value - arr[ni][nj]) <= h:
                        return True
        
    return False

def bfs(arr, start, visited):
    x, y = start
    queue = deque([[x, y, [(x, y)], [arr[x][y]]]])
    visited[x][y] = True
    
    # Finding phase
    while queue:
        x, y, point_arr, val_arr = queue.popleft()
        val = arr[x][y]
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
                new_val = arr[nx][ny]
                if l <= abs(val - new_val) <= h:
                    point_arr.append((nx, ny))
                    val_arr.append(new_val)
                    visited[nx][ny] = True
                    queue.append([nx, ny, point_arr, val_arr])
    # Update phase
    else:
        update_value = sum(val_arr) // len(val_arr)
        for x, y in point_arr:
            arr[x][y] = update_value
    
    return arr, visited

n, l, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cycle = 0
while True:
    visited = [[False] * n for _ in range(n)]
    if check(arr):
        cycle += 1
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    arr, visited = bfs(arr, (i, j), visited)
    else:
        break

print(cycle)