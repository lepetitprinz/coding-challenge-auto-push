import sys

def solution(x, y, n):
    value = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if value != arr[i][j]:
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return

    result.append(value)


n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []
solution(0, 0, n)
print(result.count(0))
print(result.count(1))