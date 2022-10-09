def solution(n, num):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    arr = [[0] * n for _ in range(n)]

    r, c = (0, 0)
    cnt = n ** 2 - 1
    direction = 0
    point = (1, 1)

    arr[r][c] = cnt + 1
    while cnt > 0:
        move = moves[direction]
        nr = r + move[0]
        nc = c + move[1]

        if (0 <= nr < n) and (0 <= nc < n) and arr[nr][nc] == 0:
            arr[nr][nc] = cnt
            r, c = (nr, nc)
            if cnt == num:
                point = (r + 1, c + 1)
            cnt -= 1
        else:
            direction = (direction + 1) % 4

    return arr, point

n = int(input())
num = int(input())

arr, point = solution(n, num)
for row in arr:
    print(*row)
print(*point)