import sys
sys.setrecursionlimit(2500)

def dfs(graph, x, y):
    if x <= -1 or x >= m or y <= -1 or y >=n:
        return False
    
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph, x-1, y)
        dfs(graph, x, y-1)
        dfs(graph, x+1, y)
        dfs(graph, x, y+1)
        return True
    
    return False

test = int(input())
for _ in range(test):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, sys.stdin.readline().split())
        graph[j][i] = 1
        
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(graph, j, i):
                result += 1
    
    print(result)