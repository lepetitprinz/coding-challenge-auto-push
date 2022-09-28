import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(arr, r, c, n):
    value = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != value:
                n = n // 3
                solution(arr, r, c, n)
                solution(arr, r, c + n, n)
                solution(arr, r, c + 2 * n, n)
                solution(arr, r + n, c, n)
                solution(arr, r + n, c + n, n)
                solution(arr, r + n, c + 2 * n, n)
                solution(arr, r + 2 * n, c, n)
                solution(arr, r + 2 * n, c + n, n)
                solution(arr, r + 2 * n, c + 2 * n, n)
                return
                
    result[value] += 1
    
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = {-1: 0, 0: 0, 1: 0}
solution(arr, 0, 0, n)
for val in result.values():
    print(val)