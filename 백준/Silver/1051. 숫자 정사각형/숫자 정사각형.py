import sys

def check(arr, i, j, l):
    flag = False
    if len(set([arr[i][j], arr[i][j + l], arr[i + l][j], arr[i + l][j + l]])) == 1:
        flag = True

    return flag

n, m = map(int, input().split())
arr = [[int(v) for v in list(sys.stdin.readline().rstrip())] for _ in range(n)]

result = 0
length = min(n, m)
for l in range(1, length):
    for i in range(n - l + 1):
        for j in range(m - l + 1):
            if (i + l < n) & (j + l < m):
                if check(arr=arr, i=i, j=j, l=l):
                    result = l
                    break

print((result + 1) ** 2)