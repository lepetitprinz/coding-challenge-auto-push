import sys

n = int(input())
arr = list(map(int, input().split()))
swap = -1
for i in range(n-1, 0, -1):
    if arr[i - 1] < arr[i]:
        swap = i - 1
        break
else:
    print(-1)
    sys.exit()

for i in range(n-1, 0, -1):
    if arr[swap] < arr[i]:
        arr[swap], arr[i] = arr[i], arr[swap]
        arr = arr[:swap + 1] + sorted(arr[swap + 1:])
        print(*arr)
        break