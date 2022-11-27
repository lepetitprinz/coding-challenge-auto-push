c, r = map(int, input().split())
num = int(input())

if c * r < num:
    print(0)
else:
    loc = (0, 0)
    direction = 0
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    while num > 1:
        move = moves[direction]
        nr = loc[0] + move[0]
        nc = loc[1] + move[1]
        if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
            loc = (nr, nc)
            visited[nr][nc] = True
        else:
            direction = (direction + 1) % 4
            move = moves[direction]
            nr = loc[0] + move[0]
            nc = loc[1] + move[1]
            loc = (nr, nc)
            visited[nr][nc] = True
        
        num -= 1
    loc = (loc[1] + 1, loc[0] + 1)

    print(*loc)