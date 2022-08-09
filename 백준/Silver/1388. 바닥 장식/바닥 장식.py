import sys
sys.setrecursionlimit(100)

def dfs(x, y, arr, visited):
    if visited[x][y]:
        return False
    else:
        visited[x][y] = 1

    if arr[x][y] == '-':
        if y - 1 >= 0:
            if arr[x][y - 1] == '-':
                dfs(x, y - 1, arr, visited)
        if y + 1 < m:
            if arr[x][y + 1] == '-':
                dfs(x, y + 1, arr, visited)
    else:
        if x - 1 >= 0:
            if arr[x - 1][y] == '|':
                dfs(x - 1, y, arr, visited)
        if x + 1 < n:
            if arr[x + 1][y] == '|':
                dfs(x + 1, y, arr, visited)

    return True

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

visited = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        cnt += dfs(i, j, arr, visited)

print(cnt)