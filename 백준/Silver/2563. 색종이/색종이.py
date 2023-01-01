import sys

input = lambda: sys.stdin.readline().strip()

arr = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x + i - 1][y + j - 1] = 1
    

result = sum(sum(row) for row in arr)
print(result)