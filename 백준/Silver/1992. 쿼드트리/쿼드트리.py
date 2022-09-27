import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(arr, x, y, n):
    value = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if value != arr[i][j]:
                result.append('(')
                solution(arr, x, y, n//2)
                solution(arr, x, y + n//2, n//2)
                solution(arr, x + n//2, y, n//2)
                solution(arr, x + n//2, y + n//2, n//2)
                result.append(')')
                return
    
    result.append(value)
    
n = int(input())
arr = [input() for _ in range(n)]
result = []
solution(arr, 0, 0, n)
print(''.join(result))