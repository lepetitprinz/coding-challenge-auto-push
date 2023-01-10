import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    cum_sum = 0
    cum_sum_row = []
    for val in row:
        cum_sum += val
        cum_sum_row.append(cum_sum)

    arr.append(cum_sum_row)
    
def add(arr, x1, y1, x2, y2):
    result = 0
    for i in range(x1, x2 + 1):
        if y1 == 0:
            result += arr[i][y2]
        else:
            result += arr[i][y2] - arr[i][y1 - 1]
    
    return result
    
k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    result = add(arr, x1-1, y1-1, x2-1, y2-1)
    print(result)