import sys
from collections import deque

def bfs(start, end, visited):
    col, row = start
    queue = deque([[col, row, 0]])
    
    while queue:
        col, row, cnt = queue.popleft()
        if (col == end[0]) and (row == end[1]):
            break
        
        for move in moves:
            m_col = col + move[0]
            m_row = row + move[1]
            if (0 <= m_col < l) and (0 <= m_row < l):
                if not visited[m_col][m_row]:
                    visited[m_col][m_row] = True
                    queue.append([m_col, m_row, cnt + 1])
    
    return cnt

moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
test = int(input())
for _ in range(test):
    l = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    visited = [[False] * l for _ in range(l)]
    cnt = bfs(start, end, visited)
    print(cnt)