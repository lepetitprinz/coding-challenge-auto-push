def dfs(x, y, seq):
    if len(seq) == 6:
        if seq not in result:
            result.append(seq)
        return
    
    for move in moves:
        dx = x + move[0]
        dy = y + move[1]
        if (0 <= dx < 5) and (0 <= dy < 5):
            dfs(dx, dy, seq + arr[dx][dy])

arr = [list(map(str, input().split())) for _ in range(5)]
moves = [(-1,0), (1,0), (0,-1), (0,1)]
result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
        
print(len(result))