import sys

input = lambda: sys.stdin.readline().rstrip()

def bfs(x, y, result):
    queue = set([(x, y, arr[x][y])])
    while queue:
        x, y, history = queue.pop()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if (0 <= nx < r) and (0 <= ny < c):
                new_alpha = arr[nx][ny]
                if new_alpha not in history:
                    queue.add((nx, ny, history + new_alpha))
                    result = max(result, len(history) + 1)

    return result


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = bfs(0, 0, 1)
print(result)