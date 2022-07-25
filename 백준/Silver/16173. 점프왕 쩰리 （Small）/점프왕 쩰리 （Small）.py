import sys
sys.setrecursionlimit(100000)

def dfs(r, c, m, n):
    flag = False
    if r == n-1 and c == n-1:
        return True
    elif m == 0:
        return False
    else:
        for move in moves:
            if flag:
                break
            move_r = move[0] * m + r
            move_c = move[1] * m + c
            if move_r < 0 or move_r >= n or move_c < 0 or move_c >= n:
                continue
            else:
                flag = dfs(move_r, move_c, arr[move_r][move_c], n)

    return flag


n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

moves = [[0, 1], [1, 0]]
if dfs(0, 0, arr[0][0], n):
    print('HaruHaru')
else:
    print('Hing')